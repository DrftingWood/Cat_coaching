"""Shared Manim helpers for the CAT-coaching channel."""

from . import theme
from .components import (
    FormulaBox,
    HighlightBox,
    OptionRow,
    ProblemBox,
    StepReveal,
)
from .layouts import (
    question_layout,
    title_card,
    topic_banner,
    two_pane_split,
)
from .utils import BrandedScene, set_channel_config

__all__ = [
    "theme",
    "BrandedScene",
    "set_channel_config",
    "ProblemBox",
    "FormulaBox",
    "HighlightBox",
    "OptionRow",
    "StepReveal",
    "title_card",
    "topic_banner",
    "question_layout",
    "two_pane_split",
]
