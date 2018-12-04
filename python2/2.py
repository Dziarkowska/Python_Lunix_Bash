
class ComplexNumber:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def __add__(self, other):
        return ComplexNumber(other.real + self.real, other.imag + self.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"
z1 = ComplexNumber(-8,7)
z2 = ComplexNumber(4,-1)
print("z1 = ",z1)
print("z2 = ",z2)
print("z1 + z2 = ",z1 + z2)
