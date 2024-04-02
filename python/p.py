import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

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
        penis_length_inches *= 0.9  # 10% reduction for Asians
    elif nationality_factor == 3:  # African
        penis_length_inches *= 1.1  # 10% increase for Africans
    
    return penis_length_inches

# Example usage
user_height_inches = float(input("Enter your height in inches: "))
nationality_factor = int(input("Enter your nationality factor (1 for Asian, 2 for Caucasian, 3 for African): "))

# Calculate penis length
penis_length_inches = calculate_penis_length(user_height_inches, nationality_factor)

# Calculate z-score
mean = 0
std_dev = 1
z_score = (penis_length_inches - mean) / std_dev

# Plot bell curve
x = np.linspace(-3, 3, 100)
plt.plot(x, norm.pdf(x, mean, std_dev))
plt.fill_between(x, norm.pdf(x, mean, std_dev), where=(x >= z_score), color="skyblue", alpha=0.5)
plt.title('Bell Curve of Penis Length (Z-score)')
plt.xlabel('Z-score')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

# Print the calculated penis length and z-score
print("Based on your height and nationality, your penis length is approximately:", round(penis_length_inches, 2), "inches")
print("The corresponding z-score of the penis length is:", round(z_score, 2))
