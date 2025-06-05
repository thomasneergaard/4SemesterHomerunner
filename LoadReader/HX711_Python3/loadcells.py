import RPi.GPIO as GPIO                # import GPIO
from hx711 import HX711                # import the class HX711
import time
  
GPIO.setmode(GPIO.BCM)                 # set GPIO pin mode to BCM numbering
hx = HX711(dout_pin=6, pd_sck_pin=5)




hx.set_scale_ratio(-20.7045454545456)
hx.zero()

#hx.set_scale_ratio(-19.8501837696336)
#17.743789731051345
#-19.094240837696336


#input(' vagt')
while True:
    reading = hx.get_weight_mean()
    #reading = hx.get_weight_mean()
    result = reading/1000
    d = round(result, 3)
    print(d)
    time.sleep(1)
    
