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
        #序列化json格式
        logging.info(json.dumps(r.json(),indent=2))
