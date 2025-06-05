import asyncio
import websockets
from app import average_calculator


class WebSockets:
    def __init__(self):
        self.WS_URL = "ws://152.70.50.114:8765/sndr"
        self.SEND_INTERVAL = 2


    async def send_data(self, weight: float):
        async with websockets.connect(self.WS_URL) as websocket:
            print(f"Forbundet til {self.WS_URL}")
            while True:
                data = f"{weight}"
                await websocket.send(data)
                print(f"Sendt: {data}")
                await asyncio.sleep(self.SEND_INTERVAL)


ws = WebSockets()
ac = average_calculator

if __name__ == "__main__":
    try:
        asyncio.run(ws.send_data(ac.run()))
    except KeyboardInterrupt:
        print("Afslutter...")