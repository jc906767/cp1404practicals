"""
CP1404 - Practical 8
Convert miles to kilometers
Lachlan Blackney
"""

from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    """Kivy app to convert miles to kilometres."""

    def build(self):
        """Build the Kivy app from the .kv file."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert_distance(self, text):
        """Convert miles to kilometres and update the output label."""
        miles = self.get_valid_number(text)
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_distance.text = f"{kilometres:.3f}"

    def input_change(self, text, change):
        """Change the miles input up or down, then update the conversion."""
        miles = self.get_valid_number(text) + change
        self.root.ids.input_number.text = str(miles)
        self.convert_distance(self.root.ids.input_number.text)

    def get_valid_number(self, text):
        """Return the number from text, or 0.0 if the text is invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometresApp().run()