


"""
# Take input from the user
user_input = input("Enter a string: ")

# Initialize a counter for digits '4' and '7'
count = 0

# Iterate over each character in the input string
for char in user_input:
    # Check if the character is '4' or '7'
    if char == '4' or char == '7':
        # Increment the counter if the character is '4' or '7'
        count += 1

# Check if the count is either 4 or 7
if count == 4 or count == 7:
    # Print 'YES' if the count is 4 or 7
    print('YES')
else:
    # Print 'NO' if the count is not 4 or 7
    print('NO')
"""

print('YES' if sum(i in '47' for i in input()) in [4, 7] else 'NO')
