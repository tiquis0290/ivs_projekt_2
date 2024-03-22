"""!
@package calc_mathlib
    Math library for calculator
    Working with float numbers

    #TODO Inputs and results has to be in range \
    <-sys.float_info.max and sys.float_info.max> \
    If not return OverflowError

    #TODO Factorial input and result
"""

def add(a, b):
    """!
    @return a + b
    @exception OverflowError
    """
    pass

def sub(a, b):
    """!
    @return a - b
    @exception OverflowError
    """
    pass


def mul(a, b):
    """!
    @return a * b
    @exception OverflowError
    """
    pass
def div(a, b):
    """!
    @return a/b
    @exception ZeroDivisionError a/0
    @exception OverflowError
    """
    pass

def fac(n):
    """!
    @return n!
    @exception ValueError n not in Z
    @exception OverflowError
    """
    pass

def pow(a, b):
    """!
    @return a ^ b
    @exception ValueError b not in N
    @exception OverflowError
    """
    pass

def root(a, b):
    """!
    @return a ^ (1/b)
    @exception ZeroDivisionError a ^ (1/0)
    @exception ValueError  a < 0 and b
    @exception OverflowError
    """
    pass

def abs(a):
    """!
    @return |a|
    """
    pass