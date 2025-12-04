![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# VigilantTrack: Dynamic Vehicle Health Monitor

## Overview
VigilantTrack is a comprehensive vehicle health monitoring simulation system designed to demonstrate real-time sensor data processing, predictive maintenance algorithms, and fault-tolerant system architecture. This project simulates the sensor monitoring systems found in modern vehicles, similar to OBD-II diagnostic platforms and advanced driver assistance systems (ADAS). Uses a bell-curve velocity pattern.

**IMPORTANT NOTICE**: This is a SIMULATION program intended for educational and demonstration purposes only. It doesn't currently use data from actual sensors, although it can be added with minimal modification and extension. All sensor data are randomly generated to simulate real-world conditions.

## Purpose
This project serves multiple purposes:

1. Educational Tool - Demonstrates embedded systems concepts and real-time monitoring
2. Portfolio Showcase - Exhibits professional software development practices
3. Proof of Concept - Validates sensor fusion and predictive maintenance algorithms
4. Learning Platform - Provides a foundation for understanding automotive diagnostics systems

Possible Implications: Can replace random sensor data with actual sensor data from an outside source to gather realistic data reading.

## Features

* Multi-Sensor Monitoring
    * 5 types of automotive sensors (Ultrasonic, Camera, Radar, Temperature, Speed)
    * Real-time health tracking with percentage-based degradation
    * Individual sensor status monitoring with color-coded indicators
 
* Real-Time Visualization
    * Live terminal interface with ANSI escape code animations
    * Dynamic data updates without screen flickering
    * Color-coded health indicators (🟢 Green: Good, 🟡 Yellow: Moderate, 🔴 Red: Critical)
    * Countdown timer showing remaining monitoring duration
      
* Predictive Maintenance
    * Simulated sensor health degradation over ride duration
    * Early warning system for sensor failures
    * Critical failure detection with automatic vehicle stop

* Data Analytics
    * Average speed calculation over the monitoring period
    * Average temperature tracking
    * Sensor condition categorization (Critical/Moderate/Good)
    * Comprehensive post-monitoring summary report

* Unit Conversion
    * Support for Imperial units (MP/H, °F)
    * Support for Metric units (KP/H, °C)
    * Real-time conversion during display
 
* Fault Tolerance
    * System continues operation with degraded sensors
    * Graceful handling of individual sensor failures
    * Automatic emergency stop when all sensors reach critical levels
 
## Advanced Features

* Adaptive Sensor Calibration - Automatic health restoration for sensors below threshold
* Sensor Fusion Algorithm - Integrates data from multiple sensor types
* Real-time Data Visualization - Terminal UI with live updates
* Fault Tolerant Framework - Continues operation despite individual sensor failures
* Input Validation & Confirmation - Robust user input handling with error checking

## Component Overview

<pre>
VigilantTrack System
│
├── vigilant_tracker_sensor.py    # Sensor class hierarchy
│   ├── VehicleSensor (Base)      # Common sensor functionality
│   ├── UltrasonicSensor          # Parking assist, collision detection
│   ├── CameraSensor              # Lane detection, visual monitoring
│   ├── RadarSensor               # Adaptive cruise control
│   ├── TemperatureSensor         # Engine thermal monitoring
│   └── SpeedSensor               # Velocity tracking
│
├── loading_animation.py          # UI utilities and animations
│
└── vigilant_tracker_monitor.py  # Main program orchestration
    ├── User Input Module
    ├── Sensor Monitoring Loop
    ├── Data Processing Engine
    └── Reporting System
</pre>

## Installation/Usage

* Prerequisites
    * Python 3.8 or higher
    * Terminal with ANSI escape code support (most modern terminals)
    * No external dependencies required (uses Python standard library only)

> Verify Python Version (and upgrade as needed)

```bash
python --version  # Should be 3.8 or higher
```

> Clone the Repository

```bash
git clone https://github.com/VigneshT24/Python-Vehicle-Monitoring-Program.git
cd Python-Vehicle-Monitoring-Program # you can press tab to autocomplete
```

> Ensure "Emulate terminal in output console" is enabled

For proper terminal animation display in PyCharm:

1. Go to **Run** → **Edit Configurations...**
2. Select your Python configuration (or create a new one)
3. Check the box **"Emulate terminal in output console"**
4. Click **Apply** and **OK**
5. Run the program

**Note**: This setting enables ANSI escape codes for live terminal animations. Without it, you'll see multiple lines instead of smooth updates.

## Technical Specifications

| Sensor Type | ID Format   | Range       | Purpose     | Update Frequency |
| ----------- | ----------- | ----------- | ----------- | ---------------- |
| Ultrasonic | HCSR##  | 4m  | Parking assist, collision detection | 1 Hz |
| Camera | OV####  | 75m  | Lane detection, visual monitoring | 1 Hz |
| Radar | RCWL-####  | 10m | Adaptive cruise control | 1 Hz |
| Temperature | A#### | N/A  | Engine thermal monitoring | 1 Hz |
| Speed | DS##B##  | N/A  | Velocity tracking | 1 Hz |

* Health Thresholds
    * Good (🟢): ≥ 50%
    * Moderate (🟡): 5% - 49%
    * Critical (🔴): < 5%

* Temperature Thresholds
    * Normal (Green): < 100°F (< 37.8°C)
    * Warning (Red): ≥ 100°F (≥ 37.8°C)

* Speed Thresholds
    * Normal (Green): < 80 MP/H (< 128.7 KP/H)
    * Warning (Red): ≥ 80 MP/H (≥ 128.7 KP/H)

* Performance Characteristics
    * Update Rate: 1 second intervals
    * Sensor Array Size: 5 sensors
    * Monitoring Duration: User-defined (recommended: 30-300 seconds)
    * Data Processing: O(n) complexity where n = number of sensors
    * Memory Usage: Minimal (< 10 MB typical)

## Example Images

**DURING RUNTIME:**

<img width="912" height="782" alt="image" src="https://github.com/user-attachments/assets/c1f1daca-14df-40a2-bb47-5542fa4ec6d3" />

**AFTER COMPLETION:**

<img width="791" height="710" alt="image" src="https://github.com/user-attachments/assets/81491961-7646-4ac7-96f6-0bd0ab377bb4" />
