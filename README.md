# Twitch，b站->qqBot

#### what can it do

这是一个服务器上的后端项目，其作用是定时获取Twitch台指定主播在线状态及b站指定up的新视频，并且将其推送指qq群聊.

手机上打开被动websocket，设置端口和服务器公网ip作为websocket连接地址即可。

具体操作可以去看看openshamrock的github主页

___

#### how you use it

指定主播和up需要直接对代码块修改，有点麻烦并且可能出错，i know，下次试试解决这个问题。

__指定主播的功能需要在Bot.py里面更改`stream`变量的值即可，将其改成Twitch台主播的名字。__

__指定up的功能则需要在Bot.py里面改掉up主的名字和uid号。__

```python
up_list = {}
up_list['小小小Janey'] = 32149224
up_list['TheOnlyShark'] = 517913954
up_list['COMAYUMI'] = 14445191
up_list['HeNTa1111'] = 1114874220
up_list['sunshine102506'] = 3537124194257576
#欢迎大家来关注这些up
```

以上两个功能如果想要在bili.py和Twitch.py里面单独测试，都需要在这两个文件里单独再改。

**以及指定up的功能还需要再项目当前目录下创建与up主名字同名的文件。**

```shell
touch 小小小Janey
```

**最后是服务器端口设置及群聊号设置。**

端口没有什么特别讲究，只要和手机上openshamrock保持一致即可

```python
IP_ADDR = "0.0.0.0"
IP_PORT = "8421"

Test_group = xxxxxxxx#没什么人，或全是机器人的群
sunshine_group = 859055590#要推送的主群
```

Test_group在你启动项目设置DEBUG模式时会被用到，**在DEBUG模式下，所有消息都会被发送到Test_group。**

用于在大片更改代码之后心里没底的时候测试用，防止机器人出事把主群炸了。
### 最后是项目效果
![43ae69a8be0f4370d8ac70ab003af35e](https://github.com/dbgbgtf1/Twitch-bili--QQBot/assets/149954065/c7242568-2cbe-431a-8798-afbda942fe0d)

![30637e44dab0aec227e2ecc302857fe6](https://github.com/dbgbgtf1/Twitch-bili--QQBot/assets/149954065/e57d2bc7-7fd5-4edb-ba46-61baa04f70f3)

![image](https://github.com/dbgbgtf1/Twitch-bili--QQBot/assets/149954065/b08a6201-e1b4-44c5-959a-f4787609a239)

最后两张图还没更新成最新的效果



