from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.lang.builder import Builder

Builder.load_file('src/blue_and_pink_synth_editor/ui_controls/params_grid_non_mod_cell.kv')


class ParamsGridNonModCell(BoxLayout):
    screen_name = StringProperty('')
    section_name = StringProperty('')
    title = StringProperty('')
    param_name = StringProperty('')
    value_prop = NumericProperty(0)
    corner_radius = NumericProperty(0)
    value_color_string = StringProperty('#06070FFF')
    background_color_string = StringProperty('#438EFFFF')
    param_name_color_string = StringProperty('#ECBFEBFF')
