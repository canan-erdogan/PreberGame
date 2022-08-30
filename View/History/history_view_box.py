from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box_preber_history import HistoryViewBoxPreberHistory
from View.History.history_view_box_predict_box import HistoryViewBoxPredictBox

Builder.load_file("History/kv/history_view_box.kv")


class HistoryViewBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BoxLayout())
        self.add_widget(HistoryViewBoxPredictBox())
        self.add_widget(BoxLayout())