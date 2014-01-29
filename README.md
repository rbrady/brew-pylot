brew-pylot
==========

Software that runs on the Raspberry Pi using 1 wire temperature sensors and solid state relays to automate selected parts of the homebrewing process.

###Equipment / Materials / Parts
- Raspberry Pi (http://www.raspberrypi.org/)
- DS18b20 Waterproof Temperature Sensors [source](http://www.amazon.com/gp/product/B00CC7TGKO/ref=oh_details_o02_s00_i04?ie=UTF8&psc=1)
- Pi Cobbler Breakout Board [source](http://www.amazon.com/gp/product/B00EBXP3R2/ref=oh_details_o02_s00_i00?ie=UTF8&psc=1)
- Wireless USB Adapter [source] (http://www.amazon.com/gp/product/B003MTTJOY/ref=oh_details_o02_s00_i03?ie=UTF8&psc=1)
- 2 Ch 5V SSR [source] (http://www.amazon.com/gp/product/B00E0NTPP4/ref=oh_details_o02_s00_i05?ie=UTF8&psc=1)
- 4.7k Ohm resistor
- *Still evaluating the SSR solution for running the 240v 5500w heating element in the boil kettle

###Setup
- You first have to run the following commands to load the kernel modules


    sudo modprobe w1_gpio && sudo modprobe w1_therm
    sudo sh -c "echo 'w1_gpio\nw1_therm\n' >> /etc/modules"

- Connect thermo sensors to GPIO pin, power and ground.
- Add 4.7k ohm resistor between power and GPIO pin
- Check the directory at /sys/bus/w1/devices/
- Read files in each $DIR named w1_slave

Files look like:

    0b 00 4b 46 7f ff 05 10 95 : crc=95 YES
    0b 00 4b 46 7f ff 05 10 95 t=22564
