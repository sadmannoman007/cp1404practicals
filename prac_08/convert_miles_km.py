"""
CP1404 Practical 08
Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKmConverterApp(App):
    """Convert miles to kilometres."""

    output_km = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self, miles_text):
        """Convert miles_text string to kilometres and update output."""
        miles = self.get_valid_miles(miles_text)
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, miles_text, change):
        """Increase/decrease miles by change, update field and km."""
        miles = self.get_valid_miles(miles_text)
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(self.root.ids.input_miles.text)

    @staticmethod
    def get_valid_miles(text):
        """Return 0.0 if text is invalid, otherwise float(text)."""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    MilesKmConverterApp().run()
