# print(100/10)
# try:
#     print(100/0)
# except ValueError as e:
#     print(e)
# finally:
#     print("Finally block for final decission")
# print(100/20)

class SmallNumberException(Exception):
    pass


class BigNumberException(Exception):
    pass


def takeNumber():
    try:
        number = int(input("Enter a number: "))
        if number > 90:
            raise BigNumberException
        if number < 10:
            raise SmallNumberException

        print(100/number)

    except BigNumberException as e:
        print(e, "Please enter number smaller then 90.")
        takeNumber()
    except SmallNumberException as e:
        print(e, "Please enter number bigger then 10.")
        takeNumber()
    except Exception as e:
        print(e)
        takeNumber()


takeNumber()