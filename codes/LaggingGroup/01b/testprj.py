from manim import *

from colour import Color

def myHSV(hue, s = 0.96, v = 0.98):
    return ManimColor.from_hsv([hue,s,v])      

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=myHSV(j/20), fill_opacity=0.5)
        for j in range(20)]).arrange_in_grid(4,5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))
