#-*-coding:utf-8-*-
import requests
import logging
import json

class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url="https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r=requests.get(self.url)
        logging.info(r)
        #logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))#将 Python 对象编码成 JSON 字符串

    def test_post(self):
        r=requests.post(self.url,params={"a":1,"b":"string corntent"},
                        proxies={"https":"127.0.0.1:7888"}
                        )
        logging.info(r.url)
        logging.info(r.text)


