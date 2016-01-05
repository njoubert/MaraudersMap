# Marauder's Map

```WELCOME! THIS IS AN EXPERIMENTAL, UNTESTED, IN-PROGRESS PRE-ALPHA PROJECT! THAT BE DRAGONS AHEAD YET LADDY!```

<br/>
## MCR - Mission Concept Review

*What is the need, objectives and concept for meeting said objectives?*

At large outdoor venues, such as Burning Man or ski resorts, it is easy to lose your friends, and difficult to locate them again. Often this is a *good* thing since it leads to serendipidous adventures and a forced relaxation of scheduling stress. Often, though, it's a source of stress and frustration. 

This project aims to make it possible to find your friends, while staying true to the principles of immediacy, serendipitously meeting people, and going on adventures together! 

This project consists of a cheap, self-contained person locator to help you find your friends and share points of interest. But it doesn't make it too easy!

- Everyone only gets a very limited set of points they can save - so everyone has their own Top 5 places!
- We only provide an approximate distance and direction to a friend, so it's an adventure to try and find them!
- The system might sometimes lie to you, who knows?

*Note: in many ways this revisits the ideas that originally went into my iPhone app [Burble](https://github.com/njoubert/UndergraduateProjects/tree/master/Burble/trunk)*

**Other Ideas**

- This project can include a visual component - by animating EL wire or the like as you get closer to a friend!
- **Lying?** - What if the system only gives you a true value part of the time? What if it deliberately lies?
- **Only works part of the time?** - What if you can't always use the system, you have to wait for it to become active?

<br/>
## SRR - System Requirements Review

*What is the functional and performance requirements for the system?*

Bushwack needs to be:

- A completely homogenous, decentralized position reporting system.
- A mesh network where the typical communication scheme is NOT all-to-all, but might be.
- Stand-alone, with no dependency on wifi or cell signals.
- A small, cheap (ideally <$50) handheld device.
- Weather-resistant in dusty and extreme temperature environments.
- Resilient to power-cycling
- Support 20 to 50 people.
- Be as passive as possible: don't interfere with people's burn, it's not a cellphone.

<br/>
## SDR - System Design Review

*What is the proposed system architecture and design, and the flow of data through the system?*

Each unit has:

- Sensors:
  - a GPS for positioning
  - a compass for orientation
- User Interface:
  - a small OLED screen for information display
  - a few buttons for interaction
- Power
  - a rechargeable battery (most likely LiPo or Li-Ion)
  - a battery charging circuit
  - a power regulator and battery protection circuit
- Radio
  - long range (ideally 1.5 miles to cover entire Black Rock City diameter)
  - doesn't depend on pairing with another device (support one-to-many broadcast)
  - license-free spectrum
  - ~5kbps data rates
  - reasonable latency (<1s)

#### Suggested System Architecture

**Raspberry Pi Zero as command center.**

[Specs:](http://www.raspberrypi-spy.co.uk/2015/11/introducing-the-raspberry-pi-zero/)

- Price: $5
- Fast: 1Ghz ARM1 Core (Same as Raspberry Pi 1, BCM2836), 512MB Ram, microSD card
- Low Power: 160mA power draw
- Tiny: 65mm x 30mm x 5mm, 9g
- [Good Peripherals](http://elinux.org/RPi_Low-level_peripherals): [SPI Bus](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md), two I2C buses, a Display Serial Interface connector, and HDMI out

**Displays**

[OLED: 128x64 yellow and blue 0.96"](http://www.amazon.com/gp/product/B00O2LLT30?keywords=arduino%20oled&qid=1451557496&ref_=sr_1_1&sr=8-1):

- Price: $15
- SSD1306 SPI controller
- 8 lines of text, 22 characters wide (176 characters total)

[TFT: 160x128 full-color 1.8"](https://www.adafruit.com/products/358)

- Price: $20
- SPI

[LCD: Monochrome Nokia Display 84x48](https://www.adafruit.com/products/338)

- Price: $10
**CC1101 Radio Modem**

**GPS Module**

[NavSpark-GL GPS/GLONASS Dev Board](https://navspark.mybigcommerce.com/navspark-gl-arduino-compatible-development-board-with-gps-glonass/)

- Price: $25 + $9 antenna = $34
- Arduino-compatible, hackable
- Very sensitive, GPS, GLONASS, SBAS, QZSS for amazing coverage, Venus 8 167 channel engine, 10Hz update, 2.5m CEP accuracy 
- 38mm x 18mm
- Serial and Serial-Over-USB IO

[AdaFruit Ultimate GPS Module](https://www.adafruit.com/products/746)

- Price: $40
- 15mm x 15mm x 4mm with patch antenna
- Built-in datalogging to flash memory
- Serial out
 
[UBlox Neo6 GPS Module on eBay](http://www.ebay.com/itm/Ublox-NEO-6M-GPS-Module-Aircraft-Flight-Controller-For-Arduino-MWC-IMU-APM2-/200911914297?hash=item2ec7488539:g:s7IAAOSwYHxWFgLf)

[uBlox Neo6M with Compass on eBay](http://www.ebay.com/itm/Ublox-neo-6M-GPS-Module-W-box-Built-in-Compass-for-PIX-Pixhawk-PX4-Autopilo-New-/281835342531?hash=item419eb20ac3:g:czYAAOSw~gRV0tSn)

- Price: $11 to $17
- 9600 baud serial out


**Battery Power**


<br/>
## Resources and Inspiration

**System Design Inspiration:**

[Wolfgang Klerk's Arduino and Raspberry Pi Projects](https://wolfgangklenk.wordpress.com/) and his [SPI protocol driver for TI CC11001](https://github.com/wklenk/CC1101SocketDriver)


**Product Design Inspiration:**

[Teenage Engineering's PO-16 synth](https://www.teenageengineering.com/products/po)

**Other Resources:**

[Design Review Cycle](https://en.wikipedia.org/wiki/Design_review_(U.S._government)#System_Requirements_Review_.28SRR.29)


<br/>
## Discarded System Designs (Dead Kittens)

**APRS-based system**

APRS radios are to expensive, too clunky, power hungry, and way too slow (<1kbps). Building my own from scratch is painful. APRS is also a notoriously inefficient use of spectrum: we should be able to push significantly higher throughput at the same power and range without using more spectrum.
