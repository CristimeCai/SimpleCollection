# -*- coding: utf-8 -*-
# Software: Visual Studio Code

x = ""
y = ""
oper = ""

def calc():
    print("ConsoleCalc: ")
    try:
        getInput()
        ans = work()
        print("The answer is: ", ans)
    
    except Exception as error:
        print("An error occured: ", error)
        return


def getInput():
    global x, y, oper

    x = input("Input the first number: ")
    y = input("Input the second number: ")
    oper = input("Input the operator(+-*/%^):  ")

    while not(is_number(x)) or not(is_number(y)):
        print("Please enter two number! ")

        x = input("Input the first number: ")
        y = input("Input the second number: ")
        oper = input("Input the operator(+-*/%^):  ")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False




def work():
    global x, y, oper

    if oper == "+":
        return float(x) + float(y)
    
    elif oper == "-":
        return float(x) - float(y)
    
    elif oper == "*":
        return float(x) * float(y)
    
    elif oper == "/":
        return float(x) / float(y)
    
    elif oper == "%":
        return int(x) % int(y)
    
    elif oper == "^":
        return float(x) ** int(y)
    
    else:
        raise Exception('Undefined operator!')