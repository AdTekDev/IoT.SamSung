# IoT.SamSung

## LIBs
- https://gpiozero.readthedocs.io/en/stable/installing.html     
- https://github.com/WiringPi/WiringPi  
- http://wiringpi.com/  
- https://abyz.me.uk/rpi/pigpio/  

Các thư viện khác:
- https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/ 
- https://www.ics.com/blog/gpio-programming-exploring-libgpiod-library  
...

## Tham khảo
- https://www.raspberrypi.com/documentation/computers/os.html#gpio-in-python  
- https://gpiozero.readthedocs.io/en/stable/   

# Chạy thử

## C / GCC

   wget https://raw.githubusercontent.com/AdTekDev/IoT.SamSung/main/B01/timsolonnhat.c
   
   gcc timsolonnhat.c -o timso
   
   ./timso


## Python 

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


## install python 


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

# Bài tập

## B03 

LED - LED board 
https://gpiozero.readthedocs.io/en/stable/recipes.html#led 

