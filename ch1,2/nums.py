from fractions import Fraction

a = Fraction(2, 8)
b = 1
c = 3.6
x = complex(b, c)
y = 4 + 7j

nums = [a, b, c, x, y]

for num in nums:
    print(num)

# Working with fractions
print(" ")
print( a + b )
print( a + b + c, "\n" )

# Working with complex numbers
print( x + y)
print( b + x)
print(a + y,"\n")

# Complex number methods
print(x.real, '+', x.imag, "i", sep="")
print(x.conjugate())
x_mag = (x.real**2 + x.imag**2)**(1/2)
print(x_mag)
print(abs(x))