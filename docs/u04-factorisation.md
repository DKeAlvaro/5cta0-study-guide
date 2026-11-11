# U4 · Spectral factorisation: from a PSD in cos θ to the innovation filter

<div class="meta"><span class="hot">Rank 14 · 2.1 points over 5 sittings</span><span>0.4 p in Apr 2025 and Apr 2024, 0.75 p in Nov 2022, MC in Jun 2026</span><span>50 min</span></div>

!!! need "Before this page"
    [M3 the z version of cosines](maths.md#m3-complex-exponentials-and-cosine-identities) ($\cos\theta = \frac{z+z^{-1}}{2}$, $|1+az^{-1}|^2 \leftrightarrow (1+az^{-1})(1+az)$), [M7 minimum phase](maths.md#m7-the-z-domain-in-four-facts), [M8 quadratic formula](maths.md#m8-argmax-set-the-derivative-to-zero-quadratics). It is the reverse of [U14](u14-model-autocorr.md) step 2.

## The idea in plain words

You are given the PSD of a signal and asked which filter, fed with white noise, would produce it. The PSD is $\sigma_i^2|L(e^{j\theta})|^2$, and $|L|^2 = L(z)L(z^{-1})$: every factor $(1 + az^{-1})$ comes with its mirror $(1 + az)$. Your job is to rewrite the given expression in that mirrored form and then keep only the half with $z^{-1}$: that half is the **innovation filter** $L(z)$, and the constant left over is the noise variance.

!!! idea "The thing that confused me"
    A number like $61 + 60\cos\theta$ hides a product. Because $\cos\theta = \frac{z + z^{-1}}{2}$, it is $61 + 30z + 30z^{-1}$, and $(1 + az^{-1})(1 + az) = 1 + a^2 + a(z + z^{-1})$. So "$61 + 30(z + z^{-1})$" is "$C(1 + a^2) + Ca(z+z^{-1})$": two equations, $C(1+a^2) = 61$ and $Ca = 30$. Divide them and $C$ disappears, leaving a quadratic in $a$ whose two roots are $a$ and $1/a$. The one inside the unit circle is the minimum-phase choice.

## A tiny example with numbers

$P(e^{j\theta}) = 5 + 4\cos\theta$. Write $5 + 2(z + z^{-1}) = C(1+a^2) + Ca(z+z^{-1})$: $C(1+a^2) = 5$, $Ca = 2$. Divide: $\frac{1+a^2}{a} = \frac52 \Rightarrow 2a^2 - 5a + 2 = 0 \Rightarrow a = \frac{5\pm3}{4}$: $2$ or $\frac12$. Keep $a = \frac12$, then $C = 2/a = 4$. So $P = 4(1 + \frac12z^{-1})(1 + \frac12z)$: $\sigma_i^2 = 4$, $L(z) = 1 + \frac12z^{-1}$ (an MA(1)). Check: $4|1 + \frac12e^{-j\theta}|^2 = 4(1 + \frac14 + \cos\theta) = 5 + 4\cos\theta$. ✓

!!! question "Your turn"
    $P(e^{j\theta}) = \dfrac{1}{1.25 - \cos\theta}$. Find $a$, $C$, $\sigma_i^2$, $L(z)$.

    ???+ solution "Answer"
        Denominator $1.25 - \frac12(z+z^{-1}) = C(1 - az^{-1})(1 - az) = C(1+a^2) - Ca(z+z^{-1})$: $Ca = \frac12$, $C(1+a^2) = 1.25$; $\frac{1+a^2}{a} = 2.5 \Rightarrow 2a^2 - 5a + 2 = 0 \Rightarrow a = \frac12$, $C = 1$. $P = \dfrac{1}{(1 - \frac12z^{-1})(1 - \frac12z)}$: $\sigma_i^2 = \frac{1}{C} = 1$, $L(z) = \dfrac{1}{1 - \frac12z^{-1}}$ (an AR(1)).

## The formulas, every symbol named

<div class="key" markdown>

$$P_x(z) = \sigma_i^2\,L(z)\,L(z^{-1}),\qquad P_x(e^{j\theta}) = \sigma_i^2|L(e^{j\theta})|^2,\qquad \cos\theta = \frac{z + z^{-1}}{2}$$

$$\text{numerator or denominator of the form } \alpha + \beta\cos\theta = C(1 + a^2) + Ca(z + z^{-1}) \;\Rightarrow\; Ca = \tfrac{\beta}{2},\quad C(1+a^2) = \alpha$$

</div>

| Symbol | Meaning |
|---|---|
| $L(z)$ | innovation filter: causal, stable, **minimum phase** (poles and zeros inside the unit circle); white noise in → $x[n]$ out |
| $\sigma_i^2$ | variance of that white noise $=$ (numerator constant)/(denominator constant) after factoring |
| $a$ | the root inside the unit circle; its partner $1/a$ is the mirror and is discarded |
| $C$ | the scale pulled out of each factored polynomial |
| sign | $\alpha + \beta\cos\theta$ with $\beta > 0$ factors as $(1 + az^{-1})(1+az)$; with $\beta<0$ as $(1 - az^{-1})(1 - az)$, $a>0$ |

**Why minimum phase.** $L(z)$ must be invertible (so the noise can be recovered from the signal, "innovation") and causal and stable. Zeros or poles outside the unit circle break that. The quadratic always offers $a$ and $1/a$; exactly one is inside.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "find the spectral factorization of $x[n]$, that is the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$" | the full recipe below |
| "$P_x(e^{j\theta}) = \dfrac{7}{25 - 24\cos\theta}$" (a constant over a cosine) | only the denominator needs factoring; $L(z)$ is $1/(1 - az^{-1})$, an AR(1) |
| "$P_x = \dfrac{\frac{17}{8} - \cos\theta}{\frac{25}{16} + \frac32\cos\theta}$" | factor numerator and denominator separately: ARMA(1,1) |
| "which statement is true" with a factorisation printed (Jan 2022 1d) | $L(z)$ is the half with $z^{-1}$ only, with poles and zeros inside; $\sigma_i^2$ is the constant in front |
| "condition for $H(z)$ to be the innovation filter" (Jun 2026 1e) | minimum phase: all poles and zeros inside (or on) the unit circle |

## Recipe

!!! recipe key "U4 · Factor in six moves"
    1. **Replace** $\cos\theta$ by $\frac{z+z^{-1}}{2}$ in numerator and denominator: $\alpha + \beta\cos\theta \to \alpha + \frac\beta2 z + \frac\beta2 z^{-1}$.
    2. **Match** each polynomial to $C(1 \pm az^{-1})(1 \pm az) = C(1 + a^2) \pm Ca(z + z^{-1})$. Sign $+$ if $\beta > 0$, $-$ if $\beta<0$. Two equations: $Ca = |\beta|/2$ and $C(1+a^2) = \alpha$.
    3. **Divide** them: $\frac{1 + a^2}{a} = \frac{2\alpha}{|\beta|}$, i.e. $|\beta|a^2 - 2\alpha a + |\beta| = 0$. Quadratic formula ([M8](maths.md#m8-argmax-set-the-derivative-to-zero-quadratics)). Keep the root with $|a| < 1$; then $C = \frac{|\beta|}{2a}$.
    4. **Assemble**: $P_x(z) = \dfrac{C_n(1\pm bz^{-1})(1\pm bz)}{C_d(1\pm az^{-1})(1\pm az)}$. A plain constant numerator means $C_n = $ that constant and no zero.
    5. **Read off**: $\sigma_i^2 = C_n/C_d$; $L(z) = \dfrac{1\pm bz^{-1}}{1\pm az^{-1}}$ (the $z^{-1}$ halves).
    6. **Check**: expand $\sigma_i^2|L(e^{j\theta})|^2$ back into $\cos\theta$ with M3 and compare with the given PSD at $\theta = 0$.

## Worked exam question, one step at a time

!!! exam "April 2025 · 1e · 0.4 p"
    Random signal $x[n]$ has the following power spectral density: $P_x(e^{j\theta}) = \dfrac{1}{61 + 60 \cos \theta}$. Find the spectral factorization of $x[n]$, that is, the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$.

<div class="stepper" markdown>

**Step 1 · Replace.** $61 + 60\cos\theta = 61 + 30z + 30z^{-1}$. Numerator is the constant $1$: $C_n = 1$, no zeros.

**Now do step 2 yourself:** match $61 + 30(z + z^{-1})$ to $C(1 + a^2) + Ca(z+z^{-1})$ and write the two equations.

---

**Step 2 · Match.** $\beta = 60 > 0$, so the factor is $(1 + az^{-1})(1 + az)$. $C(1 + a^2) = 61$ and $Ca = 30$.

**Now do step 3 yourself:** divide, get the quadratic, solve, choose.

---

**Step 3 · Quadratic.** $\frac{1+a^2}{a} = \frac{61}{30} \Rightarrow 30a^2 - 61a + 30 = 0$. $\sqrt{61^2 - 4\cdot30\cdot30} = \sqrt{3721 - 3600} = \sqrt{121} = 11$. $a = \frac{61\pm11}{60}$: $\frac{72}{60} = 1.2$ or $\frac{50}{60} = \frac56$. Keep $a = \frac56$ (inside the unit circle; $1.2 = 1/(5/6)$ is its mirror). $C_d = \frac{30}{a} = 30\cdot\frac65 = 36$.

**Now do steps 4 and 5 yourself.**

---

**Steps 4 and 5 · Assemble and read off.** $P_x(z) = \dfrac{1}{36(1 + \frac56z^{-1})(1 + \frac56z)}$. $\sigma_i^2 = \frac{C_n}{C_d} = \frac{1}{36}$, $L(z) = \dfrac{1}{1 + \frac56z^{-1}}$.

**Step 6 · Check.** $\frac1{36}\cdot\frac{1}{|1 + \frac56e^{-j\theta}|^2} = \frac{1}{36(1 + \frac{25}{36} + \frac53\cos\theta)} = \frac{1}{36 + 25 + 60\cos\theta} = \frac{1}{61 + 60\cos\theta}$. ✓ Time domain: $x[n] = i[n] - \frac56x[n-1]$, an AR(1) with $\sigma_i^2 = 1/36$.

!!! answer "Answer"
    $L(z) = \dfrac{1}{1 + \frac56z^{-1}}$, $\sigma_i^2 = \dfrac{1}{36}$.

</div>

## Do it cold · 1

!!! exam "April 2024 · 1e · 0.4 p"
    $P(e^{j\theta}) = \dfrac{7}{25 - 24\cos(\theta)}$. Find the spectral factorization of $x[n]$: the coefficients of the innovation filter $L(z)$ and the variance of the input noise $\sigma_i^2$, so that $x[n]$ can be expressed as the output of the innovation filter when white noise with variance $\sigma_i^2$ is given as input.

???+ solution "Solution"
    **Step 1.** $25 - 24\cos\theta = 25 - 12z - 12z^{-1}$; numerator $C_n = 7$.

    **Step 2.** $\beta < 0$: factor $(1 - az^{-1})(1 - az) = 1 + a^2 - a(z+z^{-1})$. $C(1+a^2) = 25$, $Ca = 12$.

    **Step 3.** $12a^2 - 25a + 12 = 0$; $\sqrt{625 - 576} = 7$; $a = \frac{25\pm7}{24}$: $\frac43$ or $\frac34$. Keep $a = \frac34$; $C_d = \frac{12}{3/4} = 16$.

    **Steps 4, 5.** $P(z) = \dfrac{7}{16(1 - \frac34z^{-1})(1 - \frac34z)}$; $\sigma_i^2 = \frac{7}{16}$, $L(z) = \dfrac{1}{1 - \frac34z^{-1}}$.

    **Step 6.** $\frac{7}{16}\cdot\frac{1}{1 + \frac{9}{16} - \frac32\cos\theta} = \frac{7}{16 + 9 - 24\cos\theta} = \frac{7}{25 - 24\cos\theta}$. ✓ (This is the denominator of the Nov 2022 ARMA PSD $28\frac{1-\cos\theta}{25-24\cos\theta}$: same pole at $\frac34$.)

    !!! answer "Answer"
        $L(z) = \dfrac{1}{1 - \frac34z^{-1}}$, $\sigma_i^2 = \dfrac{7}{16}$.

## Do it cold · 2

!!! exam "November 2022 · 1d · 0.75 p"
    $P_x(e^{j\theta}) = \dfrac{1}{\frac53 - \cos(\theta)}$. Find the spectral factorization: the variance of the input noise $\sigma_i^2$ and the innovation filter $L(z)$.

???+ solution "Solution"
    **Steps 1, 2.** $\frac53 - \frac12(z + z^{-1}) = C(1+a^2) - Ca(z+z^{-1})$: $Ca = \frac12$, $C(1+a^2) = \frac53$. Numerator $1$: $C_n = 1$, $b = 0$.

    **Step 3.** $\frac{1+a^2}{a} = \frac{10}{3} \Rightarrow 3a^2 - 10a + 3 = 0$; $\sqrt{100 - 36} = 8$; $a = \frac{10\pm8}{6}$: $3$ or $\frac13$. Keep $\frac13$; $C_d = \frac{1/2}{1/3} = \frac32$. (The key lists both candidate pairs, $(\frac16, 3)$ and $(\frac32, \frac13)$, and picks the second for minimum phase.)

    **Steps 4, 5.** $P_x(z) = \dfrac{2}{3}\cdot\dfrac{1}{(1 - \frac13z^{-1})(1 - \frac13z)}$; $\sigma_i^2 = \frac{1}{3/2} = \frac23$, $L(z) = \dfrac{1}{1 - \frac13z^{-1}}$.

    !!! answer "Answer"
        $\sigma_i^2 = \frac23$, $L(z) = \dfrac{1}{1 - \frac13z^{-1}}$.

## Do it cold · 3 (MC on a printed factorisation)

!!! exam "January 2022 resit · 1d · 0.3 p"
    $P_x(e^{j\theta}) = \dfrac{\frac{17}{8} - \cos\theta}{\frac{25}{16} + \frac32\cos\theta}$ (corrected sign), factorized as $P_x = 2\dfrac{(1 - \frac14z)(1 - \frac14z^{-1})}{(1 + \frac34z)(1 + \frac34z^{-1})}$. Which statement is true?

    - a) The provided factorization does not represent the spectral factorization of $x[n]$.
    - b) The innovation filter is $L(z^{-1}) = \dfrac{1 - \frac14z}{1 + \frac34z}$.
    - c) The innovation filter is $L(z) = \dfrac{1 - \frac14z^{-1}}{1 + \frac34z^{-1}}$.
    - d) The input variance is $\sigma_i^2 = 1/2$.

???+ solution "Solution"
    Verify the factorisation: numerator $2(1 + \frac1{16} - \frac14(z+z^{-1}))\to$ over the $2$: $\frac{17}{16} - \frac12\cos\theta\cdot$… multiply by the leading 2: $\frac{17}{8} - \cos\theta$ ✓. Denominator $1 + \frac{9}{16} + \frac34(z+z^{-1}) = \frac{25}{16} + \frac32\cos\theta$ ✓. So (a) is false. The innovation filter is the $z^{-1}$ half: **(c)**, zero at $\frac14$ and pole at $-\frac34$, both inside. (b) is the mirror, maximum phase. (d): the constant in front is $\sigma_i^2 = 2$, not $\frac12$.

    !!! answer "Answer"
        (c).

## Do it cold · 4 (MC on the condition)

!!! exam "June 2026 resit · 1e · 0.25 p"
    Which condition is required for a discrete-time rational filter $H(z)$ to be the innovation filter obtained through the spectral factorisation of a given PSD $P_x(z)$?

    - (a) $H(z)$ must be a minimum-phase system, meaning all its poles and zeros must lie inside (or on) the unit circle.
    - (b) $H(z)$ must be a maximum-phase system, meaning all its poles and zeros must lie strictly outside the unit circle.
    - (c) $H(z)$ must have a purely real-valued impulse response with strict linear phase to avoid phase distortion.
    - (d) $H(z)$ must be an all-pass system to ensure that the power of the driving noise is perfectly preserved.

???+ solution "Solution"
    **(a)**. (b) is the discarded mirror. (c) linear phase is a filter-design property, irrelevant here. (d) an all-pass has $|H| = 1$ and could not shape any PSD.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $\cos\theta \to z + z^{-1}$ | $\cos\theta = \frac{z+z^{-1}}{2}$: $60\cos\theta \to 30z + 30z^{-1}$. |
    | $Ca = 60$ | $Ca$ equals **half** the cosine coefficient: $30$. |
    | Keeping $a = 1.2$ | Inside the unit circle only: $a = 5/6$. Write "minimum phase". |
    | $\sigma_i^2 = C_d$ | $\sigma_i^2 = C_n/C_d = 1/36$; the denominator constant goes *under*. |
    | $L(z) = (1 + az^{-1})(1 + az)$ | $L(z)$ is only the $z^{-1}$ half. |
    | Sign of $a$ flipped | $+\beta\cos\theta \to (1 + az^{-1})$; $-\beta\cos\theta \to (1 - az^{-1})$ with $a>0$. Check by expanding back. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| The innovation filter must be causal, stable and minimum phase. | True | Jan 2022 1d key; Jun 2026 1e (a). |
| For a PSD $\sigma_i^2 L(z)L(z^{-1})$, the factor $L(z^{-1})$ with zeros outside the unit circle is also a valid innovation filter. | False | It is maximum phase: not invertible causally. |
| The variance of the input noise is the constant multiplying the factorised PSD. | True | Jan 2022 1d (d) is wrong only because it says $\frac12$ instead of $2$. |
| A PSD of the form $1/(\alpha - \beta\cos\theta)$ corresponds to an AR(1) innovation filter. | True | Apr 2024 1e, Nov 2022 1d: one pole, no zero. |

</div>

**You can leave this page when you can:**

- [ ] rewrite $\alpha + \beta\cos\theta$ as $C(1+a^2) \pm Ca(z+z^{-1})$ and write the two equations.
- [ ] solve the quadratic and justify the root you keep in three words.
- [ ] read off $\sigma_i^2 = C_n/C_d$ and $L(z)$.
- [ ] check the result by expanding back with M3.

*[innovation filter]: the minimum-phase filter L(z) such that white noise through L(z) has the given PSD.
*[spectral factorisation]: writing a PSD as σ² L(z) L(1/z) with L minimum phase.
*[maximum phase]: all zeros and poles outside the unit circle; the mirror of minimum phase.
