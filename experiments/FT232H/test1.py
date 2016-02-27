# Copyright (C) 2015 Niels Joubert
# Contact: Niels Joubert <njoubert@gmail.com>
#

# Following https://learn.adafruit.com/adafruit-ft232h-breakout/spi

import Adafruit_GPIO.FT232H as FT232H

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()
 
# Find the first FT232H device.
ft232h = FT232H.FT232H()
 
# Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
# Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
spi = FT232H.SPI(ft232h, cs=8, max_speed_hz=3000000, mode=0, bitorder=FT232H.MSBFIRST)
 
# Write three bytes (0x01, 0x02, 0x03) out using the SPI protocol.
spi.write([0x01, 0x02, 0x03])

# Read 3 bytes of data using the SPI protocol.
response = spi.read(3)
print 'Received {0}'.format(response)
 
# Write 3 bytes and simultaneously read 3 bytes using the SPI protocl.
response = spi.transfer([0x01, 0x02, 0x03])
print 'Received {0}'.format(response)