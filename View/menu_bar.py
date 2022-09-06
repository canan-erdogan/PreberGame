from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.menu_bar_count_box_frame import MenuBarCountBoxFrame
from View.menu_bar_limit_box import MenuBarLimitBox
from View.menu_bar_modes_box import MenuBarModesBox

Builder.load_file("kv/menu_bar.kv")


class MenuBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuBarCountBoxFrame())
        self.add_widget(MenuBarModesBox())
        self.add_widget(MenuBarLimitBox())




