import RPi.GPIO as GPIO
from hx711 import HX711

class Loadcells:
    def __init__(self):

        """Henter en vaegt fra badevaegten og omdanner vaegten fra gram til kg
         Returnerer vaegt i kg"""
    def get_weight_in_kg(self, weight: float):
        if weight == 0 or weight < 0:
            return 0
        return weight / 1000


GPIO.setmode(GPIO.BCM)
lc = Loadcells()
hx = HX711(dout_pin=6, pd_sck_pin=5)
hx.zero()
hx.set_scale_ratio(-20.79251)
def run():
    print("running...")
    weight = lc.get_weight_in_kg(hx.get_weight_mean())
    return weight