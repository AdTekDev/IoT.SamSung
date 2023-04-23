# IoT.SamSung

## LIBs
- https://gpiozero.readthedocs.io/en/stable/   
- https://github.com/WiringPi/WiringPi  
- http://wiringpi.com/  
- https://abyz.me.uk/rpi/pigpio/  

Các thư viện khác:
- https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/ 
...


# C / GCC

   wget https://raw.githubusercontent.com/AdTekDev/IoT.SamSung/main/B01/timsolonnhat.c
   
   gcc timsolonnhat.c -o timso
   
   ./timso


# Python 

wget   https://raw.githubusercontent.com/AdTekDev/IoT.SamSung/main/B01/timsolonnhat.py

python  timsolonnhat.py 


# Install


## Wiringpi  
(http://wiringpi.com/download-and-install/)   
sudo apt-get install wiringpi  

Hoặc 
git clone https://github.com/WiringPi/WiringPi   
cd WiringPi   
./build   


# install python 


sudo apt install python3-gpiozero  
sudo apt install python-gpiozero  


hay

sudo pip3 install gpiozero  
sudo pip install gpiozero  


# Check GPIO 
>>> import gpiozero
>>> 
>>> led = gpiozero.LED(17)
>>> 
>>> led.on()
>>> 

# B03 

LED - LED board 
https://gpiozero.readthedocs.io/en/stable/recipes.html#led 

