# Read the input string
s = input().strip()

# Initialize counters
cnts = 0
cntb = 0

# Count lowercase and uppercase characters
for char in s:
    if 'a' <= char <= 'z':
        cnts += 1
    else:
        cntb += 1

# Determine whether to convert to lowercase or uppercase
if cnts >= cntb:
    # Convert to lowercase
    s = s.lower()
else:
    # Convert to uppercase
    s = s.upper()

# Print the result
print(s)
