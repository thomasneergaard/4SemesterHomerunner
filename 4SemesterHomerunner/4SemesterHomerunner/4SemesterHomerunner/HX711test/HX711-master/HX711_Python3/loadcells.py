import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)

hx.zero()
input ('Sæt en kendt vægt på sensoren og tryk Enter:')
reading = hx.get_data_mean(readings=100)

known_weight_grams = input ('Indtast den kendte vægt og tryk Enter:')
value = float(known_weight_grams)

ratio = reading/value
hx.set_scale_ratio(ratio)

def main():
    print("")
    raw_weight = hx.get_weight_mean()
    print("Vægt " + str(raw_weight))
    return raw_weight
   
    
main()