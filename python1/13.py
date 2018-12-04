import numpy as n
import random as r

size = 8
M1 = n.matrix('1 2 3 4 1 2 3 4 ; 5 6 7 8 5 6 7 8 ; 9 10 11 12 9 10 11 12; 13 14 15 16 13 14 15 16 ; 1 2 3 4 1 2 3 4 ; 5 6 7 8 5 6 7 8 ; 9 10 11 12 9 10 11 12; 13 14 15 16 13 14 15 16')
M2 = n.matrix('2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2 ; 2 2 2 2 2 2 2 2')
M3 = M1
M3=M1*M2
print("Wynik mnozenia macierzy M1:\n",M1,"\ni M2:\n",M2,"\nwynosi:\n", M3)

