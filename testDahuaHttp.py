import requests
import grequests
from tornado.httpclient import AsyncHTTPClient
import json

def sendMsg(msg):
    print("aaa")


path = r"s.txt"

file = open(path, "r", encoding="utf-8", errors="ignore")

task = []
i = 0
while True:
    mystr = file.readline()  # 表示一次读取一行
    if not mystr:
        # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
        break
    print(mystr, end="")  # 打印每次读到的内容
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }

    # jsonObj = json.loads(mystr)

    # if jsonObj['data']['alarmData']['ManTempInfo']['HighTemp'] <= 32:
    #     print("ssssssss=> %s", mystr)

    # http_client = tornado.httpclient.
    # http_client.fetch("http://192.168.2.15:52000/agent", method='POST', body=mystr, headers=headers)
 
    # responses = grequests.post(url="http://192.168.2.15:52000/agent", data=mystr, headers=headers)
    # task.append(responses)
    # task.append(responses)
    requests.post("http://192.168.2.15:52000/agent", data=mystr, headers=headers)
    i = i + 1
    # response = requests.post("http://192.168.2.15:52000/agent", data=mystr, headers=headers).text
    # print("Server response ", response)


# resp = grequests.map(task)
# print(resp)
print(i)
