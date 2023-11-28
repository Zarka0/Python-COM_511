# Create a function Max_of_three that takes three numbers as argument and return the largest of them and also create an parameter function that check whether a given number is armstrong or not


def max_of_three(a, b, c):
    """
    Returns the largest of three numbers.
    """
    return max(a, b, c)

def is_armstrong_number(number):
    """
    Checks if the given number is an Armstrong number.
    """
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
max_value = max_of_three(a, b, c)
print(f"The maximum of {a}, {b}, and {c} is: {max_value}")
armstrong_number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(armstrong_number):
    print(f"{armstrong_number} is an Armstrong number.")
else:
    print(f"{armstrong_number} is not an Armstrong number.")