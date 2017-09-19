# to determine if a function is callable you used the __callable__()

def is_even(x):
    return x % 2 == 0
print(callable(is_even))

#strings are not callabe