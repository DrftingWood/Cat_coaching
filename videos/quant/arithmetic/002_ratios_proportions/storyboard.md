# Storyboard: Ratio & Proportion — the k-method

## 1. Storyboard table

| #  | Duration  | Visual                                                        | VO line                                              | Scene class    | Notes                              |
|----|-----------|---------------------------------------------------------------|------------------------------------------------------|----------------|------------------------------------|
| 1  | 0:00-0:15 | Topic banner + title card write in                           | "You think ratio questions are about numbers..."    | Intro          | Hold final frame 1s                |
| 2  | 0:15-0:30 | FormulaBox with `a:b = 3:4 ⇒ a = 3k, b = 4k`                 | "By the end of three minutes, one technique..."     | Intro          | Same scene, continues              |
| 3  | 0:30-0:40 | Light fade of `a/b = c/d ⇔ ad = bc`                          | "You need basic fractions and linear equations..."  | Intro          | Reuse scene; FadeOut at end        |
| 4  | 0:40-1:25 | Two buckets fill 3:2, then rescale 6:4, 9:6; morph to 3k,2k  | "...shape not count...give the scale a name..."     | ScaleIsFree    | k in ACCENT                        |
| 5  | 1:25-2:00 | `a:b = c:d` with outer/inner glow, morph to `a·d = b·c`      | "Product of means equals product of extremes..."    | MeansExtremes  |                                    |
| 6  | 2:00-3:00 | ProblemBox + StepReveal of 4 steps; green highlight on ans  | "Ajay and Bina's ages... Bina is fifty-six."       | WorkedExample  | Sync step reveals to VO beats      |
| 7  | 3:00-3:15 | Two small FormulaBoxes with red cross-outs                   | "Two traps. Ratios do not add..."                   | Traps          | Cross-out = HighlightBox in WRONG  |
| 8  | 3:15-3:30 | title_card "Subscribe" + "Next: Mixtures & alligations"     | "One move. Name the scale..."                       | Outro          |                                    |

## 2. Scene class plan

### Intro
- Inherits: `BrandedScene`
- Purpose: Banner + title, state the one-move promise, show the k-method and prereq formulas.
- Uses: `topic_banner`, `title_card`, `FormulaBox`
- Key beats:
  1. Fade in banner
  2. Write title
  3. Fade in subtitle
  4. Swap title card for k-method `FormulaBox`
  5. Swap again for prereq cross-multiplication `FormulaBox`
  6. Fade everything out

### ScaleIsFree
- Inherits: `BrandedScene`
- Purpose: Visually show that 3:2 is the same shape at every scale, then introduce k.
- Uses: `FormulaBox`, plain `Rectangle`s for the buckets, `theme`
- Key beats:
  1. Draw two rectangles labelled "Boys" and "Girls" that fill to heights 3 and 2 (units)
  2. Rescale them to 6:4, then 9:6, showing the ratio is preserved
  3. Fade buckets; write `3:2`, transform into `3k, 2k` with k in `ACCENT`

### MeansExtremes
- Inherits: `BrandedScene`
- Purpose: Teach product-of-means = product-of-extremes by highlighting positions.
- Uses: `MathTex`, `theme`
- Key beats:
  1. Write `a : b = c : d`
  2. Colour a and d (extremes) in `PRIMARY`
  3. Colour b and c (means) in `ACCENT`
  4. Transform to `a \cdot d = b \cdot c`
  5. Hold 1s, fade out

### WorkedExample
- Inherits: `BrandedScene`
- Purpose: Solve the Ajay/Bina age problem.
- Uses: `ProblemBox`, `StepReveal`, `HighlightBox`
- Key beats:
  1. Reveal `ProblemBox` with the stem
  2. Reveal 4 steps, 0.8s apart
  3. Green `HighlightBox` around the final step
  4. Fade out

### Traps
- Inherits: `BrandedScene`
- Purpose: Call out the two biggest misconceptions.
- Uses: `FormulaBox`, `HighlightBox`
- Key beats:
  1. Show `3:4 + 2:5 = 5:9` in a FormulaBox, draw a red cross-out
  2. Show `\text{boys} = \tfrac{3}{2}` in a FormulaBox, draw a red cross-out
  3. Fade out

### Outro
- Inherits: `BrandedScene`
- Purpose: Recap + CTA.
- Uses: `title_card`
- Key beats:
  1. Fade in title card "Subscribe / Next: Mixtures & alligations"
  2. Hold 2s, fade out

## Render order
1. Intro
2. ScaleIsFree
3. MeansExtremes
4. WorkedExample
5. Traps
6. Outro

## Edit-bay notes
- Cross-fade between scenes in editor, not Manim.
- BG track at -20 dB under VO.
- VO takes named `NN_scene.wav` where `NN` matches shot number.

READY FOR MANIM CODE
