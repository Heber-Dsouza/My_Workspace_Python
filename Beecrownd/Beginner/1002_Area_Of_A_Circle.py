# -*- coding: utf-8 -*-

def Calc_Circle_Area(r):
    _PI = 3.14159
    return _PI * (r**2)

r_Value = float(input())

print('A={:.4f}'.format(round(Calc_Circle_Area(r_Value), 4)))     

# see more information at:
#   https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points