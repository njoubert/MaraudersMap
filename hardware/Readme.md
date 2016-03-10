# Marauder's Map Hardware

Some Advice on Circuit Design:

- Lay out a board with everything, and connectors, even if you don't populate it. Build it so that you don't have to have everything populated for it to work, and you can bypass any onboard circuit by plugging into connectors.
- Work from reference designs, and copy other people's boards.

## Useful Resources 

- [Niels' Raspberry Pi Christmas Adventure](https://github.com/njoubert/RaspberryPiChristmasCodingAdventure)

**Reference Designs**

- https://www.olimex.com/
- [STM32 Nucleo and Discover boards](http://www.st.com/web/en/catalog/mmc/FM141/SC1169?sc=stm32)

## Sourcing

**Components**

- [OctoPart](https://octopart.com/)
- [Digikey]()
- [Mouser]()
- [Jameco (local pickup in bay area)]()
 

**PCBs**

- [SEEED Studio](https://www.seeedstudio.com/service/index.php?r=pcb)
 

## Radio

### Different SX127x offerings:

Supported modulation: LORA, FSK, OOK

| Model | Freq        | Bandwidth (Khz)  | Spreading Factor | Eff. Bitrate (kbps) | Sensitivity (dBm) | Power Out (dBm) |
|-------|-------------|------------------|------------------|---------------------|-------------------|-----------------|
|SX1272 | 860-1020Mhz | 125, 250, 500    | 6-12             | 0.24 - 37.5         |-117 to -137       | +14 RFO, +20 PA |
|SX1273 | 860-1020Mhz | 125, 250, 500    | 6-9              | 1.7 - 37.5          |-117 to -130       | +14 RFO, +20 PA |
|SX1276 | 137-1020Mhz | 7.8 - 500        | 6-12             | 0.18 - 37.5         |-111 to -148       | +14 RFO, +20 PA |
|SX1277 | 137-1020Mhz | 7.8 - 500        | 6-9              | 0.11 - 37.5         |-111 to -139       | +14 RFO, +20 PA |
|SX1278 | 137-525Mhz  | 7.8 - 500        | 6-12             | 0.18 - 37.5         |-111 to -148       | +14 RFO, +20 PA |
|SX1279 | 137-960Mhz  | 7.8 - 500        | 6-12             | 0.18 - 37.5         |-111 to -148       | +14 RFO, +20 PA |

Sensitivity vs Throughput

![Sensitivity vs Throughput]()

### Si443x comparison (3DR Radio module)

Supported modulation: GFSK, FSK, OOK

| Model | Freq        | Bandwidth (Khz)  | Spreading Factor | Eff. Bitrate (kbps) | Sensitivity (dBm) | Power Out (dBm) |
|-------|-------------|------------------|------------------|---------------------|-------------------|-----------------|
| Si4430| 900-960Mhz  | +-0.615 - +-320  |                NA| 0.123-256kbps       | -102 to -121      | +13 |
| Si4431| 240-930Mhz  | +-0.615 - +-320  |                NA| 0.123-256kbps       | -102 to -121      | +13 |
| Si4432| 240-930Mhz  | +-0.615 - +-320  |                NA| 0.123-256kbps       | -102 to -121      | +20 |

| Sensitivity | Throughput | Bandwidth |
|-------------|------------|-----------|
| -121        | 2kbps      | +- 5Khz   |
| -108        | 40kbps     | +- 20Khz  |
| -104        | 100kbps    | +- 50Khz  |
| -101        | 125kbps    | +- 62.5Khz|


### HopeRF 

```Units on this is in mm```

![HopeRF PCB](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/HopeRF-RFM95W-pcb.png)

![HopeRF CAD](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/HopeRF-RFM95W-cad.png)


## GPS and Compass

**GPS UART:**

| Pin | Signal   | Volt  | 
|-----|--------  |-------|
| 1   | VCC      | +5V   |
| 2   | RX (IN)  | +3.3V |
| 3   | TX (OUT) | +3.3V |
| 4   | RST (OUT)| +3.3V |
| 5   | CTS (IN) | +3.3V |
| 6   | GND      | GND   |


``` Check that I got the RX/TX order right! ```

**Compass I2C:**

| Pin | Signal | Volt  |
|-----|--------|-------|
| 1   | VCC    | +5V   |
| 2   | SCL    | +3.3V |
| 3   | SDA    | +3.3V |
| 4   | GND    | GND   |

[Details here.](https://pixhawk.org/modules/pixhawk)

Connectors are Hirose DF13 6pos ([Digi-Key Link: DF13A-6P-1.25H(20)](https://www.digikey.com/product-search/en?WT.z_header=search_go&lang=en&site=us&keywords=DF13A-6P-1.25H(20)&x=0&y=0)) or 4pos. ([Digi-Key Link: DF13A-4P-1.25H(20)](https://www.digikey.com/product-search/en?WT.z_header=search_go&lang=en&site=us&keywords=DF13A-4P-1.25H(20)&x=0&y=0))




## Raspberry Pi

### GPIO Pinout

![RaspbPi GPIO](https://raw.githubusercontent.com/njoubert/MaraudersMap/master/hardware/images/Raspberry-Pi-GPIO-Layout-Model-B-Plus-small.png)


