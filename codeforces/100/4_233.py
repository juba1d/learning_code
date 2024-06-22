"""must understand p[p[i]]=i concept, then why odd mapping fails, 
finally why switching positions helps"""


def perfect_permutation(n):
    if n % 2 != 0:
        return [-1]
    else:
        permutation = list(range(1, n + 1))
        for i in range(0, n, 2):        #2 added to skip 2 already worked elements
            permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]
        return permutation

n = int(input())

result = perfect_permutation(n)

if result == [-1]:
    print(-1)
else:
    print(' '.join(map(str, result)))

