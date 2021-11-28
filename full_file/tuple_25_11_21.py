# tuple -> immutable collection

t = () # create a tuple

print(type(t))

t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(t)

# index 
print(t[0])
print(t[3])
print(t[4])


# slicing
print(t[:7:2])

# t[0] = 100

# tuple build function 2

print(t.index(1))
print(t.count(2))