---
layout: page
title: RGB Matrix Clock
description: CircuitPython firmware for a 64x32 matrix clock with RTC, sensors, and menu controls.
img: assets/img/projects/rgb-matrix-clock.jpg
importance: 1
category: work
github: https://github.com/gitbenlewis/RGB_Matrix_Clock_waveshare_64_32_pi_pico
---

{% include figure.liquid loading="eager" path="assets/img/projects/rgb-matrix-clock.jpg" title="RGB matrix clock build" class="img-fluid rounded z-depth-1" %}

## Overview

This project is a hardware clock build powered by CircuitPython on a Raspberry Pi Pico-class board and a Waveshare 64x32 RGB matrix panel.
It combines local sensor input with RTC-backed timekeeping and a compact on-device menu for display control.

## Hardware Stack

- Raspberry Pi Pico-class board (UF2 in repo targets Pico 2 W)
- Waveshare 64x32 RGB matrix panel
- DS3231 RTC (I2C)
- DHT22 temperature/humidity sensor
- Photoresistor for ambient light sensing
- Three buttons for menu navigation

## Firmware Structure

The active firmware lives in `RGB_scroll_clock_0215/` and is split by responsibility:

- `code.py`: main loop, refresh cadence, and fault recovery reload
- `display_manager.py`: matrix and label object setup
- `display_updates.py`: time/date rendering, animations, sensor display updates
- `brightness.py`: auto/manual dim logic and color scaling
- `menu.py`: button handling and menu state transitions
- `sensors.py`: DS3231, DHT22, and photoresistor initialization

## Key Features

- Animated 24-hour time display
- Date and weekday row
- Temperature and humidity readout
- Scrolling banner text
- Auto brightness with manual override
- Menu controls for brightness mode and dim level

## Setup Summary

1. Flash CircuitPython UF2 from `RGB_scroll_clock_0215/`.
2. Copy firmware files and `lib/` dependencies to `CIRCUITPY`.
3. Confirm wiring in `config.py` pin mappings.
4. Set display text/colors and brightness defaults in `config.py`.
5. Reboot and verify menu controls and sensor updates.

## Repository

Source code and setup documentation:
[gitbenlewis/RGB_Matrix_Clock_waveshare_64_32_pi_pico](https://github.com/gitbenlewis/RGB_Matrix_Clock_waveshare_64_32_pi_pico)
