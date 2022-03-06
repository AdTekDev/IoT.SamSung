from gpiozero import LEDBoard
from time import sleep
from signal import pause
#######################3
# Doc file cau hinh o day

xTime = 5
vTime = 3
dTime = 8

##################### Functions

ledNum = {
    -1 :(0,0,0,0,0,0,0),
    0 :(1,1,1,1,1,1,0),
    1 :(0,1,1,0,0,0,0),
    2 :(1,1,0,1,1,0,1),
    3 :(1,1,1,1,0,0,1),
    4 :(0,1,1,0,0,1,1),
    5 :(1,0,1,1,0,1,1),
    6 :(1,0,1,1,1,1,1),
    7 :(1,1,1,0,0,0,0),
    8 :(1,1,1,1,1,1,1),
    9 :(1,1,1,1,0,1,1)
}

def showLED(N):
    if (N >= -1  and N < 10):
        print(ledNum[N])
        ledsNumber.value = ledNum[N]

def demNguoc(N):
    while N>0:
        sleep(1)
        print(N)
        showLED(N)
        N = N-1

def readFile():
    f = open("traffic_conf.txt", "r")
    xTime = int(f.readline())
    print(xTime) 
    vTime = int(f.readline())
    print(vTime) 
    dTime = int(f.readline())
    print(dTime) 
    f.close()

####################### MAIN CODE 
readFile()

ledsTraffic = LEDBoard(12, 16, 18)
ledsTraffic.on()

ledsNumber= LEDBoard(11,4,23,8,7,10, 17,25)
ledsNumber.on()

sleep(1)
while True:
    ledsTraffic.value = (1, 0, 0)
    demNguoc(xTime)
    ledsTraffic.value = (0, 1, 0)
    demNguoc(vTime)
    ledsTraffic.value = (0, 0, 1)
    demNguoc(dTime)
