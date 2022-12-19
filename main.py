from machine import *
from utime import sleep
from grove_lcd_i2c import Grove_LCD_I2C

sleep(1)
print("MicroPython on Raspberry Pi Pico")
print()

led = Pin(25, Pin.OUT)

LCD_SDA = Pin(14)
LCD_SCL = Pin(15)
LCD_ADDR = 62
i2c = I2C(1, sda=LCD_SDA, scl=LCD_SCL)

lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.clear()
lcd.write(" Hello World! ")

