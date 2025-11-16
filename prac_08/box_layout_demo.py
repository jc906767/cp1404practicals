"""
CP1404 - Practical 8
Box Layout Demo
Lachlan Blackney
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """changes the text in the greeting box to the given name"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """clears all the text from the output_label box"""
        self.root.ids.output_label.text = ''



BoxLayoutDemo().run()
