from manim import *

class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s,c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s,c).animate.arrange(RIGHT,buff=1))
