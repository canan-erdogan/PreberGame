from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from View.History.history_view_box_left_box_limit_records_box import HistoryViewBoxLeftBoxLimitRecordsBox


class HistoryViewBoxLeftLimitBoxRecordsBoxParent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = HistoryViewBoxLeftBoxLimitRecordsBox()
        self.dropdown_button = Button(text='LİMİT RECORDS')
        self.dropdown_button.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
        self.dropdown_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_button, 'text', x))
        self.dropdown_button.size_hint = 1, .2
        self.add_widget(self.dropdown_button)


