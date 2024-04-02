import math
import random
import matplotlib.pyplot as plt

def calculate_penis_length(human_height_inches, nationality_factor):
    # Assuming human_height = 4 * pi * penis_length
    # Rearranging the equation to solve for penis_length
    # penis_length = human_height / (4 * pi)
    penis_length_inches = human_height_inches / (4 * math.pi)
    
    # Adding some randomness to the result
    # Randomly adjusting the penis length by up to +/- 10%
    random_adjustment = random.uniform(-0.1, 0.1)  # Random value between -0.1 and 0.1
    penis_length_inches *= (1 + random_adjustment)  # Applying the random adjustment
    
    # Adjusting penis length based on nationality factor
    if nationality_factor == 1:  # Asian
        penis_length_inches *= 0.85  # 15% reduction for Asians
    elif nationality_factor == 3:  # African
        penis_length_inches *= 1.2  # 20% increase for Africans
    
    return penis_length_inches

# World's average penis length in inches
world_mean_length_inches = 5.16

# Example usage
user_height_inches = float(input("Enter your height in inches: "))
nationality_factor = int(input("Enter your nationality factor (1 for Asian, 2 for Caucasian, 3 for African): "))

# Calculate penis length
penis_length_inches = calculate_penis_length(user_height_inches, nationality_factor)

# Print the calculated penis length
print("Based on your height and nationality, your penis length is approximately:", round(penis_length_inches, 2), "inches")

# Data for the bar graph
labels = ['World Mean Length', 'Your Calculated Length']
lengths = [world_mean_length_inches, penis_length_inches]

# Plotting the bar graph
plt.bar(labels, lengths, color=['blue', 'green'])
plt.title('Comparison of Penis Lengths')
plt.ylabel('Penis Length (inches)')
plt.show()


