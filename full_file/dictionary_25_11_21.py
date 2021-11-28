# key value pair
d = {"key1":"value1", "key2":"value2", "key3":"value3", 0: 10, 1:200}
# print(d)

# print(d["key1"])
# print(d["key3"])


for i, j in d.items():
    print(i, j)

print(d.keys())
print(d.values())
d[1] = 300
print(d[1])