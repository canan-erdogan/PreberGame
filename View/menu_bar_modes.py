from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from Service.predict_service import PredictService


class MenuBarModes(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_modes_buttons_to_children()
        self.max_height = 150

    def add_modes_buttons_to_children(self):
        for mode in ["HISTORY", "START", "RESET", "PREBER GAME"]:
            btn = Button(text=mode, size_hint_y=None, height=44)
            if mode == "PREBER GAME":
                btn.disabled = True
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        if value.text == "RESET":
            value.parent.parent.parent.children[1].children[0].start_game(True)
        elif value.text == "START":
            value.parent.parent.parent.children[1].children[0].start_game()
        elif value.text == "HISTORY":
            value.parent.parent.parent.children[1].children[0].add_history_view()
            for child in self.children[0].children:
                if child.text != "PREBER GAME":
                    child.disabled = True
                else:
                    child.disabled = False
        elif value.text == "PREBER GAME":
            value.parent.parent.parent.children[1].children[0].add_preber_view()
            for child in self.children[0].children:
                if child.text == "PREBER GAME":
                    child.disabled = True
                else:
                    child.disabled = False




