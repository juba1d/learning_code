pailam=(input().split(' '))

n=int(pailam[0])
m=int(pailam[1])

def count_pairs(n, m):
    answer = 0
    a = 0
    while a * a <= n and a <= m:
        b = n - a * a
        if a + b * b == m:
            answer += 1
        a += 1
    return answer


result = count_pairs(n, m)

print(result)
