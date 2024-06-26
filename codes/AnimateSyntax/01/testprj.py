from manim import *

class AnimateSyntax(Scene):
    def construct(self):
        s = Square()
        self.play(s.animate.shift(RIGHT)) # animation of shift by RIGHT
        self.play(s.animate(run_time=2).scale(3)) # supports animation keywords
        self.play(s.animate.scale(1/2).shift(2*LEFT)) # supports chaining
