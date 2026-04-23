# Prompt 02 — Script Writer

Feed this prompt the output of `01_concept_explainer.md` as context.

---

You convert a CAT concept explanation into a tight narratable video script.

**Input:** the concept explainer output (intuition, formalism, example, traps).

**Output:** a markdown document that exactly matches this template:

```
# Script: <video title>

- **Section / Topic:**
- **Target length:** 6–8 minutes
- **Difficulty:**
- **Learning goal (one sentence):**

## 1. Hook (0:00 – 0:20)
> VO:
> ANIMATION:

## 2. Learning goal (0:20 – 0:40)
> VO:
> ANIMATION:

## 3. Prereqs (0:40 – 1:00)

## 4. Core explanation (1:00 – 4:00)
### Idea 1: <name>
> VO:
> ANIMATION:
### Idea 2: <name>
> VO:
> ANIMATION:

## 5. Worked example (4:00 – 6:30)
> VO:
> ANIMATION:

## 6. Common traps (6:30 – 7:30)

## 7. Summary & CTA (7:30 – end)

## Animation hooks
- [ANIM: ...] tags inline in VO lines.
```

Rules:
- Every `> VO:` line is what the creator actually says. Write it as spoken
  English, contractions allowed, ~150 words per minute.
- Every `> ANIMATION:` line is a one-sentence description of what's on screen
  during that VO. Reference existing components by name when natural:
  `ProblemBox`, `FormulaBox`, `HighlightBox`, `OptionRow`, `StepReveal`,
  `title_card`, `topic_banner`, `question_layout`.
- Use `[ANIM: <description>]` tags inline inside VO lines whenever a beat needs
  a synced visual cue (e.g. `"...which equals [ANIM: highlight 42] forty-two."`).
- Do NOT write Manim Python code here. That's a later step.
- Keep every VO paragraph under 40 words so it reads naturally.
- Time hints in section headings are approximate — adjust if the content
  justifies it, but preserve the section order.

End with a line:

```
READY FOR STORYBOARD
```
