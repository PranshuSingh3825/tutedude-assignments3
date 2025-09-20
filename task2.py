import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Perform calculations using math module
square_root = math.sqrt(num)
logarithm = math.log(num)      # natural log (base e)
sine = math.sin(num)           # sine in radians

# Display results in the same style
print("Square root:", square_root)
print("Logarithm:", logarithm)
print("Sine:", sine)