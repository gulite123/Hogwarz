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