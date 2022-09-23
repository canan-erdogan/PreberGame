from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_left_box_limit_records_box import HistoryViewBoxLeftBoxLimitRecordsBox
from View.History.history_view_box_left_limit_box_records_box_parent import HistoryViewBoxLeftLimitBoxRecordsBoxParent

Builder.load_file("History/kv/history_view_box_left_box.kv")


class HistoryViewBoxLeftBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HistoryViewBoxLeftLimitBoxRecordsBoxParent())
        self.add_widget(BoxLayout())
        self.orientation = "vertical"