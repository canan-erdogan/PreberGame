from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.menu_bar_count_box import MenuBarCountBox

Builder.load_file("C:\\Users\\QueFact\\Documents\\GitHub\\PreberGame\\View\\kv\\menu_bar_count_box_frame.kv")


class MenuBarCountBoxFrame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuBarCountBox())
