from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from View.History.history_view_box_left_box_limit_view_box import HistoryViewBoxLeftBoxLimitViewBox
from ViewModel.predict_viewmodel import PredictViewmodel

Builder.load_file("History/kv/history_view_box_limit_records_preber_history.kv")

class HistoryViewBoxLimitRecordsPreberHistory(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, None)
        self.predict_viewmodel = PredictViewmodel()
        self.add_predict()


    def add_predict(self):
        def selectionSort(array, size):
            for ind in range(size):
                min_index = ind

                for j in range(ind + 1, size):
                    if array[j].predict_limit < array[min_index].predict_limit:
                        min_index = j

                    if array[j].predict_limit == array[min_index].predict_limit:
                        if array[j].predict_count < array[min_index].predict_count:
                            min_index = j

                (array[ind], array[min_index]) = (array[min_index], array[ind])

        predict_array = self.predict_viewmodel.predicts
        size = len(predict_array)
        selectionSort(predict_array, size)

        for predict in self.predict_viewmodel.predicts:
            self.add_widget(HistoryViewBoxLeftBoxLimitViewBox(predict.predict_number, predict.predict_count, predict.predict_limit))