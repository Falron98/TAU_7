

class Car:
    def __init__(self, year, model):
        self.__year = year
        self.__model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if 0 < self.__speed <= 5:
            self.__speed = 0
        elif self.__speed > 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed


