from operators import *

def calc(a,b, operator):
    result = 0
    if operator == '+':
        result = plus(float(a), float(b))
    elif operator == '-':
        result = minus(float(a), float(b))
    elif operator == '*':
        result = multiply(float(a), float(b))
    elif operator == '/':
        result = div(float(a), float(b))
    return result