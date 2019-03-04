# itertools.product()

from itertools import product

a  = map(int,input().strip().split())
b  = map(int,input().strip().split())

a = list(a)
b = list(b)

rez = list(product(a, b))
print(' '.join(map(str,rez)))