n=input()

nums=set(map(int,input().split()))

nums=list(nums)

nums.sort()

if len(nums)>1:
    print(nums[1])
else:
    print("NO")

