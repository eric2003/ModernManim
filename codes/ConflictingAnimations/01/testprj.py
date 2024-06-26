from manim import *

class ConflictingAnimations(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        #self.play(Rotate(s,PI), Rotate(s,-PI), run_time=3)
        self.play(Rotate(s,PI), run_time=3)
        self.play(Rotate(s,-PI), run_time=6)
