from kivy.lang import Builder
from kivy.uix.bubble import Bubble

Builder.load_file("kv/menu_bubble.kv")
class MenuBubble(Bubble):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
