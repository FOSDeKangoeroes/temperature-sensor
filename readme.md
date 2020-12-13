# Hottub temperature monitoring system

## Setting up the temp sensors

- Enable 1-wire interface on the host PI
- For each of the connected sensors, run: 
  `sudo dtoverlay w1-gpio gpiopin=<pin where sensor is connected> pullup=0`

 