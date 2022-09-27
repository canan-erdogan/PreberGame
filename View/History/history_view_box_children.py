from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_children_predict_box import HistoryViewBoxChildrenPredictBox
from View.History.history_view_box_children_title_box import HistoryViewBoxChildrenTitleBox

Builder.load_file("History/kv/history_view_box_children.kv")


class HistoryViewBoxChildren(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HistoryViewBoxChildrenTitleBox())
        self.add_widget(HistoryViewBoxChildrenPredictBox())
