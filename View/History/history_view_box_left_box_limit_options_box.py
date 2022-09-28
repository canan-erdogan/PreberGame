from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from View.History.history_view_box_children_preber_history_predict_box import \
    HistoryViewBoxChildrenPreberHistoryPredictBox
from ViewModel.predict_viewmodel import PredictViewmodel


class HistoryViewBoxLeftBoxLimitOptionsBox(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_limit_options_to_children()
        self.max_height = 150
        self.predict_viewmodel = PredictViewmodel()


    def add_limit_options_to_children(self):
        btn = Button(text=str("TURN BACK"), size_hint_y=None, height=44)
        if btn.text == "TURN BACK":
            btn.disabled = True
        btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
        btn.bind(on_release=lambda btn: self.select(btn.text))
        btn.bind(on_press=self.pressed)
        self.add_widget(btn)
        for limit_options in range(100, 5100, 100):
            btn = Button(text=str(limit_options), size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        if value.text != "TURN BACK":
            for child in self.children[0].children:
                if child.text != "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].clear_widgets(self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].children)
            predict_array = self.predict_viewmodel.predicts
            size1 = len(predict_array)
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].selectionSort(predict_array, size1)
            for predict in self.predict_viewmodel.predicts:
                if str(predict.predict_limit) == value.text:
                    self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].add_widget(
                        HistoryViewBoxChildrenPreberHistoryPredictBox(predict.predict_number, predict.predict_count,
                                                                    predict.predict_limit))
        elif value.text == "TURN BACK":
            for child in self.children[0].children:
                if child.text == "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False
                    self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].clear_widgets(self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].children)
                    self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].add_predict()

