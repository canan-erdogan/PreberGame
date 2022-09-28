from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_left_box_limit_options_box_parent import HistoryViewBoxLeftBoxLimitOptionsBoxParent
from View.History.history_view_box_left_box_predict_records_box_parent import \
    HistoryViewBoxLeftBoxPredictRecordsBoxParent


class HistoryViewBoxLeftBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HistoryViewBoxLeftBoxLimitOptionsBoxParent())
        self.add_widget(HistoryViewBoxLeftBoxPredictRecordsBoxParent())
        self.orientation = "vertical"