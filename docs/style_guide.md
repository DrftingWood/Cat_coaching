# Channel style guide

This is the human-readable mirror of `lib/theme.py` plus voice/pacing rules.

## Palette

| Role     | Hex      | Used for                                       |
|----------|----------|------------------------------------------------|
| PRIMARY  | #1F6FEB  | Titles, primary stroke, topic banner text     |
| ACCENT   | #F5A623  | Highlights, option labels, call-outs          |
| CORRECT  | #2ECC71  | Correct answer, success state                 |
| WRONG    | #E74C3C  | Wrong answer, common trap flag                |
| NEUTRAL  | #8E9AA8  | Secondary text, axes, grid lines              |
| BG       | #101418  | Scene background (dark mode only — bright rooms look bad with light BG) |
| SURFACE  | #1B2129  | Card fills (ProblemBox, OptionRow)            |
| TEXT     | #F5F7FA  | Primary on-screen text                        |
| MUTED    | #B7C0CC  | Subtitles, captions, hint text                |

Never hard-code hex values in a video's `scenes.py`. Import from `lib.theme`.

## Typography

- Title: 56pt, bold, PRIMARY.
- Subtitle: 36pt, MUTED.
- Body: 32pt, TEXT.
- Caption: 24pt, MUTED.

Keep at most **one** font family. The default `sans-serif` is a placeholder —
pick a free Google font (Inter, Manrope, Source Sans 3) and update both
`lib/theme.py::FONT_FAMILY` and `assets/fonts/` once decided.

## Voice

- Second person ("you"), never "one" or "the student".
- Contractions OK.
- Short sentences. Long sentences only when a proof chain demands it.
- Name the CAT examiner's intent: "examiners give you this wrinkle because...".

## Pacing

- 150 words per minute spoken. Write accordingly.
- Every visual beat holds for ≥ 1 second. Do not flash info.
- Every scene should have at least one deliberate pause (`self.wait(1.5)`)
  so the viewer can process.

## On-screen density

- Max **one** big idea per shot. If you have two, split the shot.
- Max **5 lines** of text visible at once. If you need more, use `StepReveal`
  and reveal incrementally.
- Problem statements go in a `ProblemBox`. Raw `Text` directly on the
  background is only for titles and one-liners.

## What NOT to do

- No rainbow colors. The palette above is the whole palette.
- No animations that reverse direction for no reason — every motion should
  carry meaning.
- No walls of LaTeX. Break long derivations into `StepReveal` steps.
