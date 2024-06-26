from manim import *
from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5,51,5):
            #self.add(Circle(radius=perc*Percent(X_AXIS)))
            self.add(Square(side_length=2*perc*Percent(Y_AXIS),color=YELLOW))
            
        d = Dot()
        d.shift(100*Pixels * RIGHT)
        self.add(d)
        

