from kivy.uix.scrollview import ScrollView
from View.History.history_view_box_children_preber_history import HistoryViewBoxChildrenPreberHistory
from View.History.history_view_box_limit_records_preber_history import HistoryViewBoxLimitRecordsPreberHistory


class HistoryViewBoxChildrenPredictBoxScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history_view_box_preber_history = HistoryViewBoxChildrenPreberHistory()
        self.history_view_box_preber_history.bind(minimum_height=self.history_view_box_preber_history.setter('height'))
        self.add_widget(self.history_view_box_preber_history)


    def add_limit_records_preber_history(self):
        self.clear_widgets(self.children)
        self.history_view_box_limit_records_preber_history = HistoryViewBoxLimitRecordsPreberHistory()
        self.history_view_box_limit_records_preber_history.bind(
            minimum_height=self.history_view_box_limit_records_preber_history.setter('height'))
        self.add_widget(self.history_view_box_limit_records_preber_history)

    def clear_limit_records_preber_history(self):
        self.remove_widget(self.history_view_box_limit_records_preber_history)
        self.add_widget(self.history_view_box_preber_history)