#!usr/bin/env python
# coding:utf-8
import requests
from pprint import pprint
res=requests.get('https://api.github.com/events')
res=requests.post()
print(res.status_code)
pprint(res.json())