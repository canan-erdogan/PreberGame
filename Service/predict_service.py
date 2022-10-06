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

    @staticmethod
    def predict_records_dropdown(predicts):
        predict_records = {}
        for predict in predicts:
            if predict.predict_limit not in predict_records:
                predict_records[predict.predict_limit] = [predict.predict_count, predict.predict_number]
        return predict_records


    @staticmethod
    def limit_options_selection_sort(array, size):
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                if array[j].predict_limit < array[min_index].predict_limit:
                    min_index = j

                elif array[j].predict_limit == array[min_index].predict_limit:
                    if array[j].predict_count < array[min_index].predict_count:
                        min_index = j

            (array[ind], array[min_index]) = (array[min_index], array[ind])

    @staticmethod
    def predict_records_selection_sort(array, size):
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                if array[j].predict_limit < array[min_index].predict_limit:
                    min_index = j
                    for j in range(ind + 1, size):
                        if array[j].predict_count < array[min_index].predict_count:
                            min_index = j

            (array[ind], array[min_index]) = (array[min_index], array[ind])
