from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout


class ErrorDialog(BoxLayout):
    ok = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ErrorDialog, self).__init__(**kwargs)
