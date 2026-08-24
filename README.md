# 🕒 ESP32 MAX7219 Smart Matrix Clock (96x8 Pixel)

Eine smarte 96x8 LED-Matrix-Uhr basierend auf einem ESP32 und ESPHome, vollständig integriert in Home Assistant.

## ✨ Features
- ⏰ **Uhrzeit:** Große Ziffern mit fettem, blinkendem Doppelpunkt
- 📅 **Datums-Einblendung:** Automatisch jede Minute für 5 Sekunden (Sekunde 50-55)
- 🌡️ **Home Assistant Integration:** Live-Außentemperatur aus Home Assistant
- 👾 **Expressiv- & Retro-Icons:** 8x8 Pixel-Art (Herzschlag, Pac-Man, Space Invader, etc.)
- 🌙 **Automatischer Nachtmodus:** Einstellbare Dimm- und Abschaltzeiten über Home Assistant
- 📜 **Lauftext-Modus:** Scroll-, Bounce- und Wipe-Animationen für individuelle Nachrichten

## 🔌 Hardware & Pinbelegung (ESP32)

| ESP32 Pin | MAX7219 Display |
|---|---|
| 5V / VIN | VCC |
| GND | GND |
| GPIO26 | CLK (Clock) |
| GPIO27 | DIN / MOSI (Data) |
| GPIO25 | CS / LOAD (Chip Select) |

Wenn dir dieses Projekt gefällt, unterstütze mich gerne mit einer kleinen Spende.
[![PayPal Spendenseite](https://shields.io)](https://www.paypal.com/donate/?hosted_button_id=R3GX3HE8RF4LW)

## 🚀 Installation
1. Klone dieses Repository oder lade die Dateien herunter.
2. Kopiere die Schriftarten aus `/fonts` in deinen Home Assistant Ordner `/config/esphome/fonts/`.
3. Benenne `secrets.example.yaml` in `secrets.yaml` um und trage dein WLAN-Passwort ein.
4. Installiere die Konfiguration über das ESPHome Dashboard auf deinen ESP32.
