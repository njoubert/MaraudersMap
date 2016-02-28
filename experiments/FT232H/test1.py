# Copyright (C) 2015 Niels Joubert
# Contact: Niels Joubert <njoubert@gmail.com>
#

# Following https://learn.adafruit.com/adafruit-ft232h-breakout/spi



import Adafruit_GPIO.FT232H as FT232H
from LoRa import *

import logging, sys, time


class SX1276(object):
  '''
  Class to manage SX1276 radio
  '''
  def __init__(self, spi):
    self._log = logging.getLogger('MaraudersMap.SX1276')
    self._spi = spi
    self._log.debug("SX1276 Created")



def log_to_stdout(level=1):
  h1 = logging.StreamHandler(sys.stdout)
  log = logging.getLogger('MaraudersMap.SX1276')
  log.addHandler(h1)
  log.setLevel(level)

def main():
  log_to_stdout()

  FT232H.use_FT232H()
  ft232h = FT232H.FT232H()
   
  # Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
  # Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
  spi = FT232H.SPI(ft232h, cs=8, max_speed_hz=3000000, mode=0, bitorder=FT232H.MSBFIRST)


  radio = LoRa(spi=spi)
  radio.set_freq(915)

  print(radio)

  ''' LET'S TRY TO READ THE TEMPERATURE SENSOR!! Only available in FSK/OOK Mode? '''
  # Here's the sequence (P89 from http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf)

  radio.rx_chain_calibration()

  # 1) Set device to Standby, wait for oscillator startup
  radio.set_mode(MODE.SLEEP)

  # 2) Set the device to FSRx mode (or should this be standby??)
  radio.set_mode(MODE.FSRX)

  # 3) set TempMonitorOff=0
  # set register IMAGE_CAL lowest bit to 0
  image_cal = (radio.get_register(REG.FSK.IMAGE_CAL))
  image_cal = image_cal & 0xFE
  radio.set_register(REG.FSK.IMAGE_CAL, image_cal)

  # 4) Wait for 140 microseconds
  time.sleep(0.1)

  # 5) Set TempMonitorOff=1
  image_cal = (radio.get_register(REG.FSK.IMAGE_CAL)) | 0x01
  print image_cal
  radio.set_register(REG.FSK.IMAGE_CAL, image_cal)

  # 6) Set device back to Sleep mode
  radio.set_mode(MODE.SLEEP)  
  
  # 7) Access temperature value in RegTemp (0x3C)
  val = radio.get_register(0x3C)
  print val 

if __name__ == "__main__":
  main()




# # Write three bytes (0x01, 0x02, 0x03) out using the SPI protocol.
# spi.write([0x01, 0x02, 0x03])

# # Read 3 bytes of data using the SPI protocol.
# response = spi.read(3)
# print 'Received {0}'.format(response)
 
# # Write 3 bytes and simultaneously read 3 bytes using the SPI protocl.
# response = spi.transfer([0x01, 0x02, 0x03])
# print 'Received {0}'.format(response)
