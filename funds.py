from asyncio import wait_for
import requests
import json
import re
import webbrowser
from datetime import datetime


tickers = ["000251","001511","001557","001592","005911","005919","110020","163409","001717","002009","005919","010869","163402","519738","001204","007658","002803","002986","005706","009076","163406","501049"]  # 基金代码
for ticker in tickers:
    url = "http://fundgz.1234567.com.cn/js/%s.js"%ticker
    # 浏览器头
    headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text
    pattern = r'^jsonpgz\((.*)\)'
    search = re.findall(pattern, content)
    # 遍历结果
    for i in search:
        data = json.loads(i)
        datejzrq = datetime.strptime(data["jzrq"],"%Y-%m-%d")
        wizjzrq = datetime.strftime(datejzrq,"%Y%m%d")
        moneywiz = str("moneywiz://updateholding?symbol={}.CN&price={}&date=".format(data['fundcode'],data['dwjz']) + wizjzrq)
        webbrowser.open(moneywiz) # 运行
