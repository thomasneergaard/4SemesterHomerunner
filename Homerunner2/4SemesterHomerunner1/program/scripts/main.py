import average_calculator
import time
import asyncio
import websockets
import json


WS_URL = "ws://152.70.50.114:8765/sndr"
SEND_INTERVAL = 1
    
    
def calculate_data():
    data = {
    "Weight":average_calculator.get_weight_number()
    }
    #return json.dumps(data)
    return data

async def send_data():
    old_data = 0
    async with websockets.connect(WS_URL) as websocket:
        print(f"Forbundet til {WS_URL}")
        while True:
            if data != old_data:
                old_data = data
                data = json.dumps(calculate_data())
                await websocket.send(data)
                print(f"Sendt: {data}")
                await asyncio.sleep(SEND_INTERVAL)


#if __name__ == "__main__":
 #   try:
  #      asyncio.run(send_data())
  # except KeyboardInterrupt:
     #   print("Afslutter...")
        
while True:
    
    weight2 = average_calculator.get_weight_raw()
    weight = average_calculator.get_weight_number()
    print("Forarbejdet nummer: " + str(weight))
    print("Råt nummer:" + str(weight2))

