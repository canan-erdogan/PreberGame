from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_file("History/kv/history_view_box_children_title_box.kv")
class HistoryViewBoxChildrenTitleBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = 1, 0.1
        self.add_widget(Label(text="PREDİCT NUMBER", font_size=13))
        self.add_widget(Label(text="PREDİCT COUNT", font_size=13))
        self.add_widget(Label(text="PREDİCT LİMİT", font_size=13))




