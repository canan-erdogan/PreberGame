from kivy.uix.gridlayout import GridLayout
from View.History.history_view_box_predict_box_scroll_view import HistoryViewBoxPredictBoxScrollView


class HistoryViewBoxPredictBox(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(HistoryViewBoxPredictBoxScrollView())