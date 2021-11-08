from fractions import Fraction
import math
import numpy as np
"""
We want to find \sum_{i=1}^n i^d. This is equal to P(n) then P(n)-P(n-1)=n^d.
Assign polynomials to things and do what we want
"""
"""
#Test
with open("data.txt",'w') as f:
    f.write("[Fraction(0,1),Fraction(1,1)]")
with open("formatted.txt","w") as f:
    f.write("\\[\\sum_{k=1}^xk^0=x\\]")
"""

class Polynomial:
    def __init__(self,coefficients=[]):
        """
        self.coefficients is labeled from 0; self.coefficients[0] is x^0 coefficient
        """
        self.coefficients = coefficients

    def subtract(self,polynomial):
        subtracted = np.array(polynomial.coefficients)
        for r in range(len(self.coefficients) - len(subtracted)):
            subtracted = np.append(subtracted,0)
        self.coefficients -= subtracted

def main(d):
    P_poly = []
    # where rhs_poly is n^d-(P(n)-P(n-1))
    rhs_poly = Polynomial(np.array([Fraction(0,1)]*d+[Fraction(1,1)]))

    pascals = []
    for r in range(d+3):
        newline = [0]*(r+1)
        for k in range(r+1):
            if k == 0 or k == r:
                newline[k]=Fraction(1,1)
            else:
                newline[k]=pascals[-1][k]+pascals[-1][k-1]
        pascals.append(newline)

    # subt_polys[i]=n^i-(n-1)^i, for d from 0 to (d+1)
    subt_polys = []
    for i in range(d+2):
        newarrcoeff = np.array([0]*i)
        for deg in range(i):
            newarrcoeff[deg]=(-1)**(deg-i+1)*pascals[i][deg]
        subt_polys.append(Polynomial(newarrcoeff))

    for r in range(d+1):
        deg = d-r
        #basically find the amount we need to subtract from the rhs to make that coeff go away, then add that coeff in P, then subt
        #deg is the degree in rhs that we're fixing
        newval = rhs_poly.coefficients[deg]/(deg+1)
        P_poly.insert(0,Fraction(newval))
        rhs_poly.subtract(Polynomial(newval*(subt_polys[deg+1].coefficients)))
    return [0]+P_poly

def my_output(polynomial):
    with open("data.txt", 'a') as fout:
        fout.write("\n"+str(polynomial))
        #print("\n"+str(polynomial))
        
    with open("formatted.txt", 'a') as fout:
        written = ""
        for index in range(len(polynomial)):
            if polynomial[index] < 0:
                if polynomial[index].numerator == -1:
                    num = ""
                else:
                    num = str(-polynomial[index].numerator)
                written += " - \\frac{" + num + "x^{" + str(index) + "}}{" + str(polynomial[index].denominator) + "}"
            elif polynomial[index] > 0:
                if polynomial[index].numerator == 1:
                    num = ""
                else:
                    num = str(polynomial[index].numerator)
                written += " + \\frac{" + num + "x^{" + str(index) + "}}{" + str(polynomial[index].denominator) + "}"
        fout.write("\n\\[\\sum_{k=1}^x k^{" + str(len(polynomial)-2) + "}=" + written[2:]+"\\]")

my_output(main(int(input())))