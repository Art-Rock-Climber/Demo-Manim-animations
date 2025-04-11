from manim import *


class RussianTexTemplate(TexTemplate):
    def __init__(self):
        super().__init__()
        self.preamble = r"""
        \usepackage{polyglossia}
        \setmainlanguage{russian}
        \setotherlanguage{english}
        \setmainfont{Arial}[]
        \usepackage{amsmath}
        \usepackage{amssymb}
        """
        
        self.engine = "xelatex"  # Явно указываем XeLaTeX


class LaTexRissuan(Scene):
    def construct(self): 
        # Создаем свой TeX-темплейт
        myTexTemplate = TexTemplate()
        myTexTemplate.add_to_preamble(r"\usepackage[english, russian]{babel}")
        MathTex.set_default(tex_template=myTexTemplate) 
        Tex.set_default(tex_template=myTexTemplate) 
 
        # Проверяем
        text = Tex(r"Кириллица")
        self.play(Write(text))
        self.wait(3)

        
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


# Теорема Пифагора
class Pythagoras(Scene): 
    def construct(self):
        # Фигуры и лейблы        
        triangle = Polygon(4 * UP, ORIGIN, 3 * RIGHT)
        triangle.set_stroke(YELLOW, 2.5).set_z_index(1)
        square = VGroup(Square(3), Square(4), Square(5))
        square.set_opacity(0.12) 
        angle = Elbow(width=0.4).set_stroke(YELLOW, 1.5)        
        theorem = MathTex("c^2 = a^2 + b^2")        
        label = MathTex("a", "b", "c")        

        # Расположение 
        square[0].next_to(triangle, DOWN, buff=0)
        square[1].next_to(triangle, LEFT, buff=0)      
        square[2].shift(3.5 * UR).rotate(np.arctan(3 / 4)) 
        theorem.move_to(square[2].get_center()) 
        label[0].next_to(triangle, DOWN, buff=0.15)
        label[1].next_to(triangle, LEFT, buff=0.15)
        label[2].next_to(2 * UP + 1.5 * RIGHT, UR, buff=0.15)  
        picture = VGroup(triangle, square, label, angle, theorem)
        picture.move_to(ORIGIN).scale(0.75)    

        # Анимация
        self.play(Create(triangle), run_time=3)  
        self.play(GrowFromCenter(angle))      
        self.play(GrowFromCenter(label))        
        self.play(FadeIn(square[0], shift=UP))
        self.play(FadeIn(square[1], shift=RIGHT))
        self.play(FadeIn(square[2], shift=LEFT + 0.75 * DOWN))
        self.play(Write(theorem), run_time=2)  
        box = SurroundingRectangle(theorem, buff=0.2)
        box.set_stroke(YELLOW, 2)       
        self.play(ShowPassingFlash(box), run_time=2) 
        self.wait(3)


class SampleStandardDeviation(Scene):
    def construct(self):
        # Настройки сцены
        self.camera.background_color = WHITE
        self.camera.frame_center = [0, -0.85, 0]
        
        # 1. Заголовок
        title = Text("Стандартное отклонение", 
                    font_size=34, 
                    color=BLACK,
                    font="Times New Roman").to_edge(UP, buff=0.5)
        
        # 2. Формула
        formula = Tex(r"$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$", 
                     font_size=40,
                     color=BLACK)
        
        # 3. Группируем и располагаем заголовок и формулу
        title_formula = VGroup(title, formula).arrange(DOWN, buff=0.8)
        title_formula.shift(UP*0.3)  # Дополнительный сдвиг вверх
        self.play(Write(title_formula))
        self.wait(0.5)
        
        # 4. Пояснения (раздельно формулы и текст)
        explanations = VGroup(
            VGroup(
                Tex("$s$", color=BLACK),
                Text("– стандартное отклонение", 
                     font="Times New Roman", 
                     font_size=24, 
                     color=BLACK)
            ).arrange(RIGHT, buff=0.15),
            
            VGroup(
                Tex("$n$", color=BLACK),
                Text("– количество наблюдений", 
                     font="Times New Roman", 
                     font_size=24, 
                     color=BLACK)
            ).arrange(RIGHT, buff=0.15),
            
            VGroup(
                Tex(r"$\bar{x}$", color=BLACK),
                Text("– среднее значение", 
                     font="Times New Roman", 
                     font_size=24, 
                     color=BLACK)
            ).arrange(RIGHT, buff=0.15),
            
            VGroup(
                Tex("$x_i$", color=BLACK),
                Text("– отдельное наблюдение", 
                     font="Times New Roman", 
                     font_size=24, 
                     color=BLACK)
            ).arrange(RIGHT, buff=0.15)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        explanations.next_to(formula, DOWN, buff=1)
        
        # 5. Анимация пояснений
        self.play(FadeIn(explanations, shift=UP*0.5))
        self.wait(1)
        
        # 6. Подсветка элементов формулы
        # Словарь с элементами формулы и их описаниями
        elements = {
            "s": (0, 1, "Стандартное отклонение"),
            r"\sqrt": (2, 4, "Корень квадратный"),
            r"\frac{1}{n-1}": (4, 9, "Дробь (несмещённая оценка)"),
            r"\sum_{i=1}^{n}": (9, 23, "Сумма по наблюдениям"),
            r"(x_i - \bar{x})": (14, 21, "Отклонение от среднего"),
            "^2": (21, 22, "Квадрат отклонения")
        }
        
        # 7. Подсветка с подписями
        for _, (start, end, desc) in elements.items():
            # Создаем подпись
            label = Text(desc, font_size=18, color=BLACK).next_to(formula, DOWN, buff=0.4)
            
            # Подсвечиваем часть формулы
            self.play(
                Circumscribe(
                    formula[0][start:end], 
                    color=RED, 
                    run_time=1
                ),
                Write(label, shift=UP*2, rate_func=linear, run_time=1),
            )
            self.play(FadeOut(label, shift=UP*0.2), run_time=0.4)
            self.wait(0.2) 
        
        # 8. Финальная пауза
        self.wait(2)


class SimpleVersion(Scene):
    def construct(self):
        title = Text("Стандартное отклонение", font_size=36)
        formula = Tex(r"$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$", 
                     font_size=32)
        self.play(Write(VGroup(title, formula).arrange(DOWN, buff=0.8)))
        self.wait()