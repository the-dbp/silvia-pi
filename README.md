#this fork is a wip
# silvia-pi
A Raspberry Pi modification to the Rancilio Silvia Espresso Machine implementing PID temperature control, and automated brewing cycles.
#### Planned Features:
* Web interface for displaying temperature and other statistics
* Brew temperature control
* Programmable machine warm-up/wake-up
* remote control of brew and steam switch
* automated start and warmup
* shot prep for next day
* automated maintenance
* external enclosure
* celcius instead of fahrenheit
* new webinterface served via flask

#### Dashboard
<img src="https://github.com/brycesub/silvia-pi/blob/master/media/silvia_dashboard.gif" width=800 />

#### Hardware
* Raspberry Pi zero w
  * $17.74 - https://www.aliexpress.com/item/2017-Raspberry-Pi-Zero-W-Board-1GHz-CPU-512MB-RAM-with-WIFI-Bluetooth-RPI-0-W

* Power Adapter
  * Any Micro USB 5v / 2A supply will do, the longer the cable the better
  * $2.88 https://www.aliexpress.com/item/AC-110V-220V-TO-DC-5V-12V-24V-1A-2A-3A-5A-10A-15A-20A-30A/32836806697.html
* Micro SD Card
  * 4GB minimum, 8GB Class 10 recommended
  * $4.75 - https://www.aliexpress.com/item/SAMSUNG-32G-64G-128G-Memory-Card-Micro-SD-SDHC-SDXC-TF80M-Grade-EVO-Class-10-Micro/32610125064.html
* 4 channel 5v relay module
  * $ 4.10 https://www.aliexpress.com/item/DC5V-1-2-4-8-Channel-Relay-Module-with-Optocoupler-Relay-Output-1-2-4-8/32888878613.html
* Solid State Relay - For switching on and off the heating element
  * $3.4 - https://www.aliexpress.com/item/1pcs-SSR-40DA-40A-Solid-State-Relay-Module-3-32V-DC-Input-24-380VAC/32681597174.html?spm=a2g0s.9042311.0.0.27424c4d5PrdXp
* Thermocouple Amplifier - For interfacing between the Raspberry Pi and Thermocouple temperature probe
  * ~~$2.35 - https://www.aliexpress.com/item/MAX31855K-Thermocouple-Sensor-Temperature-Detection-Module-Development-Board-Hot-sale/32805699868.html?spm=a2g0s.9042311.0.0.27424c4doR8tzF~~ this one is not good, buying and testing a different one
* Type K Thermocouple - For accurate temperature measurement
  * $0.85 - https://www.aliexpress.com/item/Ring-type-Probe-Thermocouple-K-Temperature-Sensor-2M-Cable-for-Industrial-Temperature-Controller/32749486833.html
* female to female dupont line for connecting everything- 
  * $0.65 - https://www.aliexpress.com/item/40PIN-Dupont-Line-10CM-20CM-30CM-Male-to-Male-Female-to-Male-and-Female-to-Female/32960712876.html
* cable sleeve 8mm diameter
  * $4.28 https://www.aliexpress.com/item/32875399483.html
*  .75mm^2 wire - For connecting the A/C side of the relay to the circuit, rubber grommet and splicing connector, 3-conductor
  * $5 - Hardware Store / Scrap
    * Don't skimp here.  Remember this wire will be in close proximit to a ~240*F boiler

#### Hardware Installation
[Installation Instructions / Pictures](http://imgur.com/a/3WLVt)
(my own version comming soon^tm)

#### Circuit Diagram
High-level circuit diagram:

![Circuit Diagram](media/circuit-drawing-silvia.png?raw=true "Circuit Diagram")

#### Software
* OS - Raspbian https://www.raspberrypi.org/downloads/raspbian/

Install Raspbian and configure Wi-Fi and timezone.



#### silvia-pi Software Installation Instructions, will be updated
Execute on the pi bash shell:
```
sudo apt-get -y update
sudo apt-get -y install git build-essential python-dev python-smbus python-pip
sudo bash -c 'echo "dtparam=spi=on" >> /boot/config.txt' 
sudo reboot
```

After the reboot:
```
sudo git clone https://github.com/the-dbp/silvia-pi.git
cd silvia-pi
sudo setup.sh
```
This last step will make the virtual environment and download the necessariy python libraries and install the silvia-pi software in /root/silvia-pi~~
