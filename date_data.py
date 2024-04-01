import json
import jieba
import re
from datetime import datetime
from Retrive_data import *


def count_message_in_a_day(filename):
    with open('output.json', 'r', encoding='utf-8') as file:
        chat_data = json.load(file)
    
    date_freq = {}
    
    for msg in chat_data:
        content = msg["realTime"]
        
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        date_match = date_pattern.search(content)
        if date_match:
            date = date_match.group()
            
        if date not in date_freq:
            date_freq[date] = 1
        else:
            date_freq[date] += 1
    
    word_freq_list = [{"date": date, "freq": freq} for date, freq in date_freq.items()]
    with open('每天聊天频率统计.json', 'w', encoding='utf-8') as out_file:
        json.dump(word_freq_list, out_file, ensure_ascii=False, indent=4)


def count_sender(filename):
    with open('output.json', 'r', encoding='utf-8') as file:
        chat_data = json.load(file)

    msg_sender = {}
    
    for msg in chat_data:
        content = msg["msgSender"]
            
        if content not in msg_sender and msg["msgType"] == 1:
            msg_sender[content] = 1
        elif content in msg_sender and msg["msgType"] == 1:
            msg_sender[content] += 1
    
    word_freq_list = [{"msgSender": sender, "freq": freq} for sender, freq in msg_sender.items()]
    with open('date_frequency.json', 'w', encoding='utf-8') as out_file:
        json.dump(word_freq_list, out_file, ensure_ascii=False, indent=4)


def count_sender_letter(filename):
    with open('output.json', 'r', encoding='utf-8') as file:
        chat_data = json.load(file)

    msg_sender = {}
    
    for msg in chat_data:
        content = msg["msgSender"]
            
        if content not in msg_sender and msg["msgType"] == 1:
            msg_sender[content] = len(msg["msgContent"])
        elif content in msg_sender and msg["msgType"] == 1:
            msg_sender[content] += len(msg["msgContent"])
    
    word_freq_list = [{"msgSender": sender, "freq": freq} for sender, freq in msg_sender.items()]
    with open('date_frequency.json', 'w', encoding='utf-8') as out_file:
        json.dump(word_freq_list, out_file, ensure_ascii=False, indent=4)



def count_message_in_weekday(filename):
    with open('output.json', 'r', encoding='utf-8') as file:
        chat_data = json.load(file)
    
    weekday_date_freq = {}
    
    for msg in chat_data:
        content = msg["realTime"]
        
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        date_match = date_pattern.search(content)
        if date_match:
            date = date_match.group()
        
        date = datetime.strptime(date, '%Y-%m-%d')
        weekday = date.strftime('%A')

        if weekday not in weekday_date_freq:
            weekday_date_freq[weekday] = 1
        else:
            weekday_date_freq[weekday] += 1
    
    word_freq_list = [{"date": weekday, "freq": freq} for weekday, freq in weekday_date_freq.items()]
    with open('date_frequency.json', 'w', encoding='utf-8') as out_file:
        json.dump(word_freq_list, out_file, ensure_ascii=False, indent=4)