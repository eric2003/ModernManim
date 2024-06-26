from manim import *

config.background_color = BLACK
config.frame_width = 10
config.frame_height = 10

config.pixel_width = 500
config.pixel_height = 500

class SimpleScene(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-8,8),y_range=(-5,5))
        tri = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(plane, tri)
