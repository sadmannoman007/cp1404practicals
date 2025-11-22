"""
CP1404-Practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Lindsay Ward"


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (300, 120)
        self.title = "Square Number"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self, value):
        """Calculate the square of value and display result."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


if __name__ == "__main__":
    SquareNumberApp().run()
