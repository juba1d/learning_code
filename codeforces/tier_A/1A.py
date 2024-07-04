#so_simple

n,m,a=map(int,input().split())

count_x=(n+a-1)//a
count_y=(m+a-1)//a

print(count_x*count_y)