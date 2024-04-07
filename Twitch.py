import requests
#api信息和主播名字
client_id = 'Your_client_id'
client_secret = 'Your_client_secret'
streamer_name = 'xxxxxxx'
#######################################################################################################

#OAuth获取的访问登录凭证
body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)
oauth = r.json()

#用登录凭证和client_id访问api
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + oauth['access_token']
}
api_result = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
stream_data =api_result.json()

#根据api返回的结果判断是否在线
if len(stream_data['data']) == 1:
    print(streamer_name + ' 在线,正在玩' + stream_data['data'][0]['game_name'] + stream_data['data'][0]['title'])
else:
    print(streamer_name + ' 不在线')
