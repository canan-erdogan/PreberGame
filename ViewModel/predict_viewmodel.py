from Model.predict_model import PredictModel
from Service.predict_service import PredictService


class PredictViewmodel:
    def __init__(self):
        self.predicts= []
        self.set_predicts_from_csv()

    def set_predicts_from_csv(self):
        for row in PredictService.read_predict_from_csv():
            self.predicts.append(PredictModel(row["predict_number"], row["predict_count"]))

    def append_predict_to_predicts(self, predict_number, predict_count):
        predict = PredictModel(predict_number, predict_count)
        self.predicts.append(predict)
        PredictService(predict.predict_number, predict.predict_count)


