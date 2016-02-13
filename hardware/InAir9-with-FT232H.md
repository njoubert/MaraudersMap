# Prototyping the InAir9 module with FT232H

[Sparkfun SPI Tutorial incl "What's wrong with Serial UART"](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

Easy to wire up. all MOSI and all MISO connects to each other. No TX goes to RX like in serial.

|FTDI|InAir9|
|====|======|
|D0  |CK    |
|D1  |MOSI  |
|D2  |MISO  |
|C0  |CS    |
|Gnd |0V    |


Connect a random GPIO pin on FTDI to the Chip Select.
