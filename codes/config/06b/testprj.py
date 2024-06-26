from manim import *

config.background_color = WHITE

class ChangeDefaults(Scene):
    def construct(self):
        text = Text("Hello World!", color=BLACK)
        self.add(text)
