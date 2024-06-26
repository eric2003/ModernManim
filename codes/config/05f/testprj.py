from manim import *

config.background_color = BLACK
config.frame_width = 9
config.frame_height = 16

config.pixel_width = 1080
config.pixel_height = 1920

class SimpleScene(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-4.5,4.5),y_range=(-8,8))
        tri = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(plane, tri)
