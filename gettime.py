# 获取当前时间
#!/usr/bin/python3
# -*- coding: utf-8 -*-

def time():
    import time
    localtime = time.asctime( time.localtime(time.time()) )
    print ("本地时间为 :", localtime)
