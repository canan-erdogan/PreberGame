from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from View.preber_box import PreberBox

Builder.load_file("kv/prebergame.kv")

class PreberGame(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(PreberBox())

class PreberGameApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return PreberGame()

if __name__ == "__main__":
    PreberGameApp().run()
