# -*- coding: utf-8 -*-
# Software: Visual Studio Code

import os
import platform
from . import help
from . import gettime
from . import calculator
from . import gettime
from . import coderain
from . import snake
# Windows 和 *nix 系统的清屏
ClearWindow_win = r"cls"
ClearWindow_linux = r"clear"

thisdir = ""

def main():
    # 目录不存在，第一次运行
    if os.path.exists("Data") == False:
        FirstRun()
    
    if platform.system() == "Windows":
        os.system(ClearWindow_win)
    else:
        os.system(ClearWindow_linux)
    
    thisdir = os.getcwd()

    command = ''
    
    while True:
        print(os.getcwd())
        command = input(">>> ")
        
        file = open(thisdir+"/Data/.simpleshrc", "a")
        file.write(command + '\n')
        file.close()

        if command == "help":
            Help(1)
        elif command == "calculator":
            Calc()
        elif command == "time":
            Time()
        elif command == "coderain":
            Coderain()
        elif command == "snake":
            Snake()
        elif command == "quit" or command == "exit":
            break
        elif command == "chdir":
            Changedir()
        else:
            os.system(command)

        

def FirstRun():
    # 确保之后不再运行
    os.mkdir("Data")                # 建立 Data 文件夹
    file = open("Data/.simpleshrc", "w")
    file.close()

    # 简单教程
    # Help(0)


def Help(num):
    help.help(num)


# 简易计算器，支持加减乘除
def Calc():
    calculator.calc()


# 获取当前时间
def Time():
    gettime.time()


# 小游戏：使用 Pygame 实现代码雨 （摘自 https://blog.csdn.net/qq_39687901/article/details/83546363）
def Coderain():
    coderain.rain()


# 小游戏：使用 Pygame 实现贪吃蛇（摘自 https://gitee.com/libao-sir/snake/blob/master/snake_game.py）
def Snake():
    snake.main()

# 更改当前目录
def Changedir():
    path = input("Type the directory that you want to change: ")
    
    try:
        os.chdir(path)
    except Exception as e:
        print("An error occured: ", e)
    
    print("Change path successfully!\n")