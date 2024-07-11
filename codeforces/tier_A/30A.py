import math

a, b, n= map(int, input().split())

X=10 ** (abs((math.log10(abs(b)) - math.log10(abs(a)))) / n)

print(-1 * round(X) if a * b < 0 else round(X))
