def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
num = int(input("Enter a number: "))

# Calculating factorial
fact = factorial(num)

# Printing the result
print(f"Factorial of {num} is: {fact}") 