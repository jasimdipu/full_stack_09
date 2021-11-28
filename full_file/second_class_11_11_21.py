# Strings


str_var = 'hello'
str_val_2 = "this is also a string"

# print(str_var, type(str_var))
# print(str_val_2, type(str_val_2))


# we don't use this kind of string text = 'it's an string type'

s = "hello"

print(s)

# indexing

print(s[0]+s[1]+s[2]+s[3]+s[4])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])

for i in s:
    print(i, end="")
print()

# slicing
print(s[:4])  # start point - end point -1
print(s[-4:-2])

print(s[::-1])
print(s[::2])

# build in function

print(s.upper())

print(s.lower())

s2 = "Hello Python Coders"
s3 = "Hello-Python-Coders"

print(s2.split())
print(s3.split("-"))
print(s2.split("e"))

print(s2.count("o"))
print(s2.find("o"))

print(s.center(30, '@'))

s = s+"\thi"
print(s.expandtabs())

