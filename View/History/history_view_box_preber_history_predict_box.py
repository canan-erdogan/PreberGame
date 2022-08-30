from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HistoryViewBoxPreberHistoryPredictBox(BoxLayout):
    def __init__(self, number, count, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 60
        self.add_widget(Label(text=number))
        self.add_widget(Label(text=count))