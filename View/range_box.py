from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_file("kv/range_box.kv")
class RangeBox(Label):
    def __init__(self, text,  **kwargs):
        super().__init__(**kwargs)
        self.text = text


