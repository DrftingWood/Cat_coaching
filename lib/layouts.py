"""Scene-level layout helpers: title cards, banners, standard compositions."""

from __future__ import annotations

from manim import VGroup, Text, Line, DOWN, UP, LEFT, RIGHT

from . import theme
from .components import OptionRow, ProblemBox


def title_card(title: str, subtitle: str | None = None) -> VGroup:
    """Big centered title with optional subtitle underneath."""
    group = VGroup()
    title_mob = Text(
        title,
        font=theme.FONT_FAMILY,
        font_size=theme.TITLE_FONT_SIZE,
        color=theme.PRIMARY,
        weight="BOLD",
    )
    group.add(title_mob)
    if subtitle:
        sub = Text(
            subtitle,
            font=theme.FONT_FAMILY,
            font_size=theme.SUBTITLE_FONT_SIZE,
            color=theme.MUTED_TEXT,
        ).next_to(title_mob, DOWN, buff=0.35)
        group.add(sub)
    return group


def topic_banner(section: str, topic: str) -> VGroup:
    """Small top banner like 'QUANT  ·  Arithmetic'."""
    label = Text(
        f"{section.upper()}  ·  {topic}",
        font=theme.FONT_FAMILY,
        font_size=theme.CAPTION_FONT_SIZE,
        color=theme.ACCENT,
    )
    rule = Line(
        start=label.get_left() + DOWN * 0.25,
        end=label.get_right() + DOWN * 0.25,
        color=theme.ACCENT,
        stroke_width=2,
    )
    return VGroup(label, rule).to_edge(UP, buff=0.4)


def question_layout(stem: str, options: list[tuple[str, str]]) -> VGroup:
    """Stacks a ProblemBox above a column of OptionRows.

    ``options`` is ``[("A", "text"), ("B", "text"), ...]``.
    """
    problem = ProblemBox("Question", stem)
    rows = VGroup(*[OptionRow(label, text) for label, text in options])
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    rows.next_to(problem, DOWN, buff=0.6)
    return VGroup(problem, rows)


def two_pane_split() -> tuple[VGroup, VGroup]:
    """Returns two empty VGroups positioned left/right at half-screen width.

    Add mobjects to the returned groups and arrange/animate them inside each pane.
    """
    left = VGroup().to_edge(LEFT, buff=0.6)
    right = VGroup().to_edge(RIGHT, buff=0.6)
    return left, right
