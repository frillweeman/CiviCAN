# carOS

personal car hacking project for my 2012 Civic

## Stack

- Raspberry Pi w/ Raspbian Buster Lite
- Python3
- can-utils
- systemd (gpio-shutdown.service and vehicle.service)

## Current Features

- automatic Click2Enter activation through TRRS jack in mobile radio

## Planned Features

- police scanner
- ambient lighting in floorboard
- CAN frame logger for every trip
- DBC file creation and parsing
- LPR (license plate recognition)

## Research

- [Automated CAN Reverse Engineering](https://github.com/brent-stone/CAN_Reverse_Engineering)
- [Fast Boot Raspberry Pi](http://himeshp.blogspot.com/2018/08/fast-boot-with-raspberry-pi.html)
- [Python DBC Parsing & CAN Encoding/Decoding](https://pypi.org/project/cantools)
