from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

from View.History.history_view_box_limit_records_preber_history import HistoryViewBoxLimitRecordsPreberHistory

Builder.load_file("History/kv/history_view_box_left_box_limit_records_box.kv")


class HistoryViewBoxLeftBoxLimitRecordsBox(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_limit_records_to_children()
        self.max_height = 150
        self.history_view_box_limit_records_preber_history = HistoryViewBoxLimitRecordsPreberHistory()


    def add_limit_records_to_children(self):
        for mode in ["LİMİT RECORDS", "TURN BACK"]:
            btn = Button(text=mode, size_hint_y=None, height=44)
            if mode == "TURN BACK":
                btn.disabled = True
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        if value.text == "LİMİT RECORDS":
            self.parent.parent.children[1].children[0].children[0].children[1].children[0].children[0].add_limit_records_preber_history()
            self.parent.parent.children[1].children[0].children[0].children[1].children[1].add_widget(Label(text="PREDİCT LİMİT", font_size=13))
            for child in self.children[0].children:
                if child.text != "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False

        elif value.text == "TURN BACK":
            self.parent.parent.children[1].children[0].children[0].children[1].children[1].remove_widget(self.parent.parent.children[1].children[0].children[0].children[1].children[1].children[0])
            self.parent.parent.children[1].children[0].children[0].children[1].children[0].children[0].clear_limit_records_preber_history()
            for child in self.children[0].children:
                if child.text == "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False