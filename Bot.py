import asyncio
import websockets
import json
import Twitch
import random

IP_ADDR = "0.0.0.0"
IP_PORT = "8421"
global state
state = True
group_id = xxxxxxxxx

# 接收从客户端发来的消息并处理，再返给客户端
async def serverinteractive(websocket):
    global state
    while True:
        recv_text = await websocket.recv()
        recv_text = json.loads(recv_text)
        recv_text = json.dumps(recv_text,indent = 2)
        print(recv_text)
        if random.randint(1, 10) > 6:
            print('[INFO]:good roll')
            game,title = Twitch.check_online('sunshinebread')
            print(game)
            if game:
                if state == False:
                    data = {"action":"send_group_notice","params":{"group_id":group_id,"content":f"sunshinebread is online,{game},{title}"}}
                    print('sunshinebread went alive,sending group notice')
                    state = True
                    await websocket.send(json.dumps(data))
            elif state == True:
                data = {"action":"send_group_notice","params":{"group_id":group_id,"content":f"sunshinebread is not online"}}
                print('sunshinebread went offline,sending group notice')
                state = False
                await websocket.send(json.dumps(data))
        else:
            print('[INFO]:bad roll')

# 接收数据
async def serverRun(websocket,path):
    await serverinteractive(websocket)

async def main():
    print("======server main begin======")
    server = await websockets.serve(serverRun, IP_ADDR, IP_PORT)
    await server.wait_closed()

asyncio.run(main())
