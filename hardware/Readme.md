# Marauder's Map Hardware

## Radio

### HopeRF 

```Units on this is in mm```

![HopeRF PCB](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/HopeRF-RFM95W-pcb.png)

![HopeRF CAD](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/HopeRF-RFM95W-cad.png)


## GPS and Compass

**GPS UART:**

| Pin | Signal   | Volt  | 
|=====|========  |=======|
| 1   | VCC      | +5V   |
| 2   | RX (IN)  | +3.3V |
| 3   | TX (OUT) | +3.3V |
| 4   | RST (OUT)| +3.3V |
| 5   | CTS (IN) | +3.3V |
| 6   | GND      | -     |


``` Check that I got the RX/TX order right! ~~~

**Compass I2C:**

| Pin | Signal | Volt  |
|=====|========|=======|
| 1   | VCC    | +5V   |
| 2   | SCL    | +3.3V |
| 3   | SDA    | +3.3V |
| 4   | GND    | -     |




## Raspberry Pi

### GPIO Pinout

![RaspbPi GPIO](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/Raspberry-Pi-GPIO-Layout-Model-B-Plus-small.png)

## Useful Resources 

- [Niels' Raspberry Pi Christmas Adventure](https://github.com/njoubert/RaspberryPiChristmasCodingAdventure)
