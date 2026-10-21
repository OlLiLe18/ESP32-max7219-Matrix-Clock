from pathlib import Path
import shutil
import subprocess
import tempfile
import textwrap

# Execute the actual YAML rendering lambda with simulated ESPHome entities.
# This checks control flow and draw coordinates, not SPI or physical rendering.
root = Path(__file__).resolve().parents[1]
src = (root / 'max7219-esp32-reg.yaml').read_text()
block = src.split('\ndisplay:\n', 1)[1].split('    lambda: |-\n', 1)[1].split('\n############################################################', 1)[0]
body = textwrap.dedent(block)
harness = r'''
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <limits>
#include <string>
#include <vector>
#define id(x) x
constexpr bool COLOR_OFF = false;
constexpr bool COLOR_ON = true;
enum class TextAlign { TOP_CENTER, TOP_LEFT, CENTER_LEFT };
struct Time { int hour=12, minute=0, second=0, day_of_week=1, day_of_month=22, month=10; bool valid=true; bool is_valid() const { return valid; } };
struct Clock { Time value; Time now() const { return value; } } sntp_time;
struct Schedule { Time value; Time state_as_esptime() const { return value; } } night_mode_start, night_mode_end;
struct Switch { bool state=true; } night_mode_enabled, display_power, show_date_enabled;
struct Number { float state=3; } display_brightness, night_brightness;
struct Select { std::string value; std::string current_option() const { return value; } } display_page, text_animation;
struct Text { std::string state; } display_text;
struct Sensor { float state=21.5; bool valid=true; bool has_state() const { return valid; } } temp_sensor;
int font_pixelmix=0, digit_font_basis=1, digit_font_basis15=2;
bool time_sync_done=true, icon_anim_phase=false;
uint32_t anim_frame=0;
int current_applied_intensity=-1, text_anim_pos=0, text_anim_dir=1, active_smiley=0;
struct Display {
  std::vector<int> brightness;
  std::vector<std::string> text;
  int pixels=0; bool blank=false;
  int get_width() const { return 96; }
  int get_height() const { return 8; }
  void intensity(uint8_t v) { brightness.push_back(v); }
  void fill(bool) { blank=true; }
  void print(int,int,int,const char* s) { text.emplace_back(s); }
  void print(int,int,int,TextAlign,const char* s) { text.emplace_back(s); }
  template<typename... Args> void printf(int,int,int,TextAlign,const char* fmt,Args... args) {
    char buf[128]; std::snprintf(buf,sizeof(buf),fmt,args...); text.emplace_back(buf);
  }
  void get_text_bounds(int,int,const char* s,int,TextAlign,int* x,int* y,int* w,int* h) {
    *x=*y=0; *w=std::strlen(s)*5; *h=8;
  }
  void draw_pixel_at(int x,int y,bool) { assert(x>=0 && x<96 && y>=0 && y<8); pixels++; }
};
void render(Display& it) {
__BODY__
}
void reset() {
 sntp_time.value=Time{}; night_mode_start.value=Time{}; night_mode_start.value.hour=22;
 night_mode_end.value=Time{}; night_mode_end.value.hour=7;
 night_mode_enabled.state=display_power.state=show_date_enabled.state=true;
 display_brightness.state=3; night_brightness.state=0;
 time_sync_done=true; current_applied_intensity=-1; anim_frame=0;
 text_anim_pos=0; text_anim_dir=1; active_smiley=0; icon_anim_phase=false;
 display_page.value="Clock"; text_animation.value="Scroll"; display_text.state="";
 temp_sensor.valid=true; temp_sensor.state=21.5;
}
int main() {
 reset(); Display d; render(d); assert(d.brightness.back()==3 && !d.text.empty());
 render(d); assert(d.brightness.size()==1);
 display_brightness.state=9; render(d); assert(d.brightness.back()==9);
 sntp_time.value.hour=23; render(d); assert(d.blank && d.brightness.back()==0);
 auto calls=d.brightness.size(); display_brightness.state=15; render(d); assert(d.brightness.size()==calls);
 night_brightness.state=2; render(d); assert(d.brightness.back()==2);
 sntp_time.value.hour=7; render(d); assert(d.brightness.back()==15);
 display_power.state=false; render(d); assert(d.brightness.back()==0);
 display_power.state=true; render(d); assert(d.brightness.back()==15);
 // Exercise every minute around an overnight schedule and a same-day schedule.
 for (bool overnight : {true,false}) {
   reset(); night_mode_start.value.hour=overnight?22:9; night_mode_end.value.hour=overnight?7:17;
   night_brightness.state=1;
   for(int minute=0; minute<1440; minute++) {
     sntp_time.value.hour=minute/60; sntp_time.value.minute=minute%60;
     Display frame; render(frame);
     bool night=overnight?(minute>=22*60 || minute<7*60):(minute>=9*60 && minute<17*60);
     assert(current_applied_intensity==(night?1:3));
   }
 }
 // All icons and both animation phases stay within the 96x8 canvas.
 for(int icon=0; icon<7; icon++) for(bool phase:{false,true}) {
   reset(); active_smiley=icon; icon_anim_phase=phase; Display frame; render(frame); assert(frame.pixels>0);
 }
 for(int sec=0; sec<60; sec++) {
   reset(); sntp_time.value.second=sec; Display frame; render(frame);
   assert(frame.text[0].find("22.10.")!=std::string::npos ? (sec>=50 && sec<=55) : !(sec>=50 && sec<=55));
 }
 reset(); sntp_time.value.valid=false; Display unsynced; render(unsynced); assert(unsynced.text[0]=="SYNC...");
 reset(); temp_sensor.state=std::numeric_limits<float>::quiet_NaN(); Display missing; render(missing); assert(missing.text.back()=="--.-°");
 for(const char* mode:{"Scroll","Bounce","Wipe","Static"}) {
   reset(); display_page.value="Text"; text_animation.value=mode; display_text.state=std::string(64,'W');
   for(int n=0;n<2000;n++) { Display frame; render(frame); assert(!frame.text.empty()); assert(text_anim_pos>=0); }
 }
 reset(); display_page.value="Text"; Display empty; render(empty); assert(empty.text[0]=="-");
 display_text.state="Hello"; Display short_text; render(short_text); assert(short_text.text[0]=="Hello");
 std::puts("PASS: brightness writes/cache, day/night boundaries (2,880 minutes), power transitions, all 14 icon frames, date timing, invalid time/temperature, empty/short text, and all four text modes (8,000 frames).");
}
'''
compiler = shutil.which('clang++') or shutil.which('g++')
if compiler is None:
    raise SystemExit('Install clang++ or g++ to run the display logic checks.')
with tempfile.TemporaryDirectory(prefix='matrix-clock-logic-') as directory:
    source = Path(directory) / 'display_logic.cpp'
    executable = Path(directory) / 'display_logic'
    source.write_text(harness.replace('__BODY__', body))
    subprocess.run([compiler, '-std=c++17', str(source), '-o', str(executable)], check=True)
    subprocess.run([str(executable)], check=True)
