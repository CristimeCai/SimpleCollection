# -*- coding: utf-8 -*-
# Software: Visual Studio Code

def time():
    import time
    localtime = time.asctime( time.localtime(time.time()) )
    print ("TIME :", localtime)
