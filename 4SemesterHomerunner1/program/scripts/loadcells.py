import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)
hx.set_scale_ratio(-20.79251)

def get_weight():
    return hx.get_weight_mean()

def get_weight_in_kg():
    weight = hx.get_weight_mean()
    if weight == 0 or weight < 0:
        weight = 1
    return round(weight, 1)

def reset():
    hx.zero()



while True:
    
    weight = hx.get_weight_mean()
    print(weight)


    