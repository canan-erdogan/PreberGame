from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.menu_bar import MenuBar
from preber_box_prediction import PreberBoxPrediction
from preber_box_range_boxes import PreberBoxRangeBoxes

Builder.load_file("kv/preber_box.kv")



class PreberBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuBar())
        self.add_widget(PreberBoxPrediction())
        self.add_widget(PreberBoxRangeBoxes())
