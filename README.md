# 🌱 Smart Agricultural Monitoring System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![RaspberryPi](https://img.shields.io/badge/Hardware-Raspberry_Pi-red)
![Proteus](https://img.shields.io/badge/Simulation-Proteus-important)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, IoT-powered agricultural monitoring system for real-time crop analysis and voice-activated irrigation control using Raspberry Pi and machine learning.

![PDS_URFy9j8o6R](https://github.com/user-attachments/assets/40933212-1688-4107-b96d-e009a464e6f1)

---

## 🚀 Key Features

### 🔧 Hardware Implementation

- **Soil Monitoring Suite**:
  - Capacitive soil moisture sensor (Analog via MCP3008)
  - LM35 temperature sensor (±0.5°C accuracy)
  - pH sensor (0–14 range, pH-4502C)
  - Rain gauge (0.2mm resolution tipping bucket)

- **Control & Output**:
  - Dual 5V DC water pumps (relay-controlled)
  - 16x2 HD44780 LCD display
  - 4x3 Matrix Keypad
  - Visual feedback via status LEDs

- **Communication**:
  - SPI interface for analog sensor reading
  - UART serial for debugging and Proteus simulation

---

### 🧠 Smart Algorithms

- **Irrigation Control**:
  - K-Nearest Neighbors (KNN) Classifier (k=5)
  - Triggered when:
    - Moisture < 30%
    - Temperature > 25°C

- **Crop Recommendation**:
  - KNN model trained on 2200+ crop samples
  - Input features: Temperature, Humidity, pH, Rainfall
  - Test Accuracy: **89.7%**

---

### 🎤 Voice Control

- Google Speech Recognition API integration  
- Voice trigger word: **“start”**
- Feedback shown on LCD screen

---

## 📐 System Architecture

```
┌───────────────────────────────────────────────────────┐
│                    Raspberry Pi 4                     │
│ ┌─────────────┐  ┌─────────────┐  ┌────────────────┐ │
│ │   Sensors   │  │   Control   │  │  ML Models     │ │
│ │ - Moisture  │  │ - Pumps     │  │ - Irrigation   │ │
│ │ - Temp      │  │ - LCD       │  │ - Crop Recomm. │ │
│ │ - pH        │  │ - Keypad    │  └────────────────┘ │
│ │ - Rain      │  └─────────────┘                     │
│ └─────────────┘                    ┌───────────────┐ │
│                                    │ Voice Control │ │
│                                    │ - Recognition │ │
│                                    │ - Validation  │ │
│                                    └───────────────┘ │
└───────────────────────────────────────────────────────┘
```

---

## 🧰 Hardware Pinout

| Component        | GPIO Pin       | Interface     | Notes                        |
|------------------|----------------|---------------|------------------------------|
| Soil Moisture    | CH0            | SPI (MCP3008) | 10-bit ADC                   |
| Temperature      | CH1            | SPI           | LM35 analog out              |
| Humidity Sensor  | CH2            | SPI           | Custom capacitive sensor     |
| pH Sensor        | CH4            | SPI           | pH-4502C module              |
| Rain Gauge       | GPIO7          | Digital       | Tip counter                  |
| Pump 1           | GPIO31         | Relay         | 5V control                   |
| Pump 2           | GPIO29         | Relay         | Backup pump                  |
| LCD RS           | GPIO13         | Parallel      | HD44780                      |
| LCD E            | GPIO26         | Parallel      |                              |
| Keypad (Rows)    | 33, 36, 35, 12 | Matrix        | 4x3 Configuration            |

---

## 🛠️ Installation

### Hardware Setup

```bash
# Enable SPI interface on Raspberry Pi
sudo raspi-config nonint do_spi 0
```

### Install Software Requirements

```bash
pip install -r requirements.txt
```

#### Core Libraries:
- `RPi.GPIO`
- `spidev`
- `scikit-learn`
- `SpeechRecognition`
- `pyserial`

---

## 🔧 Calibration

- **Rain Gauge**:
  - Modify `CALIBRATION_FACTOR_MM` based on actual tip volume

- **pH Sensor**:
  - Adjust calibration offset in `CONVERT_PH()` for accurate readings

---

### Data Logging

- Directory: `/ProjectBackups/`
- Format: CSV
- Includes timestamps and sensor readings

---

## 🧪 Proteus Simulation

The system includes a complete simulation model using **Proteus**, featuring:

- Virtual Raspberry Pi microcontroller
- Adjustable sensor models
- Simulated pumps
- UART debug console

📷 *Include your Proteus screenshot here (`proteus_simulation.png`)*

---

## 📁 Project Structure

```
AgriMonitor/
├── hardware/               # Proteus design files
│   ├── schematic.DSN
│   └── PCB_Layout.pds
├── firmware/               # Raspberry Pi code
│   ├── main.py             # Primary control logic
│   ├── sensors.py          # Sensor interfaces
│   └── ml_models/          # Trained models
├── datasets/               # Training data
│   ├── irrigation_data.csv
│   └── crop_recommendation.csv
└── docs/                   # Documentation
    ├── wiring_diagram.pdf
    └── calibration_guide.md
```

---

## 📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
