from manim import *

config.background_color = WHITE

class ChangeDefaults(Scene):
    def construct(self):
        Text.set_default(color=GREEN, font_size=100)
        text = Text("Hello World!",color=RED)
        self.add(text)
