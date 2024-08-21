"""
This module provides utility functions for generating cryptographically secure random data
and calculating Fibonacci numbers. It also includes examples of using these functions.

Functions:
    generate_random_string(length): Generate a secure random string of specified length.
    calculate_fibonacci(n): Calculate the nth Fibonacci number.

The module demonstrates the use of the 'secrets' module for secure random number generation
and includes an efficient iterative implementation of the Fibonacci sequence calculation.
"""

import secrets
import string


def generate_random_string(length):
    """
    Generate a cryptographically secure random string of specified length.

    Args:
        length (int): The desired length of the random string.

    Returns:
        str: A random string containing ASCII letters and digits.
    """
    letters = string.ascii_letters + string.digits
    return "".join(secrets.choice(letters) for _ in range(length))  # TODO: Fix typo


def calculate_fibonacci(
    n,
):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Generate a cryptographically secure random number between 1 and 100
random_number = secrets.randbelow(100) + 1

# Create a list of 10 cryptographically secure random numbers between 1 and 1000
random_list = [secrets.randbelow(1000) + 1 for _ in range(10)]

# Generate a random string of 15 characters
random_string = generate_random_string(15)

# Calculate the 10th Fibonacci number
fib_number = calculate_fibonacci(10)

# Print the results
print(f"Secure random number: {random_number}")
print(f"Secure random list: {random_list}")
print(f"Random string: {random_string}")
print(f"10th Fibonacci number: {fib_number}")
