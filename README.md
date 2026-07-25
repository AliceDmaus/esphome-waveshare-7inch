Waveshare 7-inch ESP32-S3 Dashboard
A modern, tile-based smart home dashboard configuration for the Waveshare 7-inch ESP32-S3 Touchscreen, built with ESPHome and LVGL.

⚡ Core Features
2x2 Tile Layout: Clean interface divided into four functional areas.
Weather: Real-time weather conditions with dynamic MDI icons and outdoor temperature.
Climate: Indoor temperature monitoring (with sofa icon).
Smart Appliance: Advanced washing machine monitor that translates states (e.g., run -> 15:30) and calculating finishing times from ISO timestamps.
Visual Timer: Fluid countdown animation (e.g., Pizza Timer) synchronized with Home Assistant helpers.
Performance: optimized for ESP32S3 using PSRAM with custom partition handling.
Optional Debug/Antiburn packages: toggle via the enable_debug / enable_antiburn substitutions in waveshare-7inch.yaml.


🛠️ Requirements
Hardware: Waveshare 7-inch ESP32-S3 Touchscreen.
Software:
Home Assistant (for sensors/entities).
ESPHome 2026.7.2 (Tested & Verified).


🚀 Installation
Copy the images/ and fonts/ folders to your ESPHome configuration directory.
Copy secrets-example.yml to secrets.yaml and fill in your WiFi and API credentials.
Update the entity_id references in packages/ui_sensors.yaml to match your Home Assistant entities.
Compile and upload.

Created with ESPHome & LVGL

<img width="2560" height="1928" alt="image" src="https://github.com/user-attachments/assets/8be34da7-992c-4447-a63e-ef14f955dcc9" />
