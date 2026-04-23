"""Starter Manim scenes for a new video.

Copy this file to ``videos/<section>/<topic>/NNN_slug/scenes.py`` and edit.
Every scene subclasses ``BrandedScene`` so the channel background and defaults
apply automatically. Use components from ``lib`` instead of hand-rolling hex
colors or boxes.

Render a single scene:
    make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
"""

from manim import Create, FadeIn, FadeOut, Write

from lib import (
    BrandedScene,
    ProblemBox,
    StepReveal,
    title_card,
    topic_banner,
)


class Intro(BrandedScene):
    """Title card with topic banner."""

    def construct(self):
        banner = topic_banner(section="Quant", topic="Arithmetic")
        card = title_card("Video Title", "One-line hook")
        self.play(FadeIn(banner))
        self.play(Write(card[0]))
        if len(card) > 1:
            self.play(FadeIn(card[1]))
        self.wait(1.5)
        self.play(FadeOut(card), FadeOut(banner))


class Problem(BrandedScene):
    """Pose the worked problem."""

    def construct(self):
        problem = ProblemBox(
            title="Question",
            body="Replace with the CAT problem statement.",
        )
        self.play(Create(problem[0]))
        self.play(FadeIn(problem[1]), Write(problem[2]))
        self.wait(2)


class Solution(BrandedScene):
    """Reveal steps one at a time."""

    def construct(self):
        steps = StepReveal([
            "State what's given.",
            "Pick the approach.",
            "Do the math.",
            "Check and answer.",
        ])
        for i in range(len(steps.steps_mobs)):
            self.play(Write(steps.step(i)))
            self.wait(0.5)
        self.wait(1)


class Outro(BrandedScene):
    """Recap + CTA."""

    def construct(self):
        card = title_card("Subscribe", "New CAT video every week")
        self.play(FadeIn(card))
        self.wait(2)
