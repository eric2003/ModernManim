from manim import *

config.background_color = BLACK

class ChangeDefaults(Scene):
    def construct(self):
        text = Text("Hello World!")
        self.add(text)
