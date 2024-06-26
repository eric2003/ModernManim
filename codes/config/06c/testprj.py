from manim import *

config.background_color = WHITE

class ChangeDefaults(Scene):
    def construct(self):
        Text.set_default(color=GREEN)
        text = Text("Hello World!")
        self.add(text)
