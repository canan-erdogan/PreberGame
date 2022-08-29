from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from View.menu_bar_count_box import MenuBarCountBox
from View.menu_bar_limit import MenuBarLimit
from View.menu_bar_limit_box import MenuBarLimitBox
from View.menu_bar_modes_box import MenuBarModesBox
from View.menu_bubble import MenuBubble
Builder.load_file("kv/menu_bar.kv")


class MenuBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuBarCountBox())
        self.add_widget(MenuBarModesBox())
        self.add_widget(MenuBarLimitBox())




