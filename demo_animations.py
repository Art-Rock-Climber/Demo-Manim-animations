from manim import *

        
class PoligonScene(Scene):  # Построение окружности как многоугольника
    def construct(self):
        poligon = RegularPolygon(n = 3) 
        
        self.play(Write(poligon))
        self.wait()

        for i in range(4, 20):
            new_poligon = RegularPolygon(n = i)
            self.play(ReplacementTransform(poligon, new_poligon))
            poligon = new_poligon
        self.wait()
