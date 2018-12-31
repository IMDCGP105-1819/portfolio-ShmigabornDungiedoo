class Fraction:

    def __init__(self, num1, denom1, num2, denom2):
        self.num1=num1
        self.denom1=denom1
        self.num2=num2
        self.denom2 =denom2

    def addition(self):
        numtot=self.num1 * self.denom2 + self.num2 * self.denom1
        denomtot= self.denom1 * self.denom2
        print( str(numtot)+ "/"+str(denomtot) )

    def subtraction(self):
        numtot=self.num1 * self.denom2 - self.num2 * self.denom1
        denomtot=self.denom1 * self.denom2
        print( str(numtot)+ "/"+str(denomtot) )

    def multiplication(self):
        numtot= self.num1 * self.num2
        denomtot= self.denom1 * self.denom2
        print( str(numtot)+ "/"+str(denomtot) )

    def division(self):
        numtot= self.num1*self.denom2
        denomtot=self.denom1*self.num2
        print( str(numtot)+ "/"+str(denomtot) )

    def inverse(self):
        n1=self.num1
        d1=self.denom1
        n2=self.num2
        d2=self.denom2
        print(str(d1)+"/"+str(n1) + "  "+ str(d2)+"/"+ str(n2))

fnum1=int(input("Please state numerator of the first fraction.     "))
fdenom1=int(input("Please state denomimator of the first fraction.     "))
fnum2=int(input("Please state numerator of the second fraction.     "))
fdenom2=int(input("Please state denominator of the second fraction.     "))
f1=Fraction(fnum1, fdenom1, fnum2, fdenom2)
print("addition")
f1.addition()
print("subtraction")
f1.subtraction()
print("multiplication")
f1.multiplication()
print("division")
f1.division()
print("inverse")
f1.inverse()
