from kivy.uix.gridlayout import GridLayout
from View.History.history_view_box_children_predict_box_scroll_view import HistoryViewBoxChildrenPredictBoxScrollView


class HistoryViewBoxChildrenPredictBox(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(HistoryViewBoxChildrenPredictBoxScrollView())




