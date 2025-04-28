import loadcells as lc
import time

lc
def test():
    data = lc.main()
    print(data)
    
i = 0
while i < 20:
    test()
    time.sleep(1)