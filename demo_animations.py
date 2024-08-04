from manim import *
import numpy as mp


class DemoScene(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        self.play(Write(c))
        self.wait()
        self.play(ReplacementTransform(c, s))
        self.wait()
