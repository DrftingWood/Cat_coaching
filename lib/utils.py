"""Scene base class and small helpers."""

from __future__ import annotations

from manim import Scene, config

from . import theme


class BrandedScene(Scene):
    """Subclass of ``Scene`` that applies channel defaults.

    Use this for every scene so background color and defaults stay consistent.
    """

    def setup(self):
        super().setup()
        self.camera.background_color = theme.BG


def set_channel_config() -> None:
    """Apply channel-wide Manim config overrides.

    Call at module import time in a ``scenes.py`` if you want config to apply
    even when the file is imported rather than rendered via the CLI.
    """
    config.background_color = theme.BG
