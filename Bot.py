import asyncio
import websockets
import Twitch
import bili
import logging
import json
import time

IP_ADDR = "0.0.0.0"
IP_PORT = "xxxx"

Test_group = xxxxxx你可以用来测试Bot的小群
sunshine_group = xxxxxx你想要推送的主群
streamer = 'sunshinebread'#你想推送的主播在Twitch台主播名
state = 'online'
up_list = {}
up_list['小小小Janey'] = 32149224
up_list['TheOnlyShark'] = 517913954
up_list['COMAYUMI'] = 14445191
up_list['HeNTa1111'] = 1114874220
up_list['sunshine102506'] = 3537124194257576
#欢迎大家关注这几个uphhh

def Set_Level():
    global sunshine_group
    print("choose the mode to start with[DEBUG/NORMAL]")
    while(True):
        level = input()
        if level == "DEBUG":
            sunshine_group = Test_group
            print("DEBUG mode starts!")
            logging.basicConfig(level=logging.WARNING,format="[DEBUG] %(message)s")
            return
        if level == "NORMAL":
            print("NORMAL mode starts!")
            logging.basicConfig(level=logging.WARNING,format="[NORMAL] %(message)s")
            return
        else:
            print("don't know what are u talking about\n")

async def send_group_at_all_msg(websocket,group_id,content):
    data = {
        "action":"send_group_msg",
        "params":
        {
            "group_id":group_id,
            "message":
            [
            {"type": "at","data": {"qq":"all"}},
            {"type": "text","data": {"text": content}}
            ]
        }
    }
    await websocket.send(json.dumps(data))

async def send_to_group_msg(websocket,group_id,content):
    data = {
        "action":"send_group_msg",
        "params":
            {
                "group_id":group_id,
                "message":{"type": "text","data": {"text": content}}
            }
        }
    await websocket.send(json.dumps(data))

async def mainfunc(websocket):
    global state
    while True:
        logging.warning('starting main program ...')

        game,title = Twitch.check_online(streamer)
        if game:
            logging.warning(f'{streamer}在线')
            logging.warning(f'game: {game}')
            logging.warning(f'title:{title}\n')
            if state == 'offline':
                state = 'online'
                #asyncio.create_task(send_to_group_msg(websocket,sunshine_group,f"{streamer} went alive,{game},{title}"))
                asyncio.create_task(send_group_at_all_msg(websocket,sunshine_group,f"{streamer} went alive,{game},{title}"))
                logging.warning(f'sending group msg\n')
        else:
            logging.warning(f'{streamer}不在线\n')
            if state == 'online':
                state = 'offline'
                #asyncio.create_task(send_to_group_msg(websocket,sunshine_group,f"{streamer} went offline"))
                asyncio.create_task(send_group_at_all_msg(websocket,sunshine_group,f"{streamer} went offline"))
                logging.warning(f'sending group msg\n')

        up_name,media_title,media_link = await bili.get_up_video(up_list)

        if up_name:
            #asyncio.create_task(send_to_group_msg(websocket,sunshine_group,f"Janey's new video!{media_title},{media_link}"))
            asyncio.create_task(send_group_at_all_msg(websocket,sunshine_group,f"{up_name}发布了新视频!{media_title},{media_link}"))
            logging.warning(f'sending group msg\n')
        print('\n\n')
        await asyncio.sleep(60)#设置间隔，我不希望访问直播状态过于频繁

async def serverRun(websocket,path):
    await mainfunc(websocket)

async def main():
    Set_Level()#主要是用来测试，防止新功能出问题在大群里一直乱发消息
    print("========================server main begin========================")
    server = await websockets.serve(serverRun, IP_ADDR, IP_PORT)
    await server.wait_closed()

asyncio.run(main())
