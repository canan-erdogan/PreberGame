from Service.random_number_service import RandomNumberService


class RandomNumberViewmodel:
    def __init__(self, min_limit, max_limit, predict_number=None):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.predict_number = predict_number
        self.random_service = None
        self.start_game(self.min_limit, self.max_limit)

    def start_game(self, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.random_service = RandomNumberService(int(min_limit), int(max_limit))

    def forward_game(self, predict_number):
        if self.random_service.is_predict_number(predict_number):
            return None
        else:
            return self.random_service.according_number_to_limits(predict_number)

