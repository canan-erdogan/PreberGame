from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from range_box import RangeBox

Builder.load_file("kv/preber_box_range_boxes.kv")

class PreberBoxRangeBoxes(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min_box = RangeBox("1")
        self.real_number = RangeBox("?")
        self.max_box = RangeBox("100")
        self.add_widget(self.min_box)
        self.add_widget(self.real_number)
        self.add_widget(self.max_box)


