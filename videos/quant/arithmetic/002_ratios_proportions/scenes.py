"""Ratio & Proportion — the k-method.

Render a single scene:
    make preview FILE=videos/quant/arithmetic/002_ratios_proportions/scenes.py SCENE=Intro
"""

from manim import (
    Create,
    Cross,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    MathTex,
    Rectangle,
    ReplacementTransform,
    RIGHT,
    Text,
    UP,
    VGroup,
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
        card = title_card("Ratio & Proportion", "One move. Any question.")
        self.play(FadeIn(banner))
        self.play(Write(card[0]))
        self.play(FadeIn(card[1]))
        self.wait(1.2)

        k_formula = FormulaBox(r"a:b = 3:4 \;\Rightarrow\; a = 3k,\ b = 4k")
        self.play(FadeOut(card))
        self.play(Create(k_formula[0]), Write(k_formula[1]))
        self.wait(1.8)

        prereq = FormulaBox(r"\tfrac{a}{b} = \tfrac{c}{d} \;\Leftrightarrow\; a\cdot d = b\cdot c")
        self.play(ReplacementTransform(k_formula, prereq))
        self.wait(1.0)
        self.play(FadeOut(prereq), FadeOut(banner))


class ScaleIsFree(BrandedScene):
    def construct(self):
        unit = 0.45

        def buckets(boys_units: int, girls_units: int) -> VGroup:
            b = Rectangle(
                width=1.4,
                height=boys_units * unit,
                stroke_color=theme.PRIMARY,
                stroke_width=theme.STROKE_WIDTH,
                fill_color=theme.PRIMARY,
                fill_opacity=0.6,
            )
            g = Rectangle(
                width=1.4,
                height=girls_units * unit,
                stroke_color=theme.ACCENT,
                stroke_width=theme.STROKE_WIDTH,
                fill_color=theme.ACCENT,
                fill_opacity=0.6,
            )
            b.align_to([0, -2, 0], DOWN)
            g.align_to([0, -2, 0], DOWN)
            b.shift(LEFT * 1.5)
            g.shift(RIGHT * 1.5)
            b_label = Text("Boys", font=theme.FONT_FAMILY, font_size=theme.CAPTION_FONT_SIZE, color=theme.TEXT)
            g_label = Text("Girls", font=theme.FONT_FAMILY, font_size=theme.CAPTION_FONT_SIZE, color=theme.TEXT)
            b_label.next_to(b, DOWN, buff=0.2)
            g_label.next_to(g, DOWN, buff=0.2)
            return VGroup(b, g, b_label, g_label)

        scale_1 = buckets(3, 2)
        scale_2 = buckets(6, 4)
        scale_3 = buckets(9, 6)

        caption = Text(
            "Same shape. Different scale.",
            font=theme.FONT_FAMILY,
            font_size=theme.CAPTION_FONT_SIZE,
            color=theme.MUTED_TEXT,
        ).to_edge(UP, buff=0.8)

        self.play(FadeIn(caption))
        self.play(Create(scale_1))
        self.wait(0.8)
        self.play(ReplacementTransform(scale_1, scale_2))
        self.wait(0.6)
        self.play(ReplacementTransform(scale_2, scale_3))
        self.wait(0.8)
        self.play(FadeOut(scale_3), FadeOut(caption))

        simple = MathTex(r"3:2", color=theme.TEXT).scale(1.6)
        named = MathTex("3", "k", ",\\ ", "2", "k", color=theme.TEXT).scale(1.6)
        named[1].set_color(theme.ACCENT)
        named[4].set_color(theme.ACCENT)

        self.play(Write(simple))
        self.wait(0.6)
        self.play(ReplacementTransform(simple, named))
        self.wait(1.5)
        self.play(FadeOut(named))


class MeansExtremes(BrandedScene):
    def construct(self):
        eq = MathTex("a", ":", "b", "=", "c", ":", "d", color=theme.TEXT).scale(1.6)
        self.play(Write(eq))
        self.wait(0.6)

        # extremes: first and last; means: middle two
        self.play(
            eq[0].animate.set_color(theme.PRIMARY),
            eq[6].animate.set_color(theme.PRIMARY),
        )
        self.wait(0.4)
        self.play(
            eq[2].animate.set_color(theme.ACCENT),
            eq[4].animate.set_color(theme.ACCENT),
        )
        self.wait(1.0)

        result = MathTex(
            "a", r"\cdot", "d", "=", "b", r"\cdot", "c", color=theme.TEXT,
        ).scale(1.6)
        result[0].set_color(theme.PRIMARY)
        result[2].set_color(theme.PRIMARY)
        result[4].set_color(theme.ACCENT)
        result[6].set_color(theme.ACCENT)

        self.play(ReplacementTransform(eq, result))
        self.wait(1.8)
        self.play(FadeOut(result))


class WorkedExample(BrandedScene):
    def construct(self):
        problem = ProblemBox(
            title="Question",
            body="Ajay : Bina = 5 : 7. In 8 years, ratio = 3 : 4. Bina now?",
            width=11.0,
            height=2.5,
        ).to_edge(UP, buff=0.6)

        self.play(Create(problem[0]))
        self.play(FadeIn(problem[1]), Write(problem[2]))
        self.wait(1.0)

        steps = StepReveal([
            "Ages = 5k and 7k",
            "In 8 yrs: 5k + 8 and 7k + 8 (ratio 3:4)",
            "Means x extremes: 4(5k+8) = 3(7k+8)",
            "20k + 32 = 21k + 24  =>  k = 8",
            "Bina = 7k = 56",
        ])
        steps.next_to(problem, DOWN, buff=0.6)

        for i in range(len(steps.steps_mobs)):
            self.play(Write(steps.step(i)))
            self.wait(0.7)

        highlight = HighlightBox(steps.step(-1), color=theme.CORRECT)
        self.play(Create(highlight))
        self.wait(2.0)
        self.play(FadeOut(problem), FadeOut(steps), FadeOut(highlight))


class Traps(BrandedScene):
    def construct(self):
        trap1 = FormulaBox(r"3:4 \;+\; 2:5 \;=\; 5:9").to_edge(UP, buff=1.2)
        trap2 = FormulaBox(r"\text{boys} = \tfrac{3}{2}\ \text{of the room}").to_edge(DOWN, buff=1.2)

        self.play(Create(trap1[0]), Write(trap1[1]))
        cross1 = Cross(trap1, color=theme.WRONG, stroke_width=6)
        self.play(Create(cross1))
        self.wait(0.8)

        self.play(Create(trap2[0]), Write(trap2[1]))
        cross2 = Cross(trap2, color=theme.WRONG, stroke_width=6)
        self.play(Create(cross2))
        self.wait(1.2)

        self.play(
            FadeOut(trap1), FadeOut(cross1),
            FadeOut(trap2), FadeOut(cross2),
        )


class Outro(BrandedScene):
    def construct(self):
        card = title_card("Subscribe", "Next: Mixtures & alligations")
        self.play(FadeIn(card))
        self.wait(2.2)
        self.play(FadeOut(card))
