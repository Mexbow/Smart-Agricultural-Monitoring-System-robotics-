# Smart Agricultural Monitoring System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![RaspberryPi](https://img.shields.io/badge/Hardware-Raspberry_Pi-red)
![Proteus](https://img.shields.io/badge/Simulation-Proteus-important)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent system for real-time crop monitoring and irrigation control using Raspberry Pi, multiple environmental sensors, and machine learning.

![System Diagram](WhatsApp-Image-2025-02-11-at-13.54.56_fe680e07.jpg)

## Key Features

### Hardware Implementation
- **Soil Monitoring Suite**:
  - Capacitive soil moisture sensor (Analog)
  - LM35 temperature sensor (±0.5°C accuracy)
  - pH sensor (0-14 range)
  - Rain gauge (0.2mm resolution tipping bucket)

- **Control System**:
  - 2x DC water pumps (5V/1A)
  - 16x2 LCD display (HD44780)
  - 4x3 matrix keypad
  - Status LEDs

- **Communication**:
  - UART serial communication
  - SPI interface for analog sensors

### Smart Algorithms
- **Task 1: Irrigation Control**:
  - KNN classifier (k=5) for pump activation
  - Decision threshold: Moisture < 30% AND Temp > 25°C

- **Task 2: Crop Recommendation**:
  - Multi-parameter KNN model (temperature, humidity, pH, rainfall)
  - Trained on 2200+ crop samples
  - 89.7% test accuracy

### Voice Interface
- Google Speech Recognition API
- Voice command activation ("start")
- Real-time feedback via LCD

## System Architecture

```plaintext
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
