a = list(input().strip())

cleaned_path = []
previous_char = None

for char in a:
    if char != '/' or (char == '/' and previous_char != '/'):
        cleaned_path.append(char)
    previous_char = char

output_path = ''.join(cleaned_path)

if output_path.endswith('/') and len(output_path) > 1:
    output_path = output_path[:-1]

print(output_path)
