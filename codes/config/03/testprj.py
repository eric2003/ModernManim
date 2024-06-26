from manim import *

class SimpleScene(Scene):
    def construct(self):
        tri = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(tri)
