#Write a function that calculates the factorial of a number provided by the user.
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: The non-negative integer to calculate the factorial of.

  Returns:
    The factorial of n.

  Raises:
    ValueError: If n is negative.
  """

  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Get user input
num = int(input("Enter a non-negative integer: "))

# Calculate and print the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")
