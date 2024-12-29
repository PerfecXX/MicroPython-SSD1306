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

#---Draw Shape with Polygon---
oled.fill(0)
oled.text("Poly:Triangle",5,5)
points = [(20, 40), (60, 10), (100, 40)] # 3 Point Triangle
oled.polygon(points,color=1,fill=False)
oled.show()
sleep(1)

oled.fill(0)
oled.text("Poly:Square",5,5)
points = [(30, 30), (30, 50), (50, 50), (50, 30)] # 4 Point Square
oled.polygon(points,color=1,fill=False)
oled.show()
sleep(1)

oled.fill(0)
oled.text("Poly:Rectangle",5,5)
points = [(20, 20), (20, 50), (100, 50), (100, 20)] # 4 Point Rectangle
oled.polygon(points,color=1,fill=False)
oled.show()
sleep(1)

oled.fill(0)
oled.text("Poly:Pentagon",5,5)
points = [(40, 30), (60, 20), (80, 30), (70, 50), (50, 50)] # 5 Point Pentagon
oled.polygon(points,color=1,fill=False)
oled.show()
sleep(1)

oled.fill(0)
oled.text("Poly:Octagon",5,5)
points = [(40, 20), (60, 20), (70, 30), (70, 50), (60, 60), (40, 60), (30, 50), (30, 30)] # 8 Point Octagon
oled.polygon(points,color=1,fill=False)
oled.show()
sleep(1)

# ---Draw Circle---
oled.fill(0)
oled.text("Circle",35,5)
oled.circle(60,30,10,1,0) # Outline
oled.show()
sleep(1)
oled.circle(60,30,10,1,1) # Filled
oled.show()
sleep(1)

#---Draw Ellipse---
oled.fill(0)
oled.text("Ellipse",35,5)
oled.ellipse(64, 32, 30, 10, 1,fill=False) # Outline
oled.show()
sleep(1)
oled.ellipse(64, 32, 30, 10, 1,fill=True) # Filled
oled.show()
sleep(1)

#---Draw Arc---
oled.fill(0)
oled.text("Arc",50,5)
oled.arc(64, 32, 20, 0, 180, 1)
oled.show()
sleep(1)

#---Show Text---
oled.fill(0)
oled.text("Test Complete!",0,0)
oled.show()
sleep(5)
oled.poweroff()
