from manim import *

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        
        # next_to from episode 1
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot,RIGHT+UP) # RIGHT == [1,0,0]
        self.add(red_dot, green_dot)
        
        # shift
        s = Square(color=ORANGE)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)
        
        # move_to
        c = Circle(color=PURPLE)
        c.move_to([-3,-2,0])
        self.add(c)
        
        ## align_to
        c2 = Circle(radius=0.5, color = RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP);
        self.add(c2)
