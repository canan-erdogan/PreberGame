from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_children import HistoryViewBoxChildren
from View.History.history_view_box_left_box import HistoryViewBoxLeftBox

Builder.load_file("History/kv/history_view_box.kv")


class HistoryViewBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HistoryViewBoxLeftBox())
        self.add_widget(HistoryViewBoxChildren())
        self.add_widget(BoxLayout())