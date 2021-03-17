#A
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def exponent(x):
    ex = 1 + x
    for n in range(2, 100):
        num = x
        for i in range(1, n):
            num *= x
        ex += (num) / factorial(n)
        ex = float('%0.6f' % ex)
    return ex

def abs_n (x):
    if x<0:
        x=-x
    return x

def ln (x) :
    if x <= 0:
        return 0
    y0 = x-1.0
    y_new = 0
    while 0.001 < abs_n(y_new-y0):
        y_new = y0
        y0 = y0+2*((x-exponent(y0))/(x+exponent(y0)))
    return y0

def XtimesY(x,y):
    if x <= 0:
        return 0
    num = 0
    num = exponent(y*ln(x))
    num =float('%0.6f' % num)
    return num
#B
XtimesY(-2,2)

def sqrt(x,y):
    if y<0.0 and x%2.0 == 0.0:
        return 0
    num = 0
    num = XtimesY(y, 1.0/x)
    num = float('%0.6f' % num)
    return num

#sqrt(5,-3)

#C
def calculate (x):
    num = exponent(x)*XtimesY(7,x)*(1/x)*sqrt(x,x)
    num =float('%0.6f' % num)
    return num
