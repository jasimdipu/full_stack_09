# opp principles -> abstraction, encapsulation, inheritance, polymorphism
from abc import ABC, abstractmethod

# abstract class


class Student(ABC):

    # function name-> no logic

    @abstractmethod
    def getid(self) -> int:
        pass

    @abstractmethod
    def getname(self) -> str:
        pass

    @abstractmethod
    def getdept(self) -> str:
        pass

    @abstractmethod
    def setid(self, stu_id):
        pass

    @abstractmethod
    def setname(self, name):
        pass


    @abstractmethod
    def setdept(self, dept):
        pass
