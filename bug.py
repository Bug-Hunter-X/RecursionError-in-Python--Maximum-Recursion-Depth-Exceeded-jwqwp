def my_function(x):
    if x == 0:
        return 0
    else:
        return x + my_function(x-1)

print(my_function(5)) # This works fine
print(my_function(1000)) # This will cause a RecursionError