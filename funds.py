import requests
import json
import re
import webbrowser


tickers = ["000251","001511"]  # 以此类推输入基金代码
for ticker in tickers:
    url = "http://fundgz.1234567.com.cn/js/%s.js"%ticker
    # 浏览器头
    headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    content = r.text # 获取数据
    pattern = r'^jsonpgz\((.*)\)'
    search = re.findall(pattern, content)
    # 遍历结果
    for i in search:
        data = json.loads(i)
        # 数据 (data,type(data))
        moneywiz = "moneywiz://updateholding?symbol={}.CN&price={}&date={}".format(data['fundcode'],data['dwjz'],data['jzrq']) # 生成指令
        webbrowser.open(moneywiz) # 运行
