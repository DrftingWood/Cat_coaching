# Storyboard: Percentages — the only two things that matter

| # | Duration  | Visual                                           | VO line                                          | Scene class   | Notes                        |
|---|-----------|--------------------------------------------------|--------------------------------------------------|---------------|------------------------------|
| 1 | 0:00-0:20 | Topic banner in, title + subtitle write in      | Hook about losing marks unnecessarily            | Intro         | Hold final frame 2s          |
| 2 | 0:20-0:40 | FormulaBox with `x% of y = (x/100)*y`           | "By the end you'll know two rules..."            | Intro         | Same scene, continues        |
| 3 | 1:00-2:30 | FormulaBox transform 20% → 20/100 → 0.20        | Explain percent = per hundred                    | PercentIntuition |                           |
| 4 | 2:30-4:00 | FormulaBox with `20% of 150 = 0.20 × 150 = 30`  | Explain "of" = multiply                          | OfIsMultiply  |                              |
| 5 | 4:00-5:30 | ProblemBox stems + StepReveal of 4 steps        | Walk through the CAT-style markup/discount Q     | WorkedExample | Step reveals synced to VO    |
| 6 | 5:50-6:00 | title_card "Subscribe" + "Next: Ratios"         | CTA                                              | Outro         |                              |

## Render order

1. `Intro`
2. `PercentIntuition`
3. `OfIsMultiply`
4. `WorkedExample`
5. `Outro`

## Scene class plan

### Intro
- Inherits: BrandedScene
- Purpose: Topic banner, title card, state the learning goal with a key formula.
- Uses: `topic_banner`, `title_card`, `FormulaBox`
- Key beats:
  1. Fade in banner
  2. Write title
  3. Fade in subtitle
  4. Swap title card for formula box

### PercentIntuition
- Inherits: BrandedScene
- Purpose: Show percent means divide by 100 via a transform chain.
- Uses: `FormulaBox`, `HighlightBox`
- Key beats:
  1. Write `20%`
  2. Transform into `20/100`
  3. Transform into `0.20`
  4. Highlight the final decimal

### OfIsMultiply
- Inherits: BrandedScene
- Purpose: Show "x% of y" = multiplication.
- Uses: `FormulaBox`
- Key beats:
  1. Write `20% of 150`
  2. Transform to `0.20 × 150`
  3. Transform to `= 30`

### WorkedExample
- Inherits: BrandedScene
- Purpose: Solve the markup/discount problem step-by-step.
- Uses: `ProblemBox`, `StepReveal`
- Key beats:
  1. Reveal problem box
  2. Reveal each of 4 steps with 0.6s gap
  3. Highlight the final answer

### Outro
- Inherits: BrandedScene
- Purpose: Subscribe CTA and tease the next video.
- Uses: `title_card`
- Key beats:
  1. Fade in title card
  2. Hold 2s

## Edit-bay notes
- Background track at -20 dB under VO.
- Crossfades between scenes happen in the video editor, not Manim.
