MicroPython SSD1306
===================

|Version| |License|

MicroPython Library for SSD1306 OLED Displays with some simple shape
drawing functions.

https://github.com/PerfecXX/MicroPython-SSD1306

Example Usage
=============

-  `Screen
   Control <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/screen%20control>`__
-  `Text <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/text>`__
-  `Shape <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/shape>`__
-  `Image <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/image>`__
-  `QRCode <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example/i2c/QRCode>`__
-  `More
   Example <https://github.com/PerfecXX/MicroPython-SSD1306/tree/main/example>`__

Quick Example
=============

.. code:: python

   # Import Library
   from machine import Pin,SoftI2C
   from ssd1306 import SSD1306_I2C
   from time import sleep,sleep_us

   # Pin Setup
   screen_width = 128
   screen_height = 64
   i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
   oled = SSD1306_I2C(screen_width, screen_height, i2c)

   #---Turn on the oled---
   oled.poweron()
   oled.contrast(0)

   #---Show Text---
   oled.text("...Test Begin...",0,0)
   oled.text("Contrast LV",20,20)
   oled.show()
   sleep(1)

   #---Show Contrast Level---
   for contrast_level in range(0,256,1):
       oled.contrast(contrast_level)
       oled.text("LV:{}".format(contrast_level),50,40,1)
       oled.show()
       oled.text("LV:{}".format(contrast_level),50,40,0)
       sleep_us(1)
   sleep(1)

   #---Fill Screen (clear screen)---
   oled.fill(0)
   oled.show()
   sleep(1)

   #---Invert Screen---
   oled.text("Color Inverted!",0,5)
   oled.invert(1)
   oled.show()
   sleep(1)

   # Scroll Text (Right->Left)
   for x in range(0,128):
       oled.fill(0)
       oled.text("Scroll Text", 128 - x, 10)
       oled.show()
       sleep(0.01)

   # Scroll Text (Left->Right)
   for x in range(0,128):
       oled.fill(0)
       oled.text("Scroll Text",x, 10)
       oled.show()
       sleep(0.01)

   #---Draw line---
   oled.fill(0)
   oled.text("Line",50,10)
   oled.hline(0,30,100,1) # Horizontal Line
   oled.vline(64,25,60,1) # Vertival Line
   oled.show()
   sleep(1)


   #---Draw a Triangle---
   oled.fill(0)
   oled.text("Triangle",25,5)
   oled.triangle(30, 20, 60, 60, 90, 20, color=1, fill=False) # Outline
   oled.show()
   sleep(1)
   oled.triangle(30, 20, 60, 60, 90, 20, color=1, fill=True) #Filled
   oled.show()
   sleep(1)

   #---Draw a Rectangle---
   oled.fill(0)
   oled.text("Rectangle",25,5)
   oled.rect(3,15,20,20,1,0) # Outline
   oled.show()
   oled.rect(3,40,20,20,1,1) # Filled
   oled.show()
   sleep(1)

   #---Draw a Round Rectangle---
   oled.fill(0)
   oled.text("Round Rectangle",5,5)
   oled.round_rect(10, 20, 60, 40, 1, filled=False , radius=10) # Outline
   oled.show()
   sleep(1)

Useful Link & Tools
===================

-  `External QRCode Library <https://github.com/JASchilz/uQR>`__

   -  This library is used to generate a QR code matrix and render it to
      the SSD1306.

-  `Image to Matrix Generator <https://jlamch.net/MXChipWelcome/>`__

   -  This link is used to convert images into byte arrays and render
      them to the SSD1306.

.. |Version| image:: https://img.shields.io/badge/version-1.0.2-green.svg
   :target: https://github.com/PerfecXX/MicroPython-SSD1306
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
