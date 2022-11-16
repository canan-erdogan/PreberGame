from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.History.history_view_box import HistoryViewBox
from View.History.history_view_box_children_preber_history_predict_box import \
    HistoryViewBoxChildrenPreberHistoryPredictBox
from View.menu_bar import MenuBar
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

    def reset_game(self, reset, ):
        if reset:
            self.random_number_viewmodel.start_game("1", "100")
            self.children[0].children[0].text = "100"
            self.children[2].children[0].dropdown_button.text = "100"
        else:
            self.random_number_viewmodel.start_game("1", self.children[0].children[0].text)
        self.children[0].children[2].text = "1"
        self.children[0].children[1].text = "?"
        self.children[2].children[2].children[0].children[0].text = "0"


    def start_game(self, reset=False):
        self.children[0].children[0].text = self.children[2].children[0].dropdown_button.text
        self.reset_game(reset)


    def forward_game(self, predict_number):
        limits = self.random_number_viewmodel.forward_game(predict_number)
        if limits:
            self.children[0].min_box.text = str(limits[0])
            self.children[0].max_box.text = str(limits[1])
            self.children[2].children[2].children[0].children[0].text = str(int(self.children[2].children[2].children[0].children[0].text) + 1)
        else:
            self.children[0].real_number.text = str(predict_number)
            self.children[2].children[2].children[0].children[0].text = str(int(self.children[2].children[2].children[0].children[0].text) + 1)
            self.predict_viewmodel.append_predict_to_predicts(predict_number, self.children[2].children[2].children[0].children[0].text, self.children[2].children[0].dropdown_button.text)

    def add_history_view(self):
        self.remove_widget(self.children[0])
        self.remove_widget(self.children[0])
        self.add_widget(HistoryViewBox())

    def add_preber_view(self):
        self.remove_widget(self.children[0])
        self.add_widget(PreberBoxPrediction())
        self.add_widget(PreberBoxRangeBoxes())

    def add_predict(self):
        for predict in self.predict_viewmodel.predicts:
            self.children[0].children[1].children[0].children[0].children[0].add_widget(
                HistoryViewBoxChildrenPreberHistoryPredictBox(predict.predict_number, predict.predict_count, predict.predict_limit))


