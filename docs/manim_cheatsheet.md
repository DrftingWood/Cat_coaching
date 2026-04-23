# Manim cheat sheet

Patterns you'll use constantly. Assume Manim Community v0.19.

## Imports

```python
from manim import (
    Create, Write, FadeIn, FadeOut, Transform, ReplacementTransform,
    MoveToTarget, UP, DOWN, LEFT, RIGHT, ORIGIN,
    Text, MathTex, VGroup,
)
from lib import BrandedScene, ProblemBox, FormulaBox, HighlightBox, StepReveal
from lib import theme
```

## Scene skeleton

```python
class MyScene(BrandedScene):
    def construct(self):
        box = ProblemBox("Question", "What is 20% of 150?")
        self.play(Create(box[0]))
        self.play(FadeIn(box[1]), Write(box[2]))
        self.wait(2)
```

## Text vs formulas

```python
label = Text("Profit = SP - CP", font=theme.FONT_FAMILY, font_size=theme.BODY_FONT_SIZE, color=theme.TEXT)
formula = MathTex(r"\text{CI} = P\left(1+\tfrac{r}{100}\right)^{n} - P")
```

Use raw strings for LaTeX to avoid double-escaping.

## Positioning

```python
a.next_to(b, DOWN, buff=0.35)
a.align_to(b, LEFT)
g = VGroup(a, b, c).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
g.to_edge(UP, buff=0.5)
g.move_to(ORIGIN)
```

## Revealing step by step

```python
steps = StepReveal(["Given 20% of 150", "= 0.20 * 150", "= 30"])
for i in range(len(steps.steps_mobs)):
    self.play(Write(steps.step(i)))
    self.wait(0.6)
```

## Highlighting something already on screen

```python
box = HighlightBox(formula)
self.play(Create(box))
self.wait(1)
self.play(FadeOut(box))
```

## Morphing one thing into another

```python
self.play(Transform(old_formula, new_formula))
```

Use `ReplacementTransform` if you want `old_formula` to stop existing after.

## MCQ options with answer reveal

```python
from lib import OptionRow
rows = [OptionRow("A", "20"), OptionRow("B", "25"), OptionRow("C", "30"), OptionRow("D", "40")]
group = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
self.play(FadeIn(group))
self.wait(1)
self.play(*[r.animate.set_opacity(0.4) for r in rows if r.label != "C"])
rows[2].mark_correct()
```

## Rendering

```
make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
make high    FILE=... SCENE=...
make fourk   FILE=... SCENE=...
```

Output goes to `media/videos/<source-file-stem>/<quality>/<SceneName>.mp4`.

## Debugging tips

- If LaTeX fails, check `media/Tex/` for the `.log` file — real error is there.
- If a font isn't found, Manim falls back silently and things look off.
  Confirm `theme.FONT_FAMILY` is installed in the container.
- `self.wait(...)` is cheap — use liberally to make timing tunable without
  re-editing animations.
