from manim import *
from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5,51,5):
            self.add(Circle(radius=perc*Percent(X_AXIS)))

