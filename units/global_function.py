import time
from flask import request

def get_time():
    computer_time = str(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))
    return computer_time



def html_to_chinese(txt):
    linshibianliang = ""
    for i in txt:
        if is_Chinese(i):
            linshibianliang = linshibianliang + i
        if i == "." or i == "。" or i == "," or i == "，" or i == "!" or i == "！" or i == "?" or i == '？' or i == "《" or i == "》":
            linshibianliang = linshibianliang + i
    return linshibianliang



def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def get_ip():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return ip

