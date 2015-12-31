# Bushwack

```WELCOME! THIS IS AN EXPERIMENTAL, UNTESTED, IN-PROGRESS PRE-ALPHA PROJECT! THAT BE DRAGONS AHEAD YET LADDY!```

<br/>
## MCR - Mission Concept Review

*What is the need, objectives and concept for meeting said objectives?*

At large outdoor venues, such as Burning Man or ski resorts, it is easy to lose your friends, and difficult to locate them again. Often this is a *good* thing since it leads to serendipidous adventures and a forced relaxation of scheduling stress. Often, though, it's a source of stress and frustration. 

This project aims to build a cheap, self-contained person locator:

- to help you find your friends
- to share points of interest

*Note: in many ways this revisits the ideas that originally went into my iPhone app Burble*

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

<br/>
## SDR - System Design Review

*What is the proposed system architecture and design, and the flow of data through the system?*

Each unit has:

- Sensors:
- - a GPS for positioning
- - a compass for orientation
- User Interface:
- - a small OLED screen for information display
- - a few buttons for interaction
- Power
- - a rechargeable battery (most likely LiPo or Li-Ion)
- - a battery charging circuit
- - a power regulator and battery protection circuit
- Radio
- - long range (ideally 1.5 miles to cover entire Black Rock City diameter)
- - doesn't depend on pairing with another device (support one-to-many broadcast)
- - license-free spectrum
- - ~5kbps data rates
- - reasonable latency (<1s)

#### Suggested System Architecture

**Raspberry Pi Zero as command center.**

[Specs:](http://www.raspberrypi-spy.co.uk/2015/11/introducing-the-raspberry-pi-zero/)

- Price: $5
- Fast: 1Ghz ARM1 Core (Same as Raspberry Pi 1, BCM2836), 512MB Ram, microSD card
- Low Power: 160mA power draw
- Tiny: 65mm x 30mm x 5mm, 9g
- [Good Peripherals](http://elinux.org/RPi_Low-level_peripherals): [SPI Bus](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md), two I2C buses, a Display Serial Interface connector, and HDMI out

**OLED Display with Buttons**

[128x64 yellow and blue](http://www.amazon.com/gp/product/B00O2LLT30?keywords=arduino%20oled&qid=1451557496&ref_=sr_1_1&sr=8-1):

- Price: $15
- SSD1306 SPI controller
- 8 lines of text, 22 characters wide (176 characters total)

<br/>
## Resources:

[Design Review Cycle](https://en.wikipedia.org/wiki/Design_review_(U.S._government)#System_Requirements_Review_.28SRR.29)
