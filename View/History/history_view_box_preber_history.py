from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from View.History.history_view_box_preber_history_predict_box import HistoryViewBoxPreberHistoryPredictBox
from ViewModel.predict_viewmodel import PredictViewmodel

Builder.load_file("History/kv/history_view_box_preber_history.kv")


class HistoryViewBoxPreberHistory(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, None)
        self.predict_viewmodel = PredictViewmodel()
        self.add_predict()


    def add_predict(self):
        for predict in self.predict_viewmodel.predicts:
            self.add_widget(HistoryViewBoxPreberHistoryPredictBox(predict.predict_number, predict.predict_count))
