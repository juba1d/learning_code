n = int(input())
 
capacity = 0
current = 0
 
for _ in range(n):
    a, b = map(int, input().split())
        
    current -= a
    current += b
        
    if current > capacity:
        capacity = current
    
print(capacity)