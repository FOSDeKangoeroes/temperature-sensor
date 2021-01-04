# Hottub temperature monitoring system

Overkill temperature monitoring system for the DIY hottub. The program measures the temperature from all connected DS18B20 temperature monitors and calculates the mean temperature. This temperature is displayed on an e-paper display. A connected led-strip also gives visual feedback on the temperature of the water inside the hottub. It cycles from blue (too cold), to green (just right), to red (too warm).

## Hardware

- Raspberry Pi
- DS18B20 temperature sensor (at least one), multiple sensors are supported
- SK6813 (or WS8212) LED strip
- AdaFruit 1.54" E-paper display

Refer to the Fritzing diagram for the circuit layout and which pins to use on the Pi.

**This program can only run on a Raspberry Pi**

## Software

### Prerequisites
- Python 3.7
- Pipenv

### Running


```
pipenv install
sudo python temperature_sensor.py
```
**The script needs to run as root for the LED strip to work.**

## VS Code

If you want to use VS Code for development, you can use the SSH extension pack to get everything going.

## Interfacing
Before being able to interface with the hardware, some things need to be set on the Pi:

### Temperature sensor(s)
1-wire interface needs to be enabled on the host PI

Add this to /boot/config.txt :

`dtoverlay=w1-gpio`

If you want to add sensors to multiple pins, add this to /boot/config.txt:

`dtoverlay=w1-gpio,gpiopin=<pin_where_sensor_is_connected>`

 