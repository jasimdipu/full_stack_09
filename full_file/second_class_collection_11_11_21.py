# Collections -> list

l = []  # create an empty list

print(type(l))

l = [1, 2, 3, 4.5, 5.5, 6.5, "seven", 'eight', 'nine', True, False]

print(l)

# indexing

print(l[0])
print(l[3])
print(l[7])
print(l[9])
print(type(l[0]))
print(type(l[5]))
print(type(l[7]))
print(type(l[9]))
print(len(l))  # index = len-1
print(l[10])

# slicing

print(l[1:5])
print(l[::-1])

# nested

l2 = [[1, [2.2, 2.5, 2.8], 3], [4, 5, 6], [7, 8, 9]]

print(l2[0][1][0])

# basic functions

l2.append([100, 200, 300])
l3 = l+l2
print(l2)
print(l3)
l2.reverse()
print(l2)

l2.sort()
print(l2)