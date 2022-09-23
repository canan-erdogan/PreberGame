from Model.predict_model import PredictModel
from Service.predict_service import PredictService


class PredictViewmodel:
    def __init__(self):
        self.predicts= []
        self.set_predicts_from_csv()

    def set_predicts_from_csv(self):
        for row in PredictService.read_predict_from_csv():
            self.predicts.append(PredictModel(int(row["predict_number"]), int(row["predict_count"]), int(row["predict_limit"])))

    def append_predict_to_predicts(self, predict_number, predict_count, predict_limit):
        predict = PredictModel(int(predict_number), int(predict_count), int(predict_limit))
        self.predicts.append(predict)
        PredictService(predict.predict_number, predict.predict_count, predict.predict_limit)


