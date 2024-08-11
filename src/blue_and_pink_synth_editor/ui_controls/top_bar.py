from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.lang.builder import Builder

Builder.load_file('src/blue_and_pink_synth_editor/ui_controls/top_bar.kv')


class TopBar(BoxLayout):
    corner_radius = NumericProperty(0)
    screen_name = StringProperty('')
