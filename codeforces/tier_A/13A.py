from fractions import Fraction

def convert_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1]

n = int(input())

numbers = []
digit_sums = []
grand_digit_sum = 0

# Calculate sums of digits in different bases
for i in range(2, n):
    base_repr = convert_to_base(n, i)
    digit_sums.append(sum(base_repr))
    grand_digit_sum += sum(base_repr)

average_digit_sum = grand_digit_sum / (n - 2)  # n-2 bases from 2 to n-1

fraction = Fraction(average_digit_sum).limit_denominator()

print(f"{fraction.numerator}/{fraction.denominator}")