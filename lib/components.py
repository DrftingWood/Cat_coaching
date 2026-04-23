"""Reusable Manim mobjects for CAT-coaching scenes.

Every component pulls styling from ``lib.theme`` so a single theme edit
restyles the whole channel.
"""

from __future__ import annotations

from manim import (
    VGroup,
    RoundedRectangle,
    Rectangle,
    Text,
    MathTex,
    DOWN,
    LEFT,
    RIGHT,
    UP,
)

from . import theme


class ProblemBox(VGroup):
    """Rounded card with a title strip and a body text region.

    Use for stating a CAT question on screen.
    """

    def __init__(self, title: str, body: str, width: float = 10.0, height: float = 4.0):
        super().__init__()

        card = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=theme.CORNER_RADIUS,
            stroke_color=theme.PRIMARY,
            stroke_width=theme.STROKE_WIDTH,
            fill_color=theme.SURFACE,
            fill_opacity=1.0,
        )

        title_mob = Text(
            title,
            font=theme.FONT_FAMILY,
            font_size=theme.SUBTITLE_FONT_SIZE,
            color=theme.PRIMARY,
            weight="BOLD",
        )
        title_mob.next_to(card.get_top(), DOWN, buff=theme.PAD)

        body_mob = Text(
            body,
            font=theme.FONT_FAMILY,
            font_size=theme.BODY_FONT_SIZE,
            color=theme.TEXT,
        )
        body_mob.move_to(card.get_center()).shift(DOWN * 0.3)

        self.add(card, title_mob, body_mob)


class FormulaBox(VGroup):
    """Highlighted container for a LaTeX formula."""

    def __init__(self, tex: str, width: float | None = None):
        super().__init__()
        formula = MathTex(tex, color=theme.TEXT)
        w = width if width is not None else formula.width + 2 * theme.PAD
        h = formula.height + 2 * theme.PAD
        card = RoundedRectangle(
            width=w,
            height=h,
            corner_radius=theme.CORNER_RADIUS,
            stroke_color=theme.ACCENT,
            stroke_width=theme.STROKE_WIDTH,
            fill_color=theme.SURFACE,
            fill_opacity=1.0,
        )
        formula.move_to(card.get_center())
        self.add(card, formula)


class HighlightBox(Rectangle):
    """Transparent rectangle drawn around a mobject to call attention to it."""

    def __init__(self, target, color: str = theme.ACCENT, buff: float = 0.15):
        super().__init__(
            width=target.width + 2 * buff,
            height=target.height + 2 * buff,
            stroke_color=color,
            stroke_width=theme.STROKE_WIDTH,
            fill_opacity=0.0,
        )
        self.move_to(target.get_center())


class OptionRow(VGroup):
    """A labeled MCQ option (A/B/C/D) that can be flagged correct or wrong."""

    def __init__(self, label: str, text: str, width: float = 6.0):
        super().__init__()
        self.label = label
        self.text = text

        pill = RoundedRectangle(
            width=width,
            height=0.9,
            corner_radius=0.2,
            stroke_color=theme.NEUTRAL,
            stroke_width=theme.STROKE_WIDTH,
            fill_color=theme.SURFACE,
            fill_opacity=1.0,
        )
        label_mob = Text(
            f"({label})",
            font=theme.FONT_FAMILY,
            font_size=theme.BODY_FONT_SIZE,
            color=theme.ACCENT,
            weight="BOLD",
        ).next_to(pill.get_left(), RIGHT, buff=theme.PAD)
        text_mob = Text(
            text,
            font=theme.FONT_FAMILY,
            font_size=theme.BODY_FONT_SIZE,
            color=theme.TEXT,
        ).next_to(label_mob, RIGHT, buff=theme.PAD)
        self.pill = pill
        self.add(pill, label_mob, text_mob)

    def mark_correct(self):
        self.pill.set_stroke(color=theme.CORRECT)
        return self

    def mark_wrong(self):
        self.pill.set_stroke(color=theme.WRONG)
        return self


class StepReveal(VGroup):
    """Vertical list of solution steps to be revealed one at a time.

    Use ``step(i)`` in a scene to ``Write`` or ``FadeIn`` a single step.
    """

    def __init__(self, steps: list[str]):
        super().__init__()
        self.steps_mobs = []
        for i, s in enumerate(steps):
            t = Text(
                f"{i + 1}. {s}",
                font=theme.FONT_FAMILY,
                font_size=theme.BODY_FONT_SIZE,
                color=theme.TEXT,
            )
            if i > 0:
                t.next_to(self.steps_mobs[-1], DOWN, aligned_edge=LEFT, buff=0.35)
            self.steps_mobs.append(t)
            self.add(t)

    def step(self, i: int) -> Text:
        return self.steps_mobs[i]
