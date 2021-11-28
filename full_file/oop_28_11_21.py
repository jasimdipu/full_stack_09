class Student:
    # class properties -> attributes(global variable, local variable), functions(build, custom)

    # global variable | instance | class properties
    stu_name = ""
    stu_dept = ""

    # constructor
    def __init__(self, name, dept):
        self.stu_name = name
        self.stu_dept = dept

    def get_name(self):
        return self.stu_name

    def get_dept(self):
        return self.stu_dept

    def __str__(self):
        return self.stu_name+" "+self.stu_dept
    

# create an object

student = Student("Student1", "CSE")

print(student)
student.stu_name = "Habib"
print(student.stu_name)

# print(student.get_name())
# print(student.get_dept())





