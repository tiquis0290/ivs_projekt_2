from libs.calc_mathlib import *


def calculate(text):
    return operation(text)


def operation(a):
    print(a)
    #a=absolute(a)
    a=brecket(a)

    #a=multipledivide(a)
    #a=plusminus(a)
    return a


def absolute(a):
    while "|(" in a:
        x=a.rfind("|(")+1
        y=x+a[x:len(a)+1].find(")|")-1
        b=a[x:y+1]
        c=operation(a[x+1:y])
        c=abs(c)
        a=a.replace(b,c)
    return a


def brecket(a):
    while "(" in a:
        x=a.rfind("(")
        y=x+a[x:].find(")")
        b=a[x:y+1]
        c=operation(a[x+1:y])
        a=a[:x] + str(c) + a[y+1:]
    return a
