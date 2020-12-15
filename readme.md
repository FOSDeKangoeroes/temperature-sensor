# Hottub temperature monitoring system

## Environment setup

You need a Raspberry PI to run this code.

Use venv to setup a virtual environment for easy development

## VS Code

If you want to use VS Code for development, you can use the SSH extension pack to get everything going.

## Setting up the temp sensors

- Enable 1-wire interface on the host PI
- For each of the connected sensors, run: 
  `sudo dtoverlay w1-gpio gpiopin=<pin where sensor is connected> pullup=0`

 