from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.menu_bar import MenuBar
from View.range_box import RangeBox
from ViewModel.random_number_viewmodel import RandomNumberViewmodel
from preber_box_prediction import PreberBoxPrediction
from preber_box_range_boxes import PreberBoxRangeBoxes

Builder.load_file("kv/preber_box.kv")



class PreberBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuBar())
        self.add_widget(PreberBoxPrediction())
        self.add_widget(PreberBoxRangeBoxes())
        self.random_number_viewmodel = RandomNumberViewmodel(1 , 100)

    def start_game(self):
        min_limit = "1"
        max_limit = self.children[0].children[0].text
        self.random_number_viewmodel.start_game(min_limit, max_limit)
        self.children[0].children[2].text = "1"

    def forward_game(self, predict_number):
        limits = self.random_number_viewmodel.forward_game(predict_number)
        if limits:
            self.children[0].min_box.text = str(limits[0])
            self.children[0].max_box.text = str(limits[1])
            self.children[2].children[2].children[0].text = str(int(self.children[2].children[2].children[0].text) + 1)
        else:
            self.children[0].real_number.text = str(predict_number)



