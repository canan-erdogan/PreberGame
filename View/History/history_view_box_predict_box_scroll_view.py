from kivy.uix.scrollview import ScrollView
from View.History.history_view_box_preber_history import HistoryViewBoxPreberHistory


class HistoryViewBoxPredictBoxScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history_view_box_preber_history = HistoryViewBoxPreberHistory()
        self.history_view_box_preber_history.bind(minimum_height=self.history_view_box_preber_history.setter('height'))
        self.add_widget(self.history_view_box_preber_history)
