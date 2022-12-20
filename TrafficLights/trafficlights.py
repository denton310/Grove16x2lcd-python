from machine import Pin
from time import sleep

led_red = Pin(2, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
led_green = Pin(4, Pin.OUT)

led_red.value(0)
led_yellow.value(0)
led_green.value(0)

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Change mode between LIGHTS_ACTIVE and YELLOW_BLINKING
def button_pressed():
    print("button pressed")
    lights_active = not lights_active
    seconds = 0

button1.irq(handler=button_pressed, trigger=Pin.IRQ_FALLING)

lights_active = 1
seconds = 0;

def update_lights():
    global seconds
    print("seconds:", seconds)
    if (seconds < 5):
        led_red.value(0)
        led_yellow.value(0)
        led_green.value(1)
        
    elif (seconds < 6):
        led_red.value(0)
        led_yellow.value(1)
        led_green.value(0)
        
    elif (seconds < 11):
        led_red.value(1)
        led_yellow.value(0)
        led_green.value(0)
        
    elif (seconds < 12):
        led_red.value(1)
        led_yellow.value(1)
        led_green.value(0)
    
def update_idle():
    global seconds
    
    if (seconds % 2 == 0):
        led_red.value(0)
        led_yellow.value(1)
        led_green.value(0)
    else:
        led_red.value(0)
        led_yellow.value(0)
        led_green.value(0)

while True:
    
    if (lights_active):
        update_lights()
    else:
        update_idle()
    
    if(seconds == 11):
        seconds = 0
    else:
        seconds = seconds + 1

    sleep(1)
    