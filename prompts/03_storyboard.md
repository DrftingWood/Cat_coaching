# Prompt 03 — Storyboard Generator

Feed this prompt the script from prompt 02.

---

You convert a video script into a shot-by-shot storyboard and a list of Manim
scene classes to build.

**Output format — two sections, in this order:**

## 1. Storyboard table

```
| #  | Duration | Visual | VO line | Scene class | Notes |
```

- One row per continuous visual shot. Typical video has 10–25 rows.
- `Duration` is a clock range like `0:12-0:28`.
- `Visual` is one short sentence describing what's on screen.
- `VO line` is the spoken line during this shot (trim to fit the cell).
- `Scene class` is the Python class name in `scenes.py` that renders this
  visual. Reuse a class across rows if the class animates multiple beats.
- `Notes` is timing, cross-refs to audio takes, or anything the editor needs.

## 2. Scene class plan

For each unique `Scene class` from the table, a short spec:

```
### <ClassName>
- Inherits: BrandedScene
- Purpose: one-sentence role in the video
- Uses: [components and layout helpers it will import from `lib`]
- Key beats: numbered list of the animation beats inside `construct()`
```

Rules:
- Keep class names `PascalCase` and descriptive: `PercentIntuition`, not
  `Scene1`.
- Favor fewer, longer scenes over many tiny ones; a single `Solution` scene
  can host the whole worked example.
- Assume these components already exist in `lib`: `BrandedScene`, `ProblemBox`,
  `FormulaBox`, `HighlightBox`, `OptionRow`, `StepReveal`, `title_card`,
  `topic_banner`, `question_layout`, `two_pane_split`. Only invent a new
  helper if no combination of these fits — and explicitly flag any new helper.
- Do NOT write Python yet.

End with:

```
READY FOR MANIM CODE
```
