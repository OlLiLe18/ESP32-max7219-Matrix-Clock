# 🕒 ESP32 MAX7219 Smart Matrix Clock (96×8 Pixels)

A smart 96×8 LED matrix clock built with an ESP32 and ESPHome, fully integrated with Home Assistant.

This is an English documentation fork of [OlLiLe18's original project](https://github.com/OlLiLe18/ESP32-max7219-Matrix-Clock). The README and configuration comments have been translated; the firmware settings and display behaviour are unchanged.

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

The display uses a chain of 12 MAX7219 8×8 modules, giving a total resolution of 96×8 pixels.

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

1. Open the **ESPHome dashboard** in Home Assistant.
2. Open the three-dot menu **⋮** at the top right and select **Secrets**.
3. Store your Wi-Fi credentials in `secrets.yaml`:

    ```yaml
    wifi_ssid: "YourWiFiName"
    wifi_password: "YourWiFiPassword"
    ```

The supplied firmware YAML currently uses inline placeholders. To use the Wi-Fi secrets above, replace its `wifi.ssid` and `wifi.password` values with:

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
```

The file [`secrets.example.yaml`](./secrets.example.yaml) contains example ESPHome configuration sections with placeholder credentials. It is a configuration reference; the entries shown in the first example above are the key/value format used by `secrets.yaml`.

### 3. Create the Device and Paste the YAML

1. In the ESPHome dashboard, click **+ New Device** or **Create Device**.
2. Click **Continue** and enter the device name exactly as `max7219-esp32-reg`. The [original setup screenshot](<Konfiguration erstellen ESPHome Builder – Home Assistant.png>) shows this step in German.
3. Select **ESP32** as the platform.
4. Complete the wizard using **Skip** or **Finish**, as appropriate.
5. Find the new device card and click **Edit**.
6. Replace the generated configuration with the complete contents of [`max7219-esp32-reg.yaml`](./max7219-esp32-reg.yaml).
7. Replace `DEIN_API_KEY` with your valid ESPHome API encryption key and `DEIN_OTA_PASSWORT` with your OTA password. Set the Wi-Fi credentials directly or use the `!secret` references described above, and choose a secure fallback hotspot password under `wifi.ap.password`.
8. Find `entity_id: sensor.aussenthermometer_temperature` and replace the entity ID with your own Home Assistant temperature sensor.
9. Review the configuration, then click **Save** and **Close**.

The original configuration uses the `Europe/Berlin` time zone and German weekday abbreviations (`SO`, `MO`, `DI`, `MI`, `DO`, `FR`, `SA`). Change the `time.timezone` value if needed for your location; the documentation translation retains these original firmware defaults.

### 4. Install the Firmware

Open the new device card's three-dot menu **⋮** and select **Install**. Choose **Plug into this computer** for the first installation over USB, or **Wirelessly** / **Over the air (OTA)** for later updates over Wi-Fi.

For browser-based USB flashing, use [ESPHome Web](https://web.esphome.io/).
