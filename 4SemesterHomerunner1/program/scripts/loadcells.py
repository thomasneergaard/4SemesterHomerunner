import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6, pd_sck_pin=5)


#input ('set en vegt')
#reading = hx.get_data_mean(readings=500)
#print(reading)

#known_weight_grams = input ('vagt')
#value = float(known_weight_grams)

#ratio = reading/value
#print(ratio)
hx.set_scale_ratio(-20.79251)
hx.zero()

while True:
    
    weight = hx.get_weight_mean()
    print(weight)

#def main():
 #   print("")
  #  raw_weight = hx.get_weight_mean()
   # print("vegt" + str(raw_weight))
    #return raw_weight
   
    