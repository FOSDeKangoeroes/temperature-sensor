# Hottub temperature monitoring system

## Environment setup

You need a Raspberry PI to run this code.

Use pipenv to setup a virtual environment. To install dependencies, run pipenv install.

## VS Code

If you want to use VS Code for development, you can use the SSH extension pack to get everything going.

## Setting up the temp sensors

Enable 1-wire interface on the host PI
Add this to /boot/config.txt for each sensor:

`dtoverlay=w1-gpio,gpiopin=<pin_where_sensor_is_connected>`

 