"""
CP1404 Practical 08
Dynamic Labels - create labels from a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app that creates Label widgets dynamically."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Ada Lovelace", "Lindsay Ward", "Swopnil", "JCU"]

    def build(self):
        """Build the UI and add labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Add a Label for each name."""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))


if __name__ == "__main__":
    DynamicLabelsApp().run()
