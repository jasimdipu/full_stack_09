# datatype, variable, condition, loops

char = 'b'
string_ = "ball"
int_num = 20
float_num = 5.5

# phone = 0173457329

print(char, string_, int_num, float_num)

# 1430028531760 1430028390640 1430026212816 1430030160848
print(id(char), id(string_), id(int_num), id(float_num))

# condition

if 100 < 2:
    print("True")
else:
    print('False')

name = "Forhad"

if name == "Tanvir":
    print("Welcome Tanvir")
else:
    print("Do i know you?")

# for, while

# for i in range(10): # n-1
#     print(i)
num = 0
for i in range(10):
    num = num * 2
    num += 2
print(num)




# while

i = 0
n = 10

while i < n:
    print(i)
    i = i+1

for i in range(0, 20, 3):
    print(i)