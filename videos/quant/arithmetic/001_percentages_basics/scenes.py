"""Percentages — the only two things that matter.

Render a single scene:
    make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
"""

from manim import (
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    MathTex,
    ReplacementTransform,
    UP,
    Write,
)

from lib import (
    BrandedScene,
    FormulaBox,
    HighlightBox,
    ProblemBox,
    StepReveal,
    theme,
    title_card,
    topic_banner,
)


class Intro(BrandedScene):
    def construct(self):
        banner = topic_banner(section="Quant", topic="Arithmetic")
        card = title_card("Percentages", "Two rules. That's it.")
        self.play(FadeIn(banner))
        self.play(Write(card[0]))
        self.play(FadeIn(card[1]))
        self.wait(1.5)

        formula = FormulaBox(r"x\%\ \text{of}\ y = \tfrac{x}{100}\cdot y")
        self.play(FadeOut(card))
        self.play(Create(formula[0]), Write(formula[1]))
        self.wait(2)
        self.play(FadeOut(formula), FadeOut(banner))


class PercentIntuition(BrandedScene):
    def construct(self):
        step1 = MathTex(r"20\%", color=theme.TEXT).scale(1.5)
        step2 = MathTex(r"\tfrac{20}{100}", color=theme.TEXT).scale(1.5)
        step3 = MathTex(r"0.20", color=theme.ACCENT).scale(1.5)

        self.play(Write(step1))
        self.wait(0.8)
        self.play(ReplacementTransform(step1, step2))
        self.wait(0.8)
        self.play(ReplacementTransform(step2, step3))
        highlight = HighlightBox(step3)
        self.play(Create(highlight))
        self.wait(1.5)
        self.play(FadeOut(step3), FadeOut(highlight))


class OfIsMultiply(BrandedScene):
    def construct(self):
        a = MathTex(r"20\%\ \text{of}\ 150", color=theme.TEXT).scale(1.4)
        b = MathTex(r"0.20 \times 150", color=theme.TEXT).scale(1.4)
        c = MathTex(r"= 30", color=theme.CORRECT).scale(1.4)

        self.play(Write(a))
        self.wait(0.8)
        self.play(ReplacementTransform(a, b))
        self.wait(0.8)
        self.play(ReplacementTransform(b, c))
        self.wait(1.5)
        self.play(FadeOut(c))


class WorkedExample(BrandedScene):
    def construct(self):
        problem = ProblemBox(
            title="Question",
            body="40% markup, then 25% discount. Profit %?",
            width=11.0,
            height=2.5,
        ).to_edge(UP, buff=0.8)

        self.play(Create(problem[0]))
        self.play(FadeIn(problem[1]), Write(problem[2]))
        self.wait(1)

        steps = StepReveal([
            "Let CP = 100",
            "MP = 100 + 40 = 140",
            "SP = 140 - 25% of 140 = 105",
            "Profit = 5, so profit% = 5%",
        ])
        steps.next_to(problem, DOWN, buff=0.8)

        for i in range(len(steps.steps_mobs)):
            self.play(Write(steps.step(i)))
            self.wait(0.6)

        highlight = HighlightBox(steps.step(-1), color=theme.CORRECT)
        self.play(Create(highlight))
        self.wait(2)
        self.play(FadeOut(problem), FadeOut(steps), FadeOut(highlight))


class Outro(BrandedScene):
    def construct(self):
        card = title_card("Subscribe", "Next: Ratios and proportions")
        self.play(FadeIn(card))
        self.wait(2.5)
        self.play(FadeOut(card))
