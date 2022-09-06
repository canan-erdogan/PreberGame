from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from View.prediction_range_box import PredictionRangeBox
from range_box import RangeBox

Builder.load_file("kv/preber_box_prediction.kv")


class PreberBoxPrediction(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.invisible_box_left = PredictionRangeBox("")
        self.input_box = TextInput(multiline=False, font_size=100, halign="center", size_hint=(1.5, 1))
        self.input_box.bind(on_text_validate=self.on_enter)
        self.invisible_box_right = PredictionRangeBox("")
        self.add_widget(self.invisible_box_left)
        self.add_widget(self.input_box)
        self.add_widget(self.invisible_box_right)

    def on_enter(self, value):
        self.parent.forward_game(int(value.text))
        value.text = ""





