#so_simple

n,m,a=map(int,input().split())

count_x=(n // a) + (1 if n % a != 0 else 0)
count_y=(m // a) + (1 if n % a != 0 else 0)

print(count_x*count_y)