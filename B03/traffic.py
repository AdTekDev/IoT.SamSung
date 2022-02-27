from gpiozero import LEDBoard
from time import sleep
from signal import pause
#######################3
# Doc file cau hinh o day

xTime = 5
vTime = 3
dTime = 8

#######################3
leds = LEDBoard(12, 16, 18)
leds.on()
sleep(1)
while True:
    leds.value = (1, 0, 0)
    sleep(xTime)
    leds.value = (0, 1, 0)
    sleep(vTime)
    leds.value = (0, 0, 1)
    sleep(dTime)
