import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)
hx.zero()
hx.set_scale_ratio(-20.79251)

def get_weight_in_grams():
    weight = hx.get_weight_mean()
    return weight

def get_weight_in_kg():
    weight = hx.get_weight_mean()
    if weight == 0 or weight < 0:
        weight = 1
    return weight

def reset():
    hx.zero()




    



    