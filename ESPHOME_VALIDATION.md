# ESPHome Validation

Checked on 22 October 2026 against ESPHome `2026.10.0`, using Python `3.12.14`, the `esp32dev` board, Arduino `3.3.12`, and ESP-IDF `5.5.6`.

---

## Result

The corrected `max7219-esp32-reg.yaml` passes ESPHome configuration validation and a complete ESP32 firmware build. Compilation used temporary test credentials in an isolated directory. No device was connected or flashed.

The build reported flash usage of 968,307 bytes out of 1,835,008 bytes (52.8%), and static RAM usage of 49,932 bytes out of the reported 180,736-byte budget (27.6%). These figures do not measure runtime heap usage or prove stability on hardware.

The repository contains the tested source and configuration template. Generate firmware again with your own credentials before installing it.

---

## Issues Found and Fixed

### Captive Portal Configuration

The original `captive_portal` entry was nested inside `wifi.ap`. ESPHome rejected it as an invalid option. It is now a top-level component, as required by the [ESPHome captive portal configuration](https://esphome.io/components/captive_portal/).

### Credentials and API Key

The original `DEIN_API_KEY` placeholder failed ESPHome's base64 key validation. The device configuration now uses `!secret` references, and `secrets.example.yaml` contains the corresponding key/value entries. Its API key placeholder must be replaced with a unique base64-encoded 32-byte key. Use `openssl rand -base64 32` to generate one.

The old example file contained complete ESPHome component sections rather than a usable secrets mapping. It is now a template that can be copied to `secrets.yaml`, or merged into an existing Home Assistant secrets file. No real credentials were used or added to the repository.

### Runtime Brightness Updates

In the MAX7219 matrix driver, `set_intensity()` only updates the stored intensity value. The runtime `intensity()` method also transmits the command to the chips. The rendering lambda now uses `intensity()` when the target brightness changes, following the [documented MAX7219 intensity interface](https://esphome.io/components/display/max7219digit/#max7219intensity-action).

The direct brightness and power callbacks were removed. The display lambda applies the current power and day/night settings together on the next 50 ms frame, keeping its brightness cache consistent and preventing the daytime slider from overriding night brightness.

### Text Animation

The driver's built-in scrolling is enabled by default. It could scroll the extended buffer while the custom lambda was already animating the same text. The configuration now sets `scroll_enable: false` so that the custom Scroll, Bounce, Wipe, and Static modes control positioning.

### Unavailable Temperature

The temperature display now checks that the sensor value is finite, as well as checking that a state exists. Unavailable or invalid readings display `--.-°` instead of `nan°`.

---

## Software Checks Completed

ESPHome configuration validation and the full firmware build both completed successfully. The bundled TrueType fonts were loaded successfully; their digit and text glyph heights fit the intended eight-pixel display height.

The script `scripts/check_display_logic.py` extracts and executes the actual display lambda using simulated ESPHome entities and a recording display. It checks:

- Brightness changes, cached updates, blank night mode, and power off/on transitions.
- Every minute of an overnight schedule and a same-day schedule, covering 2,880 simulated minutes.
- All seven icons in both animation phases, with icon coordinates inside the 96×8 canvas.
- Date display timing at seconds `:50`–`:55`, inclusive, and the unsynchronised clock state.
- Invalid temperature handling and empty or short text.
- Scroll, Bounce, Wipe, and Static modes over 8,000 simulated frames.

The simulation verifies control flow and icon coordinates. It does not emulate the MAX7219 electrical interface, font rasterisation, Wi-Fi, SNTP, Home Assistant, or the complete ESP32 runtime.

ESPHome emitted an advisory recommending encrypted OTA instead of the existing OTA password mechanism. The password mechanism remains accepted and compiled successfully.

---

## Repeating the Checks

After creating `secrets.yaml` with your own values, use an ESPHome `2026.10.0` environment to run:

```sh
esphome config max7219-esp32-reg.yaml
esphome compile max7219-esp32-reg.yaml
```

The host simulation requires Python 3 and either `clang++` or `g++`:

```sh
python3 scripts/check_display_logic.py
```

---

## Before the First Hardware Test

1. Confirm that the board is a classic ESP32 compatible with `esp32dev`. An ESP32-S3 or another variant needs its own board configuration and suitable pins.
2. Confirm that the display has 12 chained MAX7219 8×8 modules, matching `num_chips: 12` and the 96×8 drawing coordinates.
3. Check the regulated 5 V supply, current capacity, shared ground, and logic-level requirements. Confirm `GPIO26` → `CLK`, `GPIO27` → `DIN`, and `GPIO25` → `CS` against the actual hardware.
4. Enter your Wi-Fi and API/OTA credentials and choose the Home Assistant temperature entity. The clock needs network access for SNTP; temperature requires the Home Assistant API connection.
5. Set the `timezone` entry under `time` for your location. The original default is `Europe/Berlin`; `Australia/Sydney` is suitable for Sydney. Weekday abbreviations remain German.
6. After flashing, check module rotation/order, clock and date readability, temperature, all text modes, daytime brightness, night blanking, and power off/on. Use `rotate_chip`, `reverse_enable`, or `flip_x` if required by your module orientation.

The software is ready for a hardware trial after these installation values are configured. Correct wiring, supply quality, physical display orientation, network connectivity, and behaviour on the actual device remain unverified until that trial.
