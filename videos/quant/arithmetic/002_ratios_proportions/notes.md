# Concept notes — Ratio & Proportion

## Intuition

A ratio is just a fair comparison between two quantities *of the same kind*.
When you say the ratio of boys to girls in a room is $3:2$, you are not
claiming there are exactly three boys and two girls — you are saying that for
every three boys you walk past, you walk past two girls. The actual count
could be 30 and 20, or 300 and 200. The *relationship* is what the ratio
freezes; the *scale* is free.

That one idea — "the ratio fixes the relationship, the scale is free" — is
the whole game. Once you see it, the so-called "k-method" is just giving that
free scale a name.

A proportion is an equation between two ratios. If I tell you the salary
ratio between Rohit and Priya is $3:4$, and also between Priya and Arjun is
$4:5$, I have given you a proportion that lets you combine ratios.

## Formalism

- A ratio of $a$ to $b$ is written $a:b$ and represents $\frac{a}{b}$.
- A proportion is $a:b = c:d$, equivalent to $\frac{a}{b} = \frac{c}{d}$, which
  means $a \cdot d = b \cdot c$. The first and last terms are called
  **extremes**; the middle two are **means**. "Product of means = product of
  extremes" is the one fact that powers 80% of CAT ratio questions.
- **k-method:** if $a:b = 3:4$, set $a = 3k$ and $b = 4k$ for some
  $k > 0$. Any condition in the problem (like "their sum is 35" or "the
  difference is 10") is now a one-variable equation in $k$.

## Why CAT tests this

CAT doesn't test whether you can multiply fractions; it tests whether you can
translate English into a proportion fast. A ratio problem almost never arrives
labelled "ratio problem" — it is camouflaged inside ages, salaries, mixtures,
speeds, or partnership profits. The examiner wants to see whether you
instinctively reach for the k-method the moment you see two quantities
compared.

## Canonical example

> The ratio of Ajay's age to Bina's age is $5:7$. Eight years from now, the
> ratio will be $3:4$. Find Bina's present age.

Apply the k-method. Let present ages be $5k$ and $7k$. Eight years later the
ages are $5k + 8$ and $7k + 8$, and their ratio is $3:4$, so

$$\frac{5k+8}{7k+8} = \frac{3}{4}.$$

Product of means equals product of extremes: $4(5k+8) = 3(7k+8)$, giving
$20k + 32 = 21k + 24$, so $k = 8$. Bina's present age is $7k = 56$.

## Shortcuts & heuristics

- Always set up the k-method before you touch anything. It turns messy
  word problems into one linear equation.
- "Product of means = product of extremes" is faster than cross-multiplying
  fractions because you do not have to simplify first.
- If the answer depends only on the *ratio* and not the absolute values,
  pick convenient numbers (like $k = 1$) and work with those. This
  drops whole lines of algebra.

## Common traps

1. **Adding ratios directly.** $3:4 + 2:5 \ne 5:9$. Ratios are not vectors;
   you must bring them to a common scale first.
2. **Confusing a ratio with a fraction of the whole.** If the boy-to-girl
   ratio is $3:2$, boys are $\frac{3}{5}$ of the total, not $\frac{3}{2}$.
3. **Forgetting that $k$ must be positive and consistent.** In multi-step
   problems, if two different conditions give different $k$ values, your
   setup is wrong.
4. **Proportionality with three or more quantities.** $a:b:c = 2:3:5$ means
   $a = 2k, b = 3k, c = 5k$, with *the same* $k$ everywhere.

## Prerequisites

- Basic fractions and cross-multiplication.
- Linear equations in one variable.

## Next natural topic

Mixtures and alligations — a direct application of ratios.

READY FOR SCRIPT
