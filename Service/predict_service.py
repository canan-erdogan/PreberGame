import csv
import os.path


class PredictService:
    def __init__(self, predict_number, predict_count, predict_limit):
        self.predict_number = predict_number
        self.predict_count = predict_count
        self.predict_limit = predict_limit
        if not os.path.exists("../Service/predict.csv"):
            self.create_csv()
        self.append_predict_to_csv()


    def create_csv(self):
        header = ["predict_number", "predict_count", "predict_limit"]
        self.write_to_csv(header)

    @staticmethod
    def write_to_csv(data):
        with open("../Service/predict.csv", "a", encoding= 'UTF8', newline = "") as f:
            csv.writer(f).writerow(data)


    def append_predict_to_csv(self):
        data = [self.predict_number, self.predict_count, self.predict_limit]
        self.write_to_csv(data)

    @staticmethod
    def read_predict_from_csv():
        if os.path.exists("C:\\Users\\QueFact\\Documents\\GitHub\\PreberGame\\Service\\predict.csv"):
            reader = open("C:\\Users\\QueFact\\Documents\\GitHub\\PreberGame\\Service\\predict.csv", "r", encoding='UTF8')
            return csv.DictReader(reader)
        return {}