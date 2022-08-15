from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from View.menu_bubble import MenuBubble

Builder.load_file("kv/menu_bar.kv")
class MenuBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.predict_count = Label(text="0")
        self.add_predict_count_box_to_widgets()
        self.add_menu_buttons_to_widgets()

    def add_menu_buttons_to_widgets(self):
        self.add_widget(Button(text="history"))
        self.add_widget(Button(text="reset"))
        main_button = Button(text='Limit')
        dropdown = self.create_dropdown()
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
        self.add_widget(main_button)

    def add_predict_count_box_to_widgets(self):
        predict_count_box = BoxLayout(orientation="horizontal")
        predict_count_box.add_widget(Label(text="Predict count :"))
        predict_count_box.add_widget(self.predict_count)
        self.add_widget(predict_count_box)

    def create_dropdown(self):
        dropdown = DropDown()
        for index in range(3):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        return dropdown
