from manim import *

config.background_color = DARK_BLUE
config.frame_width = 16
config.frame_height = 9

class SimpleScene(Scene):
    def construct(self):
        tri = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(tri)
