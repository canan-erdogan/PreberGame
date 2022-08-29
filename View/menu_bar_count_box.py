from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\PreberGame\\View\\kv\\menu_bar_count_box.kv")


class MenuBarCountBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Predict Count:", font_size="20sp"))
        self.add_widget(Label(text="0", size_hint=(.5, 1), font_size="20sp"))
