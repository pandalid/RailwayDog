import itchat,tuling
from itchat.content import *

# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('你好，欢迎添加我为好友!虽然我只是一个机器人，但是希望我们一样也可以做好朋友！', msg['RecommendInfo']['UserName'])

# 收到文本消息自动回复(使用图灵机器人)
@itchat.msg_register(TEXT)
def text_reply(msg):
    return tuling.get_response(msg['Text']) or u'收到：' + msg['Text']
    #itchat.send('%s' % msg['Text'], msg['FromUserName'])

@itchat.msg_register(PICTURE)
def picture_download(msg):
    msg['Text'](msg['FileName'])
    itchat.send('已存储图片',msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()