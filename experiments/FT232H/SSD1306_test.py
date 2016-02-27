# Copyright (C) 2015 Niels Joubert
# Contact: Niels Joubert <njoubert@gmail.com>
#

# Following https://learn.adafruit.com/adafruit-ft232h-breakout/spi
# and https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries/spi-devices
# and https://learn.adafruit.com/monochrome-oled-breakouts
# and http://www.seeedstudio.com/document/pdf/RPI-OLED-Datesheet.pdf


# WIRING:
# 52pi Module to FT232H Breakout Board:
#
# GND (6) -> GND
# 5V  (2) ->  5V
# MOSI(19) -> D1
# MISO(21) -> D2
# CLK (23) -> D3
# DC  (18) -> C2 (GPIO 10)
# RST (22) -> C1 (GPIO 9)
# CS  (24) -> C0 (GPIO 8)

import Adafruit_GPIO.FT232H as FT232H
import SSD1306

import logging, sys, time
h1 = logging.StreamHandler(sys.stdout)
log = logging.getLogger('Adafruit_SSD1306.SSD1306Base')
log.addHandler(h1)
log.setLevel(1)

log.info('HERE WE GOOOO')

# Ensure that PIL is installed
import Image
import ImageDraw
import ImageFont

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()
 
# Find the first FT232H device.
ft232h = FT232H.FT232H()
 
# Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
# Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
spi = FT232H.SPI(ft232h, cs=8)

# Initialize display
disp = SSD1306.SSD1306_128_32(9, 10, spi=spi, gpio=ft232h)

# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# draw.rectangle((24,2,44,22), outline=0, fill=255)
# draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
# draw.line((68,22,81,2), fill=255)
# draw.line((68,2,81,22), fill=255)

# font = ImageFont.load_default()
# draw.text((5,20), y, font=font, fill=255)

yoff = 10
xoff = 0
xmax = 100
ymax = 28
right = True
down = True
try:
  while True:


    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    if xoff > xmax:
      right = False
    elif xoff < 0:
      right = True
    if yoff > ymax:
      down = False
    elif yoff < 0:
      down = True

    if right:
      xoff += 1
    else:
      xoff -= 1 
    if down:
      yoff += 1
    else:
      yoff -= 1 

    draw.ellipse((xoff,yoff,xoff+16,yoff+8), outline=0, fill=255)

    disp.image(image)
    disp.display()
    #time.sleep(0.1)
except KeyboardInterrupt:
  pass