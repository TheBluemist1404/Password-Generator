import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file('pass_generator.kv')
Builder.load_file('checkbox_with_label.kv')
Builder.load_file('textinput_with_label.kv')

from pass_generator import PassGenerator

class MyApp(App):
    def build(self):
        return PassGenerator()

if __name__ == '__main__':
    MyApp().run()
