import random

class RandomNumberService:
    def __init__(self, min_limit, max_limit):
        self.__min_limit = min_limit
        self.__max_limit = max_limit
        self.random_number = self.set_random_number()

    def set_random_number(self):
        return random.randint(self.__min_limit + 1, self.__max_limit)

    def set_min_limit(self, min_limit):
        self.__min_limit = min_limit

    def get_min_limit(self):
        return self.__min_limit

    def get_max_limit(self):
        return self.__max_limit

    def set_max_limit(self, max_limit):
        self.__max_limit = max_limit

    def is_predict_number(self, number):
        return self.random_number == number

    def according_number_to_limits(self, number):
        if self.__min_limit <= number < self.random_number:
            self.set_min_limit(number)
        elif self.random_number < number <= self.__max_limit:
            self.set_max_limit(number)
        return self.get_min_limit(), self.get_max_limit()

