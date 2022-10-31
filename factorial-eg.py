def factorial(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result

var = factorial(5)
print(f"The factorial of 5 is", var)