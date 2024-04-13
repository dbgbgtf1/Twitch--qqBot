# Twitch->qqBot
借用openshamrock框架实现的一个机器人，其作用是从Twitch台获取主播直播信息并向qq群推送。

本项目是部署在服务器的后端程序，前端是手机上的openshamrock软件。

我使用了websocket通信，因为不知道怎么做到服务器主动连接手机。（手机毕竟没有公网ip，涉及到内网又很麻烦）

所以现在的解决方案是利用openshamrock上定时向服务器的传输的heartbeat(大概是叫这个？)，来维持稳定通信。

缺点是必须保持手机端的openshamrock和qq不被后台杀掉。

每次手机向服务器传输确认信息的时候，就让服务器检查Twitch台主播通信状态。

2024.4.13更新

把at全体群成员及发送群消息两个功能做了简单封装，升级了DEBUG和NORMAL模式，方便调试。

加了一个检查机器人是否在线的简单功能。场景是Bot正在宿舍的手机上面运行。

在外面时可以通过用大号给机器人私发消息，如果机器人活着，会在测试群发一句简单消息。
