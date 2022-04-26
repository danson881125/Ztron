# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import receive
import reply

class Handle(object):
        def GET(self):
            try:
                data = web.input()
                if len(data) == 0:
                    return "hello, this is handle view"
                signature = data.signature
                timestamp = data.timestamp
                nonce = data.nonce
                echostr = data.echostr
                token = "ztronnum1" #请按照公众平台官网\基本配置中信息填写
       
                list = [token, timestamp, nonce]
                list.sort()
                sha1 = hashlib.sha1()
                sha1.update(list[0].encode('utf-8'))
                sha1.update(list[1].encode('utf-8'))
                sha1.update(list[2].encode('utf-8'))
                hashcode = sha1.hexdigest()

                print("handle/GET func: hashcode, signature: ", hashcode, signature)
                if hashcode == signature:
                    return echostr
                else:
                    return ""
            except (Exception,Argument):
                return Argument

        def POST(self):
            try:
                webData = web.data()
                print("Handle Post webdata is ",webData)
                # 后台打印日志
                recMsg = receive.parse_xml(webData)
                if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = "test!!"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'event' and recMsg.Event == 'subscribe':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = "xiexieguanzhu!!"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    print("zan bu chu li")
                    return "success"
            except (Exception,Argument):
                return Argument
