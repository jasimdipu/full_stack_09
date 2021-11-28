from oop_principles_28_11_21 import Student

# model class


class StudentImpl(Student):

    # private__, public, protected_
    # __stu_name = ""

    def __init__(self, stu_id, name, dept) -> None:
        self.__stu_id = stu_id
        self.__stu_name = name
        self.__stu_dept = dept

    def getid(self) -> int:
        return self.__stu_id

    def getname(self) -> str:
        return self.__stu_name

    def getdept(self) -> str:
        return self.__stu_dept

    def setid(self, stu_id):
        self.__stu_id = stu_id

    def setname(self, name):
        self.__stu_name = name

    def setdept(self, dept):
        self.__stu_dept = dept

    def __str__(self) -> str:
        return str(self.__stu_id)+" "+self.__stu_name+" "+self.__stu_dept
