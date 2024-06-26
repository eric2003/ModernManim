from manim import *

class AnimationMechanisms(Scene):
    def construct(self):
        c = Circle()
        
        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)
        self.add(c)
        self.wait()        
        self.play(MoveToTarget(c))
