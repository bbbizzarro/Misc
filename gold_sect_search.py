#!/usr/bin/env python

from sympy import pretty_print as pp, latex
import math
import matplotlib.pyplot as plt

# General function generator for polynomial
class Polynomial:

    def __init__(self, coeff_array):
        self.coeff = coeff_array 
        self.value = 0
        self.string = self.string_form()

    def __repr__(self):
        return self.string
    def __str__(self):
        return self.string
    
    def string_form(self):
        unicode_sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        str_repr_arr = []
        for exponent, coeff in enumerate(self.coeff):
            if coeff == 0:
                str_repr = ""
            elif exponent == 0:
                str_repr = "{} + ".format(coeff)
            elif coeff == 1 and exponent ==0:
                str_repr = "𝓍 + "
            elif coeff == 1 and exponent:
                str_repr = "𝓍{} + ".format(str(exponent).translate(unicode_sup))
            elif coeff == -1:
                str_repr = "-𝓍 + "
            elif exponent == 1:
                str_repr = "{}𝓍 + ".format(coeff)
            else:
                str_repr = "{}𝓍{} + ".format(coeff, str(exponent).translate(unicode_sup))
            str_repr_arr.append(str_repr)
        str_repr_arr = "".join(str_repr_arr)
        if str_repr_arr[-2:] == "+ ":
            str_repr_arr = str_repr_arr[:-3]

        
        return "𝐏(𝓍) = " + "".join(str_repr_arr)

    def evaluate(self, x_in):

        # Generate progressively larger exponentials.
        for exponent, coeff in enumerate(self.coeff):
            self.value += coeff * pow(x_in, exponent)

        return self.value

def main():
    #poly = Polynomial([1,-1,0,3, 0, 1, 9, 100])
    poly = Polynomial([-1, 0, 0, 1])
    print(poly)

    return

#-------------------------
if __name__ == "__main__":
    main()
