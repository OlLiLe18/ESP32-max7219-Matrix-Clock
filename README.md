# 🕒 ESP32 MAX7219 Smart Matrix Clock (96×8 Pixels)

A smart 96×8 LED matrix clock built with an ESP32 and ESPHome, fully integrated with Home Assistant.

This is an English documentation fork of [OlLiLe18's original project](https://github.com/OlLiLe18/ESP32-max7219-Matrix-Clock). The README and configuration comments are in English. The configuration includes the ESPHome compatibility and display fixes described in the [validation notes](./ESPHOME_VALIDATION.md).

![ESP32 MAX7219 matrix clock](<Clock max7219 (2).png>)

---

## ✨ Features

- ⏰ **Large time display:** Easy-to-read digits with a bold, double-drawn blinking colon.
- 📅 **Date display:** Automatically shows the date with a calendar icon at seconds `:50`–`:55` of each minute.
- 🌡️ **Home Assistant integration:** Displays live outdoor temperature from a Home Assistant sensor.
- 👾 **Expressive and retro icons:** Animated 8×8 pixel art, including a pulsing heart, Pac-Man, Space Invader, steaming coffee cup, and sun.
- 🌙 **Automatic night mode:** Adjustable start and end times and brightness, including a blank display at night brightness `0`.
- 📜 **Scrolling text mode:** Scroll, Bounce, and Wipe animations for custom messages from Home Assistant.

---

## 🔌 Hardware and ESP32 Pin Connections

The display uses a chain of 12 MAX7219 8×8 modules, giving a total resolution of 96×8 pixels. Use a regulated 5 V supply sized for the display chain and share ground with the ESP32. Confirm the modules' logic-level requirements when wiring the hardware.

| ESP32 pin  | MAX7219 display module | Description      |
| ---------- | ---------------------- | ---------------- |
| `5V / VIN` | `VCC`                  | 5 V power supply |
| `GND`      | `GND`                  | Ground           |
| `GPIO26`   | `CLK`                  | SPI clock        |
| `GPIO27`   | `DIN / MOSI`           | SPI data         |
| `GPIO25`   | `CS / LOAD`            | Chip select      |

---

## 💖 Support the Original Author

Enjoying the project? [Buy the original author, OlLiLe18, a coffee via PayPal](https://www.paypal.com/donate/?hosted_button_id=R3GX3HE8RF4LW).

---

## 🚀 Installation with ESPHome Device Builder

Use the ESPHome dashboard in Home Assistant to set up the clock.

### 1. Install the Fonts

Download `basis33.ttf` and `pixelmix.ttf` from the [`fonts/`](./fonts/) directory and copy them to `/config/esphome/fonts/` in your Home Assistant filesystem. You can use the File Editor, Studio Code Server, or Samba Share add-on to copy the files.

### 2. Set Up Wi-Fi and Credentials

Copy [`secrets.example.yaml`](./secrets.example.yaml) to `secrets.yaml` beside the device YAML and replace every example value. If you already have a shared `secrets.yaml` in Home Assistant, merge these entries into it instead of replacing the file. In the ESPHome dashboard, use the three-dot menu **⋮** → **Secrets** to edit that file.

Set `wifi_ssid`, `wifi_password`, `api_encryption_key`, `ota_password`, and `fallback_ap_password`. Generate a unique API encryption key using:

```sh
openssl rand -base64 32
```

The device YAML reads these values using `!secret`. Keep `secrets.yaml` private; it is excluded from Git. The API key example intentionally requires replacement before validation or installation.

### 3. Create the Device and Paste the YAML

1. In the ESPHome dashboard, click **+ New Device** or **Create Device**.
2. Click **Continue** and enter the device name exactly as `max7219-esp32-reg`. The [original setup screenshot](<Konfiguration erstellen ESPHome Builder – Home Assistant.png>) shows this step in German.
3. Select **ESP32** as the platform.
4. Complete the wizard using **Skip** or **Finish**, as appropriate.
5. Find the new device card and click **Edit**.
6. Replace the generated configuration with the complete contents of [`max7219-esp32-reg.yaml`](./max7219-esp32-reg.yaml).
7. Confirm that the credentials from step 2 are present in the ESPHome `secrets.yaml` file. Keep the `!secret` references in the device configuration.
8. Find `entity_id: sensor.aussenthermometer_temperature` and replace the entity ID with your own Home Assistant temperature sensor.
9. Review the configuration, then click **Save** and **Close**.

The configuration retains the original `Europe/Berlin` time zone and German weekday abbreviations (`SO`, `MO`, `DI`, `MI`, `DO`, `FR`, `SA`). Set the `timezone` entry under `time` to your location, for example `Australia/Sydney`, before installation.

### 4. Install the Firmware

Open the new device card's three-dot menu **⋮** and select **Install**. Choose **Plug into this computer** for the first installation over USB, or **Wirelessly** / **Over the air (OTA)** for later updates over Wi-Fi.

For browser-based USB flashing, use [ESPHome Web](https://web.esphome.io/).

---

## ESPHome Verification

See [the validation notes](./ESPHOME_VALIDATION.md) for the tested ESPHome version, fixes, software checks, and the checks that still need physical hardware.

To validate and compile after entering your own credentials:

```sh
esphome config max7219-esp32-reg.yaml
esphome compile max7219-esp32-reg.yaml
```

To run the display logic checks on a computer with Python 3 and `clang++` or `g++`:

```sh
python3 scripts/check_display_logic.py
```
