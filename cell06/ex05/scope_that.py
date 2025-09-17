def add_one(x):
    return x + 1

a = 5
print("Before:", a)

add_one(a)
print("After calling add_one:", a)

a = add_one(a)
print("After assigning result:", a)
