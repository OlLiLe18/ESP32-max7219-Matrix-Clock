# 🕒 ESP32 MAX7219 Smart Matrix Clock (96x8 Pixel)

Eine smarte 96x8 LED-Matrix-Uhr basierend auf einem ESP32 und ESPHome, vollständig integriert in Home Assistant.

---
<img width="1195" height="896" alt="Clock max7219 (1)" src="https://github.com/user-attachments/assets/46acfe09-3d6f-4676-9f4f-9e3fb7cb2ba8" />

---

![Smarte ESP32 Matrix Uhr](images/MAX7219 Smart Matrix Clock(1).jpg)

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

<p align="center">
  <strong>💖 Dir gefällt mein Projekt?</strong><br><br>
  <a href="https://www.paypal.com/donate/?hosted_button_id=R3GX3HE8RF4LW"><strong>☕ Spende mir ein Kaffee via PayPal</strong></a>
</p>

---


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

---

<details>
<summary>🇬🇧 English Version (Click to expand)</summary>

### ESP32 MAX7219 Smart Matrix Clock (96x8 pixels)

A smart 96x8 LED matrix clock based on an ESP32 and ESPHome, fully integrated with Home Assistant.

## ✨ Features

- ⏰ **Large Time:** Perfectly legible numbers with bold doubled flashing colon
- 📅 **Date overlay:** Automatically every minute for 5 seconds (second :50 to :55) with 📅 -icon
- 🌡️ **Home Assistant Integration:** Live outdoor temperature directly from Home Assistant
- 👾 **Expressive & Retro Icons:** 8x8 pixel art animations (Pulsating Heart, Pac-Man, Space Invader, Coffee with Steam, Sun, etc.)
- 🌙 **Automatic Night Mode:** Adjustable start/end time and dimming level (incl. true blanking/shutdown at level 0)
- 📜 **Scrolling text mode:** Scroll, bounce and wipe animations for individual messages from Home Assistant

---

## 🔌 Hardware & Pining (ESP32)

| ESP32-Pin | MAX7219 Display Module | Description |
|---|---|---|
| **5V / VIN** | **VCC** | 5V Power Supply |
| **GND** | **GND** | Mass |
| **GPIO26** | **CLK** | SPI Clock |
| **GPIO27** | **DIN / MOSI** | SPI Data Line |
| **GPIO25** | **CS / LADE** | Chip Selection |

---

<p align="center">
<strong>💖 You like my project?</strong><br><br>
<a href="https://www.paypal.com/donate/?hosted_button_id=R3GX3HE8RF4LW"> <strong>☕ Donate me a coffee via PayPal</strong></a>
</p>

---


## 🚀 Easy installation with ESPHome Device Builder

Thanks to the modern ESPHome interface in Home Assistant, setup is done in just a few steps:

### 1. Provide fonts
Download the two font files from the ['/fonts'](./fonts) folder and place them in your Home Assistant file system at the following path:
'/config/esphome/fonts/' (e.g. via the *File Editor*, *Studio Code Server*, or *Samba Share* add-on).
- 'basis33.ttf'
- 'pixelmix.ttf'

### 2. Enter WLAN & access data (Secrets)
1. Open the **ESPHome Dashboard** in the Home Assistant.
2. Click on the **three-dot menu '⋮'** $\rightarrow$ **'Secrets'** in the top right-hand corner.
3. Make sure that your Wi-Fi access data is stored there:
'''yaml
wifi_ssid: "YourWLANName"
wifi_password: "YourWLANPasswort"

### 3. Create a new device and insert YAML code
1. In the ESPHome dashboard, click on the blue + Create Device (or New Device) button in the bottom right corner.
2. Click on Continue See image in "Create Configuration ESPHome Builder – Home Assistant and" enter the device name exactly: max7219-esp32-reg.
3. Select ESP32 as the platform.
4. Click Skip / Finish.
5. A new map will appear for your device. Click Edit on the map.
6. Delete all the default code in the editor and paste the complete contents of the max7219-esp32-reg.yaml file.
7. Important: If necessary, adjust your api and ota keys or check the configuration.
8. Customize optionally: Find the line entity_id: sensor.aussenthermometer_temperature and enter the name of your own temperature sensor from Home Assistant there.
9. Click Save in the top right, then click Close

### 4. Install / flash firmware

1. Click on the three-dot menu ⋮ Install on the new device card.
2. Select the desired installation method:
3. Connected to this computer: For the initial installation, flash conveniently via USB cable directly via the browser. [! [web.esphome.io] (https://shields.io)] (https://web.esphome.io/)
5. On the network (OTA): For all subsequent updates, wirelessly via Wi-Fi.

</details>
