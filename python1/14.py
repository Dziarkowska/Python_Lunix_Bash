
import random as r
import numpy as n

m_size = r.randint(2,10)
#M1 = n.random.random((size, size))
M1 = n.random.randint(11, size=(m_size, m_size))
M = n.matrix(M1)

print("\nProgram generuje losowo rozmiar macierzy z przedzialu (2;10) oraz jej zawartosc\n z przedzialu (0;10) i oblicza jej wyznacznik\n")
print("Macierz M:\n", M)
print("\n wyznacznik macierzy M:\n")
print(n.linalg.det(M))
