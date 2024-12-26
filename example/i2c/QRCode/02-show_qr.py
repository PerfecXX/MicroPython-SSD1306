# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

"""
This library must be install first!
https://github.com/JASchilz/uQR
"""
from uQR import QRCode

# Pin Setup
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Generate QR Code Matrix
qr = QRCode()
qr.add_data('https://github.com/PerfecXX')
matrix = qr.get_matrix()

# QR Scale and offset
scale_factor = 2.1
x_pos_offset = 8
y_pos_offset = 8

# Show Some Text
oled.text("Scan",80,25)
oled.text("me",87,35)

# Show QR Code with Generate Matrix
for y in range(len(matrix)*scale_factor):     
    for x in range(len(matrix[0])*scale_factor):
        # Invert the QRCode Color
        value = not matrix[int(y/scale_factor)][int(x/scale_factor)]   
        oled.pixel(x-x_pos_offset, y-y_pos_offset, value)                
oled.show()    
