from manim import Circle, Create, Scene


class HelloManim(Scene):
    def construct(self):
        circle = Circle(color="#58C4DD")
        self.play(Create(circle))
        self.wait(1)
