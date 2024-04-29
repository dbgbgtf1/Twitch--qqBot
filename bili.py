import json
import logging
from bilibili_api import user,sync
import asyncio
# 实例化
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    logging.warning(f"writing {content} into file {filename}")

def compare_file(filename,target_string):
    with open(filename, 'r+') as file:
        file_content = file.read()
        if target_string == file_content:
            logging.warning(f'{target_string} == {file_content}')
            return False
        else:
            file.seek(0)
            file.truncate()
            logging.warning(f'{target_string} != {file_content}')
            return True

async def get_up_video(up_list):
    for up_name,up_uid in up_list.items():
        up = user.User(uid = up_uid)

        media = await up.get_media_list(ps = 1)

        bv_id = media.get("media_list")[0].get("bv_id")
        logging.warning('bv_id:' + bv_id)
        #print(json.dumps(media,indent = 2,ensure_ascii = False))

        if compare_file(up_name,bv_id):
            media_title = media.get("media_list")[0].get("title")
            media_link = media.get("media_list")[0].get("short_link")
            write_file(up_name,bv_id)
            logging.warning(f"{up_name}发布了新视频!")
            logging.warning(f'视频标题:{media_title}')
            logging.warning(f'视频链接:{media_link}\n')
            return up_name,media_title,media_link
        else:
            logging.warning(f"{up_name} no new video\n")
    return "False","False","False"

if __name__ == "__main__":
    print("testing bili.py ...")
    up_list = {}
    up_list['小小小Janey'] = 32149224
    up_list['TheOnlyShark'] = 517913954
    up_list['COMAYUMI'] = 14445191
    up_list['HeNTa1111'] = 1114874220
    up_list['sunshine102506'] = 3537124194257576
    sync(get_up_video(up_list))
