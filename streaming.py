import json
import asyncio
import websockets
import datetime

url = 'wss://ws-subscriptions-clob.polymarket.com/ws/market'
last_time_pong = datetime.datetime.now()
msgs = []

kamala_trump_yes_token = "token_address_here"  # Replace with actual token address 4 yes
kamala_trump_no_token = "token_address_here"  # Replace with actual token address 4 no

async def listen_for_events():
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps({"assets_ids":[kamala_trump_yes_token, kamala_trump_no_token],"type":"market"}))

        while True:
            m = await websocket.recv()
            if m != "PONG":
                last_time_pong = datetime.datetime.now()
            d = json.loads(m)
            if last_time_pong + datetime.timedelta(seconds=10) < datetime.datetime.now():
                await websocket.send("PING")
            else:
                msgs.append(d)

if __name__ == "__main__":
    asyncio.run(listen_for_events())
