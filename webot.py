import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def replay(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()
