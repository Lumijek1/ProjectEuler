import time
import math
from myfunctions import isSquare

def pentagonal(n):
    return int(n*(3*n - 1) / 2)
z = []
for i in range(-1, -300, -1):
	z.append(pentagonal(abs(i)))
	z.append(pentagonal(i))

part = [1, 1]
start = time.time()
for i in range(2, 100000):
	print(i)
	n = 0
	t = 0
	while i >= z[n]:
		if n % 4 <= 1:
			t += part[i - z[n]]
		elif n % 4 >= 2:
			t -= part[i- z[n]]
		n += 1
	if t % 1000000 == 0:
		print("FOUND. N is:", i)
		break
	part.append(t)
print(time.time()-start)
