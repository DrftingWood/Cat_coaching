# Cat_coaching

This repository is configured to run **Manim** in **GitHub Codespaces** for physics and math animations.

## What is included

- `.devcontainer/` configuration for Codespaces.
- `postCreate.sh` script that installs system dependencies Manim needs:
  - Cairo/Pango build dependencies
  - FFmpeg
  - Basic LaTeX toolchain for math rendering
- `requirements.txt` with Manim.
- `example_scene.py` as a starter animation.

## Run in Codespaces

1. Open this repository in GitHub.
2. Click **Code -> Codespaces -> Create codespace on work**.
3. Wait for the dev container to finish setup.

If setup completes successfully, Manim should already be installed.

## Create and render animations

Render the example scene:

```bash
manim -pqh example_scene.py HelloManim
```

Useful quality flags:

- `-ql` low quality (fast preview)
- `-qm` medium quality
- `-qh` high quality
- `-qk` 4K

Output videos are written inside `media/`.

## Typical workflow

1. Create a new Python file, for example `projectile_motion.py`.
2. Add one or more `Scene` classes.
3. Render a scene by class name:

```bash
manim -pql projectile_motion.py ProjectileMotionScene
```
