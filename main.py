

class Employee:
    def __init__(self, __lastname, __firstname):
        if isinstance(__firstname, str) != True or isinstance(__lastname, str) != True:
            raise Exception("Wrong input")
        self.__lastname = __lastname
        self.__firstname = __firstname

    def get_lastname(self):
        return self.__lastname

    def get_firstname(self):
        return self.__firstname

    def set_lastname(self, __lastname):
        if isinstance(__lastname, str):
            self.__lastname = __lastname
        else:
            raise Exception("Wrong input")

    def set_firstname(self, __firstname):
        if isinstance(__firstname, str):
            self.__firstname = __firstname
        else:
            raise Exception("Wrong input")


class ProductionWorker(Employee):

    def __init__(self, __lastname, __firstname, __change_number, __pay_hour):
        if isinstance(__change_number, int) is not True or \
                isinstance(__pay_hour, int) is not True:
            raise Exception("Wrong input")
        elif __change_number < 0 or __change_number > 2:
            raise Exception("Change number can be only 1 or 2")
        elif __pay_hour <= 0:
            raise Exception("Pay hour must be greater than 0")
        try:
            super().__init__(__lastname, __firstname)
            self.__change_number = __change_number
            self.__pay_hour = __pay_hour
        except:
            raise Exception

    def get_change_number(self):
        return self.__change_number

    def get_pay_hour(self):
        return self.__pay_hour

    def set_change_number(self, __change_number):
        if isinstance(__change_number, int) and 0 < __change_number <= 2:
            self.__change_number = __change_number
        else:
            raise Exception("Wrong input")

    def set_pay_hour(self, __pay_hour):
        if isinstance(__pay_hour, int) and __pay_hour > 0:
            self.__pay_hour = __pay_hour
        else:
            raise Exception("Wrong input")