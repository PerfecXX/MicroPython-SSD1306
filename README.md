# MicroPython SSD1306

[![Version](https://img.shields.io/badge/version-1.0.2-green.svg)](https://github.com/PerfecXX/MicroPython-SSD1306)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

MicroPython Library for SSD1306 OLED Displays with some simple shape drawing functions.

# Installation
- Manual Installation
  - Upload the ```ssd1306.py``` file to your device.
- Thonny IDE Package Manager
  - Open Thonny IDE.
  - Go to Tools > Manage Packages.
  - Search for ```micropython-ssd1306-driver``` and install it.

# Example Usage
- [Screen Control](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/screen%20control)
- [Text](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/text)
- [Shape](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/shape)
- [Image](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/image)
- [QRCode](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/QRCode)
- [More Example](https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example)

# Quick Example

```python
# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Text Display (Text,x,y,color)
oled.text("Hello Wolrd!",0,0,1)
oled.show()
```

# Useful Link & Tools
- [External QRCode Library](https://github.com/JASchilz/uQR)
  - This library is used to generate a QR code matrix and render it to the SSD1306.
- [Image to Matrix Generator](https://jlamch.net/MXChipWelcome/)
  - This link is used to convert images into byte arrays and render them to the SSD1306.
