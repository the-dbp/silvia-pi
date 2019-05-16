# silvia-pi
A Raspberry Pi modification to the Rancilio Silvia Espresso Machine implementing PID temperature control, and automated brewing cycles.

#### Currently Implemented Features:
* Brew temperature control
* RESTful API
* Web interface for displaying temperature and other statistics
* Programmable machine warm-up/wake-up

#### Planned Features:
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
  * $0.47 also take a 1 channel if you want to start and stop steam https://www.aliexpress.com/item/DC5V-1-2-4-8-Channel-Relay-Module-with-Optocoupler-Relay-Output-1-2-4-8/32888878613.html
* Solid State Relay - For switching on and off the heating element
  * $3.4 - https://www.aliexpress.com/item/1pcs-SSR-40DA-40A-Solid-State-Relay-Module-3-32V-DC-Input-24-380VAC/32681597174.html?spm=a2g0s.9042311.0.0.27424c4d5PrdXp
* Thermocouple Amplifier - For interfacing between the Raspberry Pi and Thermocouple temperature probe
  * $2.35 - https://www.aliexpress.com/item/MAX31855K-Thermocouple-Sensor-Temperature-Detection-Module-Development-Board-Hot-sale/32805699868.html?spm=a2g0s.9042311.0.0.27424c4doR8tzF
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
````
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install rpi-update git build-essential python-dev python-smbus python-pip
sudo rpi-update
sudo bash -c 'echo "dtparam=spi=on" >> /boot/config.txt'
sudo reboot
````

After the reboot:
````
sudo git clone https://github.com/the-dbp/silvia-pi.git /root/silvia-pi
sudo /root/silvia-pi/setup.sh
````
This last step will download the necessariy python libraries and install the silvia-pi software in /root/silvia-pi

It also creates an entry in /etc/rc.local to start the software on every boot.

#### API Documentation

##### GET /allstats
Returns JSON of all the following statistics:
* i : Current loop iterator value (increases 10x per second)
* tempf : Temperature in °F
* avgtemp : Average temperature over the last 10 cycles (1 second) in °F
* settemp : Current set (goal) temperature in °F
* iscold : True if the temp was <120°F in the last 15 minutes
* hestat : 0 if heating element is currently off, 1 if heating element is currently on
* pidval : PID output from the last cycle
* avgpid : Average PID output over the last 10 cycles (1 second)
* pterm : PID P Term value (Proportional error)
* iterm : PID I Term value (Integral error)
* dterm : PID D Term value (Derivative error)
* snooze : Current or last snooze time, a string in the format HH:MM (24 hour)
* snoozeon : true if machine is currently snoozing, false if machine is not snoozing

##### GET /curtemp
Returns string of the current temperature in °F

##### GET /settemp
Returns string of the current set (goal) temperature in °F

##### POST /settemp
Expects one input 'settemp' with a value between 200-260.  
Sets the set (goal) temperature in °F
Returns the set temp back or a 400 error if unsuccessful.

##### GET /snooze
Returns string of the current or last snooze time formatted "HH:MM" (24 hour).  
e.g. 13:00 if snoozing until 1:00 PM local time.

##### POST /snooze
Expects one input 'snooze', a string in the format "HH:MM" (24 hour).  
This enables the snooze function, the machine will sleep until the time specified.  
Returns the snooze time set or 400 if passed an invalid input.

##### POST /resetsnooze
Disables/cancels the current snooze functionality.  
Returns true always.

##### GET /restart
Issues a reboot command to the Raspberry Pi.

##### GET /healthcheck
A simple healthcheck to see if the webserver thread is repsonding.  
Returns string 'OK'.
