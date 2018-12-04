
import math as m

def quadratic_fun(a,b,c):
	delta = b*b - 4*a*c
	if delta > 0:
		x1 = (-b-m.sqrt(delta))/2*a
		x2 = (-b+m.sqrt(delta))/2*a
		print("Rownanie ma dwa pierwiastki:\n",x1,"\n", x2)
	elif delta == 0:
		x1 = -b/2*a
		print("Rownanie ma jeden podwojny pierwiastek:\n",x1)
	elif delta <0:
		print("Rownanie nie ma rozwiazan w dziedzinie liczb rzeczywistych")

def main():
	a, b, c = input("Podaj wspolczynniki f.kwadratowej a b c:\n").split()
	quadratic_fun(int(a), int(b), int(c))

main()
