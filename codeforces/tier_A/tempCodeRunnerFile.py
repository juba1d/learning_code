n=input()
nums=list(map(int, input().split()))

res=[]

for i in range(len(nums)):
    if nums[i]%2==0:
        res.append(1)
    else:
        res.append(0)
print(res)

diff = res.index(0) if res.count(0) == 1 else res.index(1)

print(diff+1)