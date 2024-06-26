from manim import *
from colour import Color

def myHSV(hue, s = 0.96, v = 0.98):
    return ManimColor.from_hsv([hue,s,v])        

class SimpleCustomAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 4 * t
            angle = 2 * t + 2 * PI
            mobject.move_to(radius * (np.cos(angle)*RIGHT + np.sin(angle)*UP) )
            mobject.set_color(myHSV(t))
            mobject.set_opacity(1-t)
            
        d = Dot(color=WHITE)
        self.add( d )
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))
            

