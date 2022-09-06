from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from View.menu_bar_limit import MenuBarLimit
Builder.load_file("C:\\Users\\QueFact\\Documents\\GitHub\\PreberGame\\View\\kv\\menu_bar_limit_box.kv")



class MenuBarLimitBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = MenuBarLimit()
        self.dropdown_button = Button(text='Limits')
        self.dropdown_button.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
        self.dropdown_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_button, 'text', x))
        self.add_widget(Label(text="Select Limits", font_size="20sp", size_hint=(1, .5), color=(0, 0, 0, 1)))
        self.add_widget(self.dropdown_button)


