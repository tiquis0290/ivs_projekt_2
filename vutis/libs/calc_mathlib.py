import sys

"""!
@package calc_mathlib
    Math library for calculator
    Working with float numbers

    #TODO Inputs and results has to be in range \
    <-sys.float_info.max and sys.float_info.max> \
    If not return OverflowError

    #TODO Factorial input and result
"""


## @return a + b
#  @exception OverflowError

def add(a, b):
    result = a + b
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result


##  @return a - b
# @exception OverflowError
def sub(a, b):
    result = a - b
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result


##@return a * b
# @exception OverflowError
def mul(a, b):
    result = a * b
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result


## @return a/b
# @exception ZeroDivisionError a/0
# @exception OverflowError
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not possible")
    result = a / b
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result


## @return n!
# @exception ValueError n not in Z
# @exception OverflowError
def fac(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Factorial is defined only for non-negative integers")
    if n == 0:
        return 1

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    if factorial > sys.float_info.max:
        raise OverflowError("Result is out of range for float")

    return factorial

##  @return a ^ b
# @exception ValueError b not in N
# @exception OverflowError
def pow(a, b):
    result = a ** b
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result

## @return a ^ (1/b)
# @exception ZeroDivisionError a ^ (1/0)
# @exception ValueError  a < 0 and b
# @exception OverflowError
def root(a, b):
    if b % 2 == 0 and a < 0:
        raise ValueError("Value of root has to be greater than 0")
    if b == 0:
        raise ValueError("B value of root can't be zero")
    if a < 0 and b % 2 != 0:
        result = -((-a) ** (1 / b))
    else:
        result = (a ** (1 / b))
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result

## @return |a|
# @exception OverflowError
def abs(a):
    if a < 0:
        result = a * -1
    else: 
        result = a
    if result > sys.float_info.max or result < -sys.float_info.max:
        raise OverflowError("Result is out of range for float")
    return result
