import ijson
import datetime
import json
import re

def retrieve_data(filename, output_filename, MESSAGE_SENDER_0, MESSAGE_SENDER_1):
    first_item = True
    with open(filename, 'rb') as f, open(output_filename, 'w', encoding='utf-8') as out_file:
        objects = ijson.items(f, 'item')
        out_file.write('[') 
        for obj in objects:
            if obj["mesDes"] == 0:
                sender = MESSAGE_SENDER_0
            elif obj["mesDes"] == 1:
                sender = MESSAGE_SENDER_1

            msgType = obj["messageType"] #1是文字，3是图片，34是语音；37是好友添加；43是视频；48是位置； 49是xml格式消息； 10000是系统消息
            realTime = datetime.datetime.fromtimestamp(obj["msgCreateTime"]).strftime('%Y-%m-%d %H:%M:%S')

            if msgType == 1:
                msgContent = obj['msgContent']
            elif msgType == 3:
                msgContent = "<image>"
            elif msgType == 34:
                msgContent = "<audio message>"
            elif msgType == 37:
                msgContent = "<add friend>"
            elif msgType == 43:
                msgContent = "<video>"
            elif msgType == 48:
                msgContent = "<location>"
            elif msgType == 47:
                msgContent = "<emoji>"
            elif msgType == 49:
                if "tickled" in obj['msgContent']:
                    if sender == MESSAGE_SENDER_0:
                        sender = MESSAGE_SENDER_1
                        msgContent = MESSAGE_SENDER_1 + " tickled " + MESSAGE_SENDER_0
                    else:
                        sender = MESSAGE_SENDER_0
                        msgContent = MESSAGE_SENDER_0 + " tickled " + MESSAGE_SENDER_1

                elif "<refermsg>" in obj['msgContent']:
                    title_match = re.search('<title>(.*?)</title>', obj['msgContent'])
                    if title_match:
                        title_content = title_match.group(1)
                        msgContent = title_content

                else:
                    msgContent = "<other xml message>"

            elif msgType == 10000:
                msgContent = "<system message>"
            else:
                msgContent = "<undefined message>"
            
            data = {
                "msgSender": sender,
                "msgType": msgType,
                "msgContent": msgContent,
                "realTime": realTime
            }
            
            if not first_item:
                out_file.write(',')  
            else:
                first_item = False  
            
            json.dump(data, out_file, ensure_ascii=False)
        
        out_file.write(']') 