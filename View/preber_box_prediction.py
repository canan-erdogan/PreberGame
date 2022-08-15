from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from range_box import RangeBox

Builder.load_file("kv/preber_box_prediction.kv")


class PreberBoxPrediction(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.invisibility_box_left = RangeBox("")
        self.input_box = TextInput(multiline=False, font_size=130, halign="center")
        self.invisibility_box_right = RangeBox("")
        self.add_widget(self.invisibility_box_left)
        self.add_widget(self.input_box)
        self.add_widget(self.invisibility_box_right)


