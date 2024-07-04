def lucky(n):
    # Check if all characters in n are either '4' or '7'
    for char in n:
        if char != '4' and char != '7':
            return False
    return True

n = int(input())
a = input().strip()

# Check if the ticket number is lucky
if lucky(a):
    half_length = n // 2
    x = list(map(int, a[:half_length]))
    y = list(map(int, a[half_length:]))

    # Check if the sum of digits in the first half equals the sum of digits in the second half
    if sum(x) == sum(y):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
