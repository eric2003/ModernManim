from manim import *

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN,fill_opacity=0.5)
        self.add(c)
        
        for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))
