import loadcells
import average_calculator
import time

running = True

while(running):
    
    average_calculator.main(loadcells.main())
    time.sleep(1)
