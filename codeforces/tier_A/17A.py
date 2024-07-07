def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n,k=map(int, input().split())

print(n,k)

primes = [i for i in range(2, n+1) if is_prime(i)]

noldbach_primes = []

for i in range(len(primes) - 1):
    possible_prime = primes[i] + primes[i+1] + 1
    if possible_prime <= n and is_prime(possible_prime):
        noldbach_primes.append(possible_prime)
        
if len(noldbach_primes) >= k:
    print("YES")
else:
    print("NO")