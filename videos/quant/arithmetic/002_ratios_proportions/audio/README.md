# Voiceover — Ratio & Proportion

## Recording conventions

- `takes/` — raw recordings, one file per shot row in `../storyboard.md`.
- Naming: `NN_scene.wav` where `NN` is the shot number and `scene` is the
  scene class.
  - `01_intro.wav`, `02_intro.wav`, `03_intro.wav` (hook / goal / prereqs)
  - `04_scale_is_free.wav`
  - `05_means_extremes.wav`
  - `06_worked_example.wav`
  - `07_traps.wav`
  - `08_outro.wav`
- `final.wav` — mixed-down, normalized VO that will sit on the video
  timeline in the editor.

## Timing targets (from storyboard)

| # | Length | Shot            |
|---|--------|-----------------|
| 1 | 0:15   | Intro hook      |
| 2 | 0:15   | Learning goal   |
| 3 | 0:10   | Prereqs         |
| 4 | 0:45   | ScaleIsFree     |
| 5 | 0:35   | MeansExtremes   |
| 6 | 1:00   | WorkedExample   |
| 7 | 0:15   | Traps           |
| 8 | 0:15   | Outro + CTA     |

Total ≈ 3:30. If a take runs long, loosen `self.wait(...)` in
`../scenes.py` rather than rush the VO.

Raw `.wav` files are gitignored. Keep them locally or in cloud storage.
