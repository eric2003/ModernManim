from manim import *

config.background_color = BLACK

class ChangeDefaults(Scene):
    def construct(self):
        Text.set_default(color=GREEN, font_size=100)
        text = Text("Hello World!",color=RED)
        Text.set_default()
        t2 = Text("Goodbye!").next_to(text, DOWN)
        self.add(text, t2)
