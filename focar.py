from machine import Pin, PWM
from time import sleep

e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

SPEED = 50000

led = Pin("LED", Pin.OUT)


def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)


def forward(seconds):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(seconds)
    stop()


def forward_left(seconds):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(60000)
    e2.duty_u16(35000)
    sleep(seconds)
    stop()


def backward_right(seconds):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(35000)
    e2.duty_u16(60000)
    sleep(seconds)
    stop()


def led_on():
    led.value(1)


def led_off():
    led.value(0)