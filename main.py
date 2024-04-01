from date_data import*
from Retrive_data import retrieve_data
from word_cloud import*

if "__main__" == "__main__":
    ###改下面变量名⬇
    filename = 'Sample_Chat_History.json' #改成聊天记录json文件名
    MESSAGE_SENDER_0 = "A"  #自己的名字
    MESSAGE_SENDER_1 = "B"  #对方的名字

    retrieve_data(filename, "output.json", MESSAGE_SENDER_0, MESSAGE_SENDER_1) #整整理和提取原始聊天记录文件
    count_message_in_a_day("output.json") #统计每天聊天的频率（条）
    
