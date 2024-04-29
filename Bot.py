import asyncio
import websockets
import Twitch
import bili
import logging
import json
import datetime
import pytz

IP_ADDR = "0.0.0.0"
IP_PORT = "8421"

Test_group = 9272775600#你可以用来测试Bot的小群
sunshine_group = 859055590#你想要推送的主群
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

async def mainfunc(websocket,path):
    global state
    while True:
        logging.warning('starting main program ...')

        game,title,viewer_count = Twitch.check_online(streamer)
        if game != "False":
            logging.warning(f'{streamer}在线')
            logging.warning(f'game:{game}')
            logging.warning(f'title:{title}')
            logging.warning(f'viewer_count:{viewer_count}\n')

            if state == 'offline':
                state = 'online'
                now = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
                await send_group_at_all_msg(websocket,sunshine_group,f"{streamer}上线啦,纽约时间{now.hour}:{now.minute},正在玩{game},{title},目前有{viewer_count}在看,直播间链接:https://www.twitch.tv/{streamer}")
                logging.warning(f'sending group msg\n')
        else:
            logging.warning(f'{streamer}不在线\n')
            if state == 'online':
                state = 'offline'
                now = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
                await send_group_at_all_msg(websocket,sunshine_group,f"{streamer}下机喽,纽约时间{now.hour}:{now.minute}")
                logging.warning(f'sending group msg\n')

        up_name,media_title,media_link = await bili.get_up_video(up_list)

        if up_name != "False":
            await send_group_at_all_msg(websocket,sunshine_group,f"{up_name}发布了新视频!{media_title},{media_link}")
            logging.warning(f'sending group msg\n')
        now = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))
        logging.warning(f'{now}\n\n')
        await asyncio.sleep(60)#设置间隔，我不希望访问过于频繁

async def main():
    Set_Level()#主要是用来测试，防止新功能出问题在大群里一直乱发消息
    print(f"========================server main run at {IP_ADDR}:{IP_PORT}========================")
    server = await websockets.serve(mainfunc, IP_ADDR, IP_PORT)
    await server.wait_closed()

asyncio.run(main())
