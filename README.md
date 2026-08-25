# 🕒 ESP32 MAX7219 Smart Matrix Clock (96x8 Pixel)

Eine smarte 96x8 LED-Matrix-Uhr basierend auf einem ESP32 und ESPHome, vollständig integriert in Home Assistant.

---
<img width="1195" height="896" alt="Clock max7219 (1)" src="https://github.com/user-attachments/assets/46acfe09-3d6f-4676-9f4f-9e3fb7cb2ba8" />

## ✨ Features

- ⏰ **Große Uhrzeit:** Perfekt lesbare Zahlen mit fett gedoppeltem, blinkendem Doppelpunkt
- 📅 **Datums-Einblendung:** Automatisch jede Minute für 5 Sekunden (Sekunde :50 bis :55) mit 📅-Icon
- 🌡️ **Home Assistant Integration:** Live-Außentemperatur direkt aus Home Assistant
- 👾 **Expressiv- & Retro-Icons:** 8x8 Pixel-Art Animationen (Pulsierendes Herz, Pac-Man, Space Invader, Kaffee mit Dampf, Sonne, etc.)
- 🌙 **Automatischer Nachtmodus:** Einstellbare Start-/Endzeit und Dimmstufe (inkl. echtem Blanking/Abschalten bei Stufe 0)
- 📜 **Lauftext-Modus:** Scroll-, Bounce- und Wipe-Animationen für individuelle Nachrichten aus Home Assistant

---

## 🔌 Hardware & Pinbelegung (ESP32)

| ESP32 Pin | MAX7219 Display-Modul | Beschreibung |
|---|---|---|
| **5V / VIN** | **VCC** | 5V Stromversorgung |
| **GND** | **GND** | Masse |
| **GPIO26** | **CLK** | SPI Clock |
| **GPIO27** | **DIN / MOSI** | SPI Datenleitung |
| **GPIO25** | **CS / LOAD** | Chip Select |

---
Spende zur Unterstützung meiner Software-Entwicklung und Pflege von Open-Source-Projekten auf GitHub.
[![PayPal Spendenseite](https://shields.io)](https://www.paypal.com/donate/?hosted_button_id=R3GX3HE8RF4LW)

## 🚀 Einfache Installation mit dem ESPHome Device Builder

Dank der modernen ESPHome-Oberfläche in Home Assistant ist die Einrichtung in wenigen Schritten erledigt:

### 1. Schriftarten bereitstellen
Lade die beiden Schriftdateien aus dem Ordner [`/fonts`](./fonts) herunter und lege sie in deinem Home Assistant Dateisystem unter folgendem Pfad ab:
`/config/esphome/fonts/` (z. B. über das *File Editor*-, *Studio Code Server*- oder *Samba Share*-Add-on).
- `basis33.ttf`
- `pixelmix.ttf`

### 2. WLAN & Zugangsdaten eintragen (Secrets)
1. Öffne das **ESPHome Dashboard** in Home Assistant.
2. Klicke oben rechts auf das **Drei-Punkte-Menü `⋮`** $\rightarrow$ **`Secrets`**.
3. Stelle sicher, dass deine WLAN-Zugangsdaten dort hinterlegt sind:
   ```yaml
   wifi_ssid: "DeinWLANName"
   wifi_password: "DeinWLANPasswort"

### 3. Neues Gerät anlegen und YAML-Code einfügen
1. Klicke im ESPHome Dashboard unten rechts auf den blauen Button + Gerät erstellen (oder New Device).
2. Klicke auf Weiter (Continue) Siehe Bild in "Konfiguration erstellen ESPHome Builder – Home Assistantund" gib als Gerätenamen genau ein: max7219-esp32-reg.
3. Wähle als Plattform ESP32 aus.
4. Klicke auf Fertigstellen (Skip / Finish).
5. Es erscheint eine neue Karte für dein Gerät. Klicke auf der Karte auf Bearbeiten (Edit).
6. Lösche den gesamten Standard-Code im Editor und füge den kompletten Inhalt der Datei max7219-esp32-reg.yaml ein.
7. Wichtig: Passe ggf. deine api- und ota-Schlüssel an bzw. überprüfe die Konfiguration.
8. Optional anpassen: Suche die Zeile entity_id: sensor.aussenthermometer_temperature und trage dort den Namen deines eigenen Temperatursensors aus Home Assistant ein.
9. Klicke oben rechts auf Speichern und anschließend auf Schließen

### 4. Firmware installieren / flashen

1. Klicke bei der neuen Gerätekarte auf das Drei-Punkte-Menü ⋮ Installieren.
2. Wähle die gewünschte Installationsmethode:
3. An diesen Computer angeschlossen: Für die Erstinstallation bequem per USB-Kabel direkt über den Browser flashen. [![web.esphome.io](https://shields.io)](https://web.esphome.io/)
5. Im Netzwerk (OTA): Für alle späteren Updates kabellos über WLAN.
