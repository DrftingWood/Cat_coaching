# Storyboard: <video title>

Each row = one continuous shot. The "Scene class" column names the Manim
`Scene` subclass in `scenes.py` that produces the visual.

| #  | Duration | Visual                                  | VO line                          | Scene class   | Notes                          |
|----|----------|-----------------------------------------|----------------------------------|---------------|--------------------------------|
| 1  | 0:00-0:08 | Title card fades in, topic banner      | "Hey, it's <channel>..."         | Intro         | Match VO take 01               |
| 2  | 0:08-0:25 | Problem box writes in                  | "Here's today's question..."     | Problem       |                                |
| 3  | 0:25-1:20 | Steps reveal one by one                | Solution narration               | Solution      | Sync pauses to step reveals    |
| 4  | 1:20-1:40 | Outro card with CTA                    | "If this helped, subscribe..."   | Outro         |                                |

## Render order
1. Intro
2. Problem
3. Solution
4. Outro

## Edit-bay notes
- Background track fades to -20 dB during VO.
- Cross-fade between scenes in editor (not in Manim) to keep renders clean.
