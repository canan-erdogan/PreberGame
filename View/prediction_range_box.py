from kivy.uix.label import Label


class PredictionRangeBox(Label):
    def __init__(self, text,  **kwargs):
        super().__init__(**kwargs)
        self.text = text