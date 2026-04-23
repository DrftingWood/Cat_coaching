# CAT coaching channel

Production repo for a YouTube channel that teaches CAT exam concepts
(Quant + LRDI) using Manim animations. Built to run inside GitHub
Codespaces / VS Code.

## Repo map

```
.devcontainer/    Codespaces image + postCreate (Manim, FFmpeg, LaTeX)
lib/              Shared Manim helpers — colors, layouts, components, BrandedScene
templates/        Starter files copied when you begin a new video
prompts/          Drop-in chatbot prompts (ChatGPT, Claude, etc.) for every stage
docs/             workflow, style guide, Manim cheat sheet, syllabus index
videos/           One folder per video, organised as videos/<section>/<topic>/NNN_slug/
assets/           Shared images, fonts, logos
media/            Manim render output (gitignored)
Makefile          preview / high / fourk / clean render shortcuts
```

## Open in Codespaces

1. On GitHub, click **Code → Codespaces → Create codespace on this branch**.
2. Wait for the container to build. It installs Manim, FFmpeg, LaTeX.
3. Verify it works:
   ```bash
   manim -pql example_scene.py HelloManim
   ```

## Make a new video (6 steps)

Full details in [`docs/workflow.md`](docs/workflow.md).

1. Pick the next topic from [`docs/cat_syllabus.md`](docs/cat_syllabus.md),
   create `videos/<section>/<topic>/NNN_slug/`, copy the four files from
   `templates/`, and create `audio/takes/`.
2. Paste `prompts/01_concept_explainer.md` into a chatbot → save output as
   `notes.md`.
3. Paste `prompts/02_script_writer.md` with the notes → save output as
   `script.md`.
4. Paste `prompts/03_storyboard.md` with the script → save output as
   `storyboard.md`.
5. Paste `prompts/04_manim_code.md` with the storyboard → replace
   `scenes.py`. Preview each scene:
   ```bash
   make preview FILE=videos/<section>/<topic>/NNN_slug/scenes.py SCENE=Intro
   ```
6. Record VO into `audio/takes/`, mix to `audio/final.wav`, final-render
   scenes with `make high`, stitch in your editor, upload.

A fully-populated example lives at
`videos/quant/arithmetic/001_percentages_basics/`. Render it:

```bash
make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
```

## Render shortcuts

```bash
make preview FILE=... SCENE=...   # -pql, fast preview
make high    FILE=... SCENE=...   # -pqh, high quality
make fourk   FILE=... SCENE=...   # -pqk, 4K
make clean                        # rm -rf media/
```

## Visual identity

Every video's `scenes.py` imports from `lib` — colors, fonts, components.
To restyle the whole channel, edit `lib/theme.py`. See
[`docs/style_guide.md`](docs/style_guide.md) for the palette and voice rules.

## Chatbot workflow

The `prompts/` folder contains vetted prompts for every stage of making a
video. They're plain markdown — paste into ChatGPT, Claude, Gemini, or any
chatbot. Each prompt specifies its expected input and output format so the
next stage's prompt can consume it unchanged.

## Reference

- `example_scene.py` — smoke-test Manim scene. Keep as a sanity check.
- [`docs/manim_cheatsheet.md`](docs/manim_cheatsheet.md) — common patterns.
- [`docs/style_guide.md`](docs/style_guide.md) — palette, typography, pacing.
- [`docs/cat_syllabus.md`](docs/cat_syllabus.md) — topic tree + publish order.
