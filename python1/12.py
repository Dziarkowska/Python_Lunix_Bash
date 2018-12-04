import random as r

size = 128
M1 = [[0 for i in range(size)] for j in range(size)]
M2 = M1
M3 = M1

for i in range(size):
	for j in range(size):
		M1[i][j] = r.randint(-100,100)
		M2[i][j] = r.randint(-100,100)

for i in range(size):
	for j in range(size):
		M3[i][j] = M1[i][j] + M2[i][j]

