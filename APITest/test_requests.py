#-*-coding:utf-8-*-
import requests
import logging
import json

class TestRequest(object):
    logging.basicConfig(level=logging.INFO)
    url="https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r=requests.get(self.url)
        logging.info(r)
        #logging.info(r.text)

        #将 Python 对象编码成 JSON 字符串
        logging.info(json.dumps(r.json(),indent=2))

    def test_post(self):
        r=requests.post(self.url,
                        params={"a":1,"b":"string content"},
                        proxies={"https":"127.0.0.1:7888"},
                        #伪造本地证书
                        verify=False)
        logging.info(r)
        #logging.info(r.text)
        #序列化json格式1
        logging.info(json.dumps(r.json(),indent=2))

    def test_cookies(self):
        r = requests.get("http://47.95.238.18:8090/cookies",
                         cookies={"a": "1", "b": "string corntent"})
        logging.info(r.text)

    def test_xueqiu(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        r = requests.get(url,
                         params={"category": "1"},
                         headers={'User-Agent': 'Xueqiu Android 11.19'},
                         cookies={"u": "3446260779", "xq_a_token": "5806a70c6bc5d5fb2b00978aeb1895532fffe502",
                                  }

                         # verify=False
                         )

        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
