"""
CP1404 - Practical 8:
Dynamic Labels.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Bob", "Sue", "Liam", "Zara", "John"]


class DynamicLabelsApp(App):
    """Kivy app that creates labels dynamically."""

    def build(self):
        """Load the .kv file and add labels to the main layout."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add a label for each name."""
        for name in NAMES:
            new_label = Label(text=name)
            self.root.ids.main.add_widget(new_label)


DynamicLabelsApp().run()
