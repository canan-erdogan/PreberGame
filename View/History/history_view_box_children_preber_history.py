from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from View.History.history_view_box_children_preber_history_predict_box import \
    HistoryViewBoxChildrenPreberHistoryPredictBox
from ViewModel.predict_viewmodel import PredictViewmodel

Builder.load_file("History/kv/history_view_box_children_preber_history.kv")


class HistoryViewBoxChildrenPreberHistory(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, None)
        self.predict_viewmodel = PredictViewmodel()
        self.add_predict()

    def selectionSort(self, array, size):
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                if array[j].predict_limit < array[min_index].predict_limit:
                    min_index = j

                elif array[j].predict_limit == array[min_index].predict_limit:
                    if array[j].predict_count < array[min_index].predict_count:
                        min_index = j

            (array[ind], array[min_index]) = (array[min_index], array[ind])

    def add_predict(self):
        predict_array = self.predict_viewmodel.predicts
        size1 = len(predict_array)
        self.selectionSort(predict_array, size1)
        for predict in self.predict_viewmodel.predicts:
            self.add_widget(
                HistoryViewBoxChildrenPreberHistoryPredictBox(predict.predict_number, predict.predict_count, predict.predict_limit))


