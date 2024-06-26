from manim import *

config.background_color = YELLOW

class SimpleScene(Scene):
    def construct(self):
        tri = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(tri)
