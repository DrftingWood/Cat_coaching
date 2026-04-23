# Making one video, end to end

The repo is designed so every video follows the same six steps. Each step has
a prompt you paste into any chatbot (ChatGPT, Claude, etc.) and a concrete
file output in this repo.

## Step 0 — Pick the topic

Open `docs/cat_syllabus.md` and pick the next topic. Create the folder:

```
videos/<section>/<topic>/NNN_slug/
```

where `NNN` is the next index **within that topic**. Copy the four files from
`templates/` into it and rename `scene_template.py` to `scenes.py`.

Also create the audio subfolder:

```
videos/<section>/<topic>/NNN_slug/audio/
videos/<section>/<topic>/NNN_slug/audio/takes/
```

## Step 1 — Concept explainer → teaching notes

Paste `prompts/01_concept_explainer.md` into your chatbot. Fill in `<TOPIC>`
and `<DIFFICULTY>`. Save the output as `notes.md` in the video folder. Review
and edit. This is the only creative step that really matters for accuracy — if
the explanation is wrong, everything downstream is wrong.

## Step 2 — Script writer → `script.md`

Paste `prompts/02_script_writer.md` with the notes as input. Save the output
as `script.md`. Read it aloud and time it. Edit until it sounds like you.

## Step 3 — Storyboard → `storyboard.md`

Paste `prompts/03_storyboard.md` with the script as input. Save as
`storyboard.md`. This is the bridge from words to pictures — make sure every
spoken beat has a matching visual row.

## Step 4 — Manim code → `scenes.py`

Paste `prompts/04_manim_code.md` with the storyboard as input. Replace the
contents of `scenes.py`. Render previews one scene at a time:

```
make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
```

Iterate with the chatbot until every scene renders cleanly.

## Step 5 — Voiceover

Record VO in the editor of your choice (Audacity, Reaper, etc.). Save takes
into `audio/takes/` as `NN_shot_name.wav`. Mix down to `audio/final.wav`.
Timestamps should align with the `Duration` column in `storyboard.md` — if
they drift, adjust `self.wait(...)` values in `scenes.py`, not the VO.

## Step 6 — Final render + upload

```
make high FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
make high FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Problem
# ...
```

Rendered files land in `media/`. Stitch scenes + VO in your editor, export,
upload. Use `prompts/05_thumbnail_ideas.md` for thumbnail concepts.

Check off items in the video's `notes.md` post-production list as you go.

## Tips

- Don't push Manim to do video editing. Scene cuts, cross-fades, VO mixing,
  background music — do those in your editor. Manim does animation, nothing
  more.
- When something looks ugly, first check whether `lib/components.py` already
  has a helper. If not, add one there rather than one-offing it in a video's
  `scenes.py`.
- When you change `lib/theme.py`, re-render the intro of a recent video to
  eyeball that the new palette still reads well.
