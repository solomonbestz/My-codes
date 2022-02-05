from bestz_decorator import bestz_print
import math

def bestz_sqrt(value):
    xo = value
    xn = value
    while True:
        ans = ((xn +(xo / xn))/ 2)
        xn = ans
        if ans % 2 == 0:
            break
    return xn

def power(base, length):
    return [base**i for i in range(1, length+1)]


bestz_print(bestz_sqrt(100))
bestz_print(power(2, 5))


