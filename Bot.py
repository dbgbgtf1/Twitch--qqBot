import asyncio
import websockets
import json
import Twitch

IP_ADDR = "0.0.0.0"
IP_PORT = "xxxxxx"you can choose what port to open in your server
global state
state = False
global Test_group
Test_group = xxxxxxxx
global sunshine_group
sunshine_group = xxxxxxxx

def Set_Level():
    global sunshine_group
    global Test_group
    print("choose the mode to start with[DEBUG/NORMAL]")
    while(True):
        level = input()
        if level == "DEBUG":
            sunshine_group = Test_group
            print("DEBUG mode starts!")
            return
        if level == "NORMAL":
            print("NORMAL mode starts!")
            return
        else:
            print("don't know what are u talking about")

async def send_group_at_all_msg(websocket,group_id,content):
    data = {
        "action":"send_group_msg",
        "params":
        {
            "group_id":group_id,
            "message":
            [
            {"type": "at","data": {"qq":"all"}},
            {"type": "text","data": {"text": f"{content}"}}
            ]
        }
    }
    print('\nsunshinebread went alive,sending group msg\n')
    state = True
    await websocket.send(json.dumps(data))

async def send_group_to_msg(websocket,group_id,content):
    data = {
        "action":"send_group_msg",
        "params":
            {
                "group_id":group_id,
                "message":{"type": "text","data": {"text": f"{content}"}}
            }
        }
    print(f'\ntriggered by private message\n')
    await websocket.send(json.dumps(data))

async def mainfunc(websocket):
    # main_function
    global sunshine_group
    global Test_group
    global state
    while True:
        recv_text = await websocket.recv()
        recv_text = json.loads(recv_text)
        # recv_text = json.dumps(recv_text,indent = 2)
        print(recv_text)

        if (recv_text.get("sub_type") == "friend"):
            await send_group_to_msg(websocket,Test_group,"i am still alive!")
            return
            #only to check the Bot live condition with my phone
            #this msg will be send to my test group in any condition

        game,title = Twitch.check_online('sunshinebread')
        print(f'game: {game}\ntitle:{title}')

        if game:#this means sunshinebread is alive
            if state == False:#this means havn't sent it
                await send_group_at_all_msg(websocket,sunshine_group,f"sunshinebread went alive,{game},{title}")
                #so send it

        else:#this means sunshinebread is not alive
            if state == True:#this means havn't sent it
                await send_group_at_all_msg(websocket,sunshine_group,"sunshinebread went offline")
                #so send it

async def serverRun(websocket,path):
    await mainfunc(websocket)

async def main():
    Set_Level()
    #sometimes i need to test new function,so i can set DEBUG mode
    #in this way,i send all my msg in my test group
    print("========================server main begin========================")
    server = await websockets.serve(serverRun, IP_ADDR, IP_PORT)
    await server.wait_closed()

asyncio.run(main())
