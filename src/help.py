# -*- coding: utf-8 -*-
# Software: Visual Studio Code

def help(num):
    if num == 0:
        print("This is the help file of the program: ")
    else:
        print("Help file: ")
    
    # BEGIN HELP FILE
    print("-"*30)
    print("Builtin Commands: ")
    print("help\t\t view the help file.")
    print("time\t\t get the current time.")
    print("calc\t\t a simple calculator.")
    print("chdir\t\t change current directory")
    print("coderain\t GAME: display code rain.(Need pygame)")
    print("snake\t\t GAME: greedy snake.(Need pygame)")
    print("-"*30)
    print("You can also use system commands.")
    print("NOTE: You should't use system command \"cd\", it does not effect. Use CHDIR to instead.")
    print("-"*30)
    print("If there's a bug, you can go to Github/Gitee to report issue.")
    print("-"*30)
    print()