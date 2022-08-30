from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.History.history_view_box import HistoryViewBox
from View.menu_bar import MenuBar
from View.range_box import RangeBox
from ViewModel.predict_viewmodel import PredictViewmodel
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
        self.random_number_viewmodel = RandomNumberViewmodel(1, 100)
        self.predict_viewmodel = PredictViewmodel()

    def reset_game(self,reset):
        if reset:
            self.children[0].children[0].text = "100"
        self.children[0].children[2].text = "1"
        self.children[0].children[1].text = "?"
        self.children[2].children[2].children[0].text = "0"

    def start_game(self, reset=False):
        min_limit = "1"
        if not self.children[2].children[0].dropdown_button.text == "Limits":
            self.children[0].children[0].text = self.children[2].children[0].dropdown_button.text
        max_limit = self.children[0].children[0].text
        self.random_number_viewmodel.start_game(min_limit, max_limit)
        self.reset_game(reset)


    def forward_game(self, predict_number):
        limits = self.random_number_viewmodel.forward_game(predict_number)
        if limits:
            self.children[0].min_box.text = str(limits[0])
            self.children[0].max_box.text = str(limits[1])
            self.children[2].children[2].children[0].text = str(int(self.children[2].children[2].children[0].text) + 1)
        else:
            self.children[0].real_number.text = str(predict_number)
            self.predict_viewmodel.append_predict_to_predicts(predict_number, self.children[2].children[2].children[0].text)

    def add_history_view(self):
        self.remove_widget(self.children[0])
        self.remove_widget(self.children[0])
        self.add_widget(HistoryViewBox())

    def add_preber_view(self):
        self.remove_widget(self.children[0])
        self.add_widget(PreberBoxPrediction())
        self.add_widget(PreberBoxRangeBoxes())



