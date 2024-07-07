id = list(input().split("@"))

pre = list(id[0].strip())
poss = list(id[1].strip().split("/"))
hostname = list(poss[0].strip())
if (len(poss) > 1): resource = list(poss[1].strip())
else: resource = ['a', 'b', 'c']

result = "YES"

if len(poss) > 2:
    result = "NO"

if not (1 < len(pre) < 16 and 1 < len(hostname) < 16 and 1 < len(resource) < 16):
    result = "NO"

def is_valid_string(s):
    return all(char.isalnum() or char == "_" or char == "." for char in s)

if not is_valid_string(pre) or not is_valid_string(hostname) or not is_valid_string(resource):
    result = "NO"

print(result)
