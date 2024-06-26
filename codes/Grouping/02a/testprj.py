from manim import *

class Grouping(Scene):
    def construct(self):
        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP, buff=0.5)
        self.add(circles)
