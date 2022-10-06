from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from View.History.history_view_box_children_preber_history_predict_box import \
    HistoryViewBoxChildrenPreberHistoryPredictBox
from ViewModel.predict_viewmodel import PredictViewmodel


class HistoryViewBoxLeftBoxPredictRecordsBox(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_predict_records_to_children()
        self.max_height = 150

    def add_predict_records_to_children(self):
        for predict_records in ["PREDİCT RECORDS", "TURN BACK"]:
            btn = Button(text=str(predict_records), size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        if value.text == "PREDİCT RECORDS":
            predict_viewmodel1 = self.parent.children[1].children[0].predict_viewmodel
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                0].clear_widgets(
                self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                    0].children)
            for child in self.children[0].children:
                if child.text != "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False
            predict_records = predict_viewmodel1.predict_records_dropdown()
            for predict in predict_records:
                self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                    0].add_widget(
                    HistoryViewBoxChildrenPreberHistoryPredictBox(predict_records[predict][1],
                                                                  predict_records[predict][0],
                                                                  predict))
        else:
            for child in self.children[0].children:
                if child.text == "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                0].clear_widgets(
                self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                    0].children)
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                0].add_predict()
