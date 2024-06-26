from manim import *
from colour import Color

def myHSV(hue, s = 0.96, v = 0.98):
    return ManimColor.from_hsv([hue,s,v])        

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1, fill_opacity=0.5, color=myHSV(j/5)
                             )
                             for j in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time=2)
        self.play(
            Rotate(polys[0],PI,rate_func=lambda t:t), # rate_func = linear
            Rotate(polys[1],PI,rate_func=smooth), # default behavior
            Rotate(polys[2],PI,rate_func=lambda t: np.sin(t*PI)),
            Rotate(polys[3],PI,rate_func=there_and_back),
            Rotate(polys[4],PI,rate_func=lambda t:1-abs(1-2*t)),
            run_time=2
        )
        self.wait()
