from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HistoryViewBoxLeftBoxLimitViewBox(BoxLayout):
    def __init__(self, number, count, limit, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 60
        self.add_widget(Label(text=str(number)))
        self.add_widget(Label(text=str(count)))
        self.add_widget(Label(text=str(limit)))