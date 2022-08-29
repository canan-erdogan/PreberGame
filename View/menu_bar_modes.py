from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MenuBarModes(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_modes_buttons_to_children()
        self.max_height = 150

    def add_modes_buttons_to_children(self):
        for mode in ["HISTORY", "RESET"]:
            btn = Button(text=mode, size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        print(value.text)
