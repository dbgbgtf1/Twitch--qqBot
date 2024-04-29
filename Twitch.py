import requests
#api信息和主播名字
client_id = 'Your_client_id'
client_secret = 'Your_client_secret'
streamer_name = 'xxxxxxx'
#######################################################################################################

def checj_online(streamer_name):
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
    
    if len(stream_data['data']) == 1:
        return stream_data['data'][0]['game_name'],stream_data['data'][0]['title'],stream_data['data'][0]['viewer_count']
    else:
        return "False","False","False"
