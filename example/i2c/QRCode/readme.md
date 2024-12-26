# MicroPython QR Code

In order to show a QR code on your OLED display, you can use the following method:

1. Use the external MicroPython QR code library.
2. Convert your QR code image to a byte array.

# Method1 - Use external MicroPython QR Code Library

Since this is an external library, which means you have to install it on your board before using it.
There are 2 ways to install the library (choose one):

1. Manually upload the library file to your board.
   - Go to this repository: https://github.com/JASchilz/uQR.
   - Upload the `uQR.py` to your board.
2. Use Thonny Package Manager.
   - Open Thonny IDE. 
   - At the top menu, click tools and select `Manage Packages`.
   - In the search box, search for `micropython-qr` and install it to your board.

After library installation is complete, you can see the library file in your board.

You can test the code based on the installation method
- If you install with the Thonny IDE package manager, try this file: [01-show_qr.py](https://github.com/PerfecXX/MicroPython-SSD1306/blob/main/example/i2c/QRCode/01-show_qr.py)
- If you manually install, try this file: [02-show_qr.py](https://github.com/PerfecXX/MicroPython-SSD1306/blob/main/example/i2c/QRCode/02-show_qr.py)

# Method2 - Convert your QR code image to a byte array.

1. Prepare the QR code image file (any format, but .png might be a good choice).
2. Resize the image resolution to fit your display.
3. Convert the image file to a byte array using this tool: https://jlamch.net/MXChipWelcome/
   - In the image setting, adjust `brightness / alpha threshold` until you can see the image clearly.
   - In the output, set the code output format to `Adafruit GFXbitmapFont` and then click `Generate`.
   - Copy the generated code (bitmap data only).
4. Create a byte array, then paste the generated code.

```python 

```
