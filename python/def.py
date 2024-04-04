def greet(name):
    print("Hello, " + name + "!")

greet("Alice")


my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing elements
my_list.append(6)  # Adding elements


my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # Accessing values
my_dict["city"] = "New York"  # Adding new key-value pairs


def is_perfect_number(num):
    # Check if the number is positive
    if num <= 0:
        return False
    
    # Find divisors and calculate their sum
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    
    # Check if the sum of divisors equals the number
    return divisor_sum == num

# Test the function

number = int(input("Enter a number: "))
print(is_perfect_number(number))


if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")



word = input("Enter a word: ")

print("Letters of the word:")
for letter in word:
    print(letter)
