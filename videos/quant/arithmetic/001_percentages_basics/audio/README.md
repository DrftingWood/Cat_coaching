# Voiceover conventions

- `takes/` — raw recorded takes, one file per shot. Name them
  `NN_shot_name.wav` where `NN` matches the storyboard shot number.
- `final.wav` — the mixed-down, cleaned VO that will sync to the stitched
  video in your editor.
- Timestamps in takes should align with the `Duration` column in
  `../storyboard.md`. If they drift, adjust `self.wait(...)` values in
  `../scenes.py` rather than re-recording.

Raw `.wav` files are gitignored (see root `.gitignore`). Keep them locally or
in cloud storage; this folder tracks only the README and structure.
