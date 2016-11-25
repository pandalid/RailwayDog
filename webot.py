import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def text_reply(msg):
    itchat.send('%s' % msg['Text'], msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()
