from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MenuBarLimit(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_limit_buttons_to_children()
        self.max_height = 150


    def add_limit_buttons_to_children(self):
        for limit in range(100, 5100, 100):
            btn = Button(text=str(limit), size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        value.parent.parent.parent.children[1].children[0].children[0].children[0].text = value.text
        value.parent.parent.parent.children[1].children[0].start_game()
