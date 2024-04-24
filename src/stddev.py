from libs.calc_mathlib import *

#
#            ________________________
#           / 1
#   s =    /----- SUM ( Xi^2 -N*x_^2 )
#        \/ N -1
#

def s(n, sumx2, x_):
    return root(mul(div(1,sub(n,1)),sub(sumx2,pow(x_, 2))),2)

def px(n, sumx):
    return div(sumx, n)

def calculate():
    n = 0
    sumx = 0
    sumx2 = 0
    try:
        while True:
            string = input()
            string = string.split()
            for number in string:
                number = int(number)
                n = add(n, 1)
                sumx = add(sumx, number)
                sumx2 = add(sumx2, pow(number,2))
    except EOFError:
        pass
    x_ = px(n, sumx)
    return s(n, sumx2, x_)
