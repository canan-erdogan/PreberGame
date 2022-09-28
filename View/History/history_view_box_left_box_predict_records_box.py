from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from ViewModel.predict_viewmodel import PredictViewmodel


class HistoryViewBoxLeftBoxPredictRecordsBox(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_predict_records_to_children()
        self.max_height = 150
        self.predict_viewmodel = PredictViewmodel()

    def add_predict_records_to_children(self):
        for predict_records in ["PREDİCT RECORDS", "TURN BACK"]:
            btn = Button(text=str(predict_records), size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)


    def pressed(self, value):
        if value.text =="PREDİCT RECORDS":
            self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].clear_widgets(self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[0].children)
            