# set is a collection, immutable and non indexing collection
s = {10, 20, 20, 30, 30, 30, 40, 50, 50}

print(type(s))

print(s)

# print(s[0])

s2 = {29, 40, 10, 57, 38, 40, 40}

print(s.union(s2))

print(s.intersection(s2))

print(s.issubset(s2))
s3 = {29, 10}
print(s3.issubset(s2))

print(s.symmetric_difference(s2))
s.update(s3)
print(s)

s.add(200)
print(s)

