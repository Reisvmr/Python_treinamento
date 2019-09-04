#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:49:46 2019

@author: viniciusreis
"""
r = requests.post('http://httpbin.org/post', data={'comentario': 'huaaaaaaa'})
print r.status_code
200
print r.content
{
  "origin": "xxx.xxx.xxx.xxx",
  "files": {},
  "form": {
    "comentario": "huaaaaaaa"
  },
  "url": "http://httpbin.org/post",
  "args": {},
  "headers": {
    "Content-Length": "20",
    "Via": "1.0 PROXY",
    "Accept-Encoding": "identity, deflate, compress, gzip",
    "Connection": "close",
    "Accept": "*/*",
    "User-Agent": "python-requests/0.12.1",
    "Host": "httpbin.org",
    "Cache-Control": "max-age=259200",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "json": null,
  "data": ""
}