from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_left_limit_box_records_box_parent import HistoryViewBoxLeftLimitBoxRecordsBoxParent


class HistoryViewBoxLeftBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HistoryViewBoxLeftLimitBoxRecordsBoxParent())
        self.add_widget(BoxLayout())
        self.orientation = "vertical"