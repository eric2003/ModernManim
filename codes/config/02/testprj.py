from manim import *

class Grouping(Scene):
    def construct(self):
        stars = VGroup(*[Star(color=YELLOW,fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4,5,buff=0.2)
        self.add(stars)
