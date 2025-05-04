#import RPi.GPIO as GPIO
from hx711 import HX711
import time

#GPIO.setmode(GPIO.BCM)

#hx = HX711(dout_pin=6, pd_sck_pin=5)
#hx.zero()
#hx.set_scale_ratio(-20.79251)

# Lavet til for testing årsager
# Henter en vægt fra badevægten og returnerer den som float
def get_weight_in_grams():
    #weight = hx.get_weight_mean()
    weight = 0
    return weight

# Henter en vægt fra badevægten og omdanner vægten fra gram til kg
# Returnerer vægt i kg
def get_weight_in_kg():
    #weight = hx.get_weight_mean()
    weight = 0
    if weight == 0 or weight < 0:
        weight = 1
    return weight / 1000

def get_weight_in_kg_test():
    i = 0
    weight = 10000
    running = True
    while running:
        weight += 500
        i += 1
        if i >= 10.0:
            running = False
        time.sleep(1)
        return weight
    return weight

# Nulstiller vægten
def reset():
    hx.zero()