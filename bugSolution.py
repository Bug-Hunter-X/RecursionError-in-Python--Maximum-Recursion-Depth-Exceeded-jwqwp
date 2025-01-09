def my_function_iterative(x):
    result = 0
    for i in range(x + 1):
        result += i
    return result

print(my_function_iterative(5))  # Output: 15
print(my_function_iterative(1000)) # Output: 500500