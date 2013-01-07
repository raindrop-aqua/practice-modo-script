#python
# -*- coding:utf-8 -*-

import os, lx

result = lx.eval("query platformservice path.path ? content")

# required full path
os.system("start main.exe " + result)
