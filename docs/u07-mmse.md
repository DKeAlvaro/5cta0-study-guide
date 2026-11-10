# U7 · MMSE: the posterior mean, one integral

<div class="meta"><span class="hot">Rank 17 · 2.7 points over 3 sittings</span><span>last asked Nov 2022 (0.5 p); its MC facts appear every year</span><span>45 min</span></div>

!!! need "Before this page"
    [U6 posterior](u06-map.md) (you need a normalised posterior), [M9 the handed-out integrals and evaluating at 0 and ∞](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty), [M6 expectation](maths.md#m6-expectation-and-variance-rules).

## The idea in plain words

MAP picks the single most plausible $\theta$. **MMSE** picks the *average* $\theta$ under the posterior: the value that, if you had to pay the squared error, costs least on average. For a symmetric posterior (a bell) the peak and the average coincide. For a skewed one they differ, and that difference is what the exam tests.

!!! idea "The thing that confused me"
    "Minimum mean square error estimator" sounds like an optimisation you have to carry out. You never do. The theorem is already done for you: the answer is **always** $E[\theta\mid\mathbf x]$, the mean of the posterior. Your only job is to compute one integral: $\int\theta\,p(\theta\mid\mathbf x)\,d\theta$.

## A tiny example with numbers

Posterior $p(\theta\mid x) = 2e^{-2\theta}$, $\theta\ge0$ (an exponential with rate 2).
$\hat\theta_{MMSE} = \int_0^\infty\theta\cdot2e^{-2\theta}d\theta$. From [M9](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty), $\int\theta e^{a\theta}d\theta = \left(\frac\theta a - \frac1{a^2}\right)e^{a\theta}$ with $a = -2$: antiderivative $2\left(-\frac\theta2 - \frac14\right)e^{-2\theta} = -(\theta + \tfrac12)e^{-2\theta}$. Upper limit: $0$. Lower limit: $-(0+\frac12)\cdot1 = -\frac12$. Subtract: $0 - (-\frac12) = \frac12$. So $\hat\theta_{MMSE} = 0.5$, while the MAP of $2e^{-2\theta}$ is at $\theta = 0$ (the peak is at the left edge). Skewed posterior → different answers.

!!! question "Your turn"
    Posterior $p(\theta\mid x) = 3e^{-3\theta}$, $\theta\ge0$. MMSE? MAP?

    ???+ solution "Answer"
        Same steps with rate 3: $\hat\theta_{MMSE} = 1/3$; MAP $= 0$. (Rule: the mean of an exponential with rate $r$ is $1/r$.)

## The formulas, every symbol named

<div class="key" markdown>

$$\hat\theta_{MMSE} = E[\theta\mid\mathbf x] = \int_{-\infty}^{\infty}\theta\,p(\theta\mid\mathbf x)\,d\theta \qquad\text{(discrete unknown: } \hat X_{MMSE} = \sum_x x\,P[X = x\mid Y]\text{)}$$

</div>

| Symbol | Meaning |
|---|---|
| $p(\theta\mid\mathbf x)$ | posterior pdf, **properly normalised** (area 1). If you only have "$\propto$", divide by $\int(\ldots)d\theta$ first |
| $E[\theta\mid\mathbf x]$ | conditional mean: average of $\theta$ weighted by the posterior |
| limits | the range where the posterior is nonzero ($0$ to $\infty$, $0$ to $2$, …) |

**Where it comes from.** Bayes risk with quadratic cost $C(e) = e^2$ is $E[(\hat\theta-\theta)^2]$; differentiating in $\hat\theta$ and setting to zero gives $\hat\theta = E[\theta\mid\mathbf x]$. That is all the exam ever wants you to say about the derivation.

**Handy means.** Beta$(a,b)$: $\frac{a}{a+b}$. Gamma$(a,\text{rate }b)$: $\frac ab$. Exponential rate $r$: $\frac1r$. Gaussian: its centre.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "find the minimum mean square error estimator" | compute $\int\theta\,p(\theta\mid x)d\theta$ with the posterior given or derived in the previous sub-question |
| "you can use the identity $\int x^2e^{-x}dx = \ldots$" | the integrand after substitution will be exactly that; substitute $y = (x+a)\theta$ |
| "first provide the formula, specifying each probability distribution explicitly" | write $\hat\theta = \frac{\int\theta\,p(x\mid\theta)p(\theta)d\theta}{\int p(x\mid\theta)p(\theta)d\theta}$ with the actual pdfs plugged in, limits included |
| "find $\hat X_{MMSE}$ of $X$ given $Y$" with $X\in\{+1,-1\}$ | $(+1)P[X=1\mid Y] + (-1)P[X=-1\mid Y]$, then simplify (often to a tanh) |
| "MMSE for $c = \frac12$ and $c = \frac34$" (mixture posterior) | integrate term by term; each Gaussian term contributes (weight × centre) |

## Recipe

!!! recipe key "U7 · Posterior mean"
    1. **Get a normalised posterior.** If the question gives $p(\theta\mid x)$, use it. If you only have likelihood × prior, the posterior is $\frac{p(x\mid\theta)p(\theta)}{\int p(x\mid\theta)p(\theta)d\theta}$: compute the denominator integral once.
    2. **Multiply by $\theta$** inside the integral and write the limits (where the posterior lives).
    3. **Match a handed-out integral.** Substitute if needed: for $\int_0^\infty\theta^2e^{-c\theta}d\theta$ put $y = c\theta$, $d\theta = dy/c$, so it becomes $\frac{1}{c^3}\int_0^\infty y^2e^{-y}dy = \frac{2}{c^3}$.
    4. **Evaluate**: antiderivative, upper limit (usually 0 for $e^{-\infty}$), lower limit, subtract ([M9](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty)).
    5. **Sanity**: the result must lie inside the range of $\theta$ and, for a right-skewed posterior, above the MAP.

## Worked exam question, one step at a time

!!! exam "November 2022 · 2f · 0.5 p"
    Assume that the parameter $\theta \geq 0$ is a random variable that admits an exponential distribution with pdf $p(\theta) = ae^{-a\theta}$. The likelihood of the observation $x \geq 0$ is $p(x|\theta) = \theta e^{-\theta x}$. Using Bayes' theorem, the posterior distribution for $\theta$ after observing $x$ is $p(\theta|x) = (x+a)^2 \theta e^{-(x+a)\theta}$ for $\theta \geq 0$ (0 else). Find the minimum-mean square error estimator. Hint: you can use the identity $\int x^2 e^{-x} dx = -e^{-x}(x^2 + 2x + 2)$, obtained by integration by parts twice.

<div class="stepper" markdown>

**Step 1 · Posterior is given and normalised** (check: $(x+a)^2\int_0^\infty\theta e^{-(x+a)\theta}d\theta = (x+a)^2\cdot\frac{1}{(x+a)^2} = 1$; the mean of an exponential with rate $c$ is $1/c$, and $\int_0^\infty\theta e^{-c\theta}d\theta = 1/c^2$).

**Now do step 2 yourself:** write $\hat\theta$ as an integral with limits.

---

**Step 2 · Multiply by $\theta$.** $\hat\theta_{MMSE} = \int_0^\infty\theta\,(x+a)^2\theta e^{-(x+a)\theta}d\theta = (x+a)^2\int_0^\infty\theta^2e^{-(x+a)\theta}d\theta$.

**Now do step 3 yourself:** substitute $y = (x+a)\theta$ so that the integral matches the hint. What do $\theta^2$ and $d\theta$ become?

---

**Step 3 · Substitute.** $y = (x+a)\theta \Rightarrow \theta = \frac{y}{x+a}$, $\theta^2 = \frac{y^2}{(x+a)^2}$, $d\theta = \frac{dy}{x+a}$. Limits stay $0$ to $\infty$. So

$$\hat\theta = (x+a)^2\int_0^\infty\frac{y^2}{(x+a)^2}e^{-y}\frac{dy}{x+a} = \frac{1}{x+a}\int_0^\infty y^2e^{-y}dy.$$

**Now do step 4 yourself:** evaluate $\int_0^\infty y^2e^{-y}dy$ with the hint.

---

**Step 4 · Evaluate.** Antiderivative: $-e^{-y}(y^2+2y+2)$. Upper limit $y\to\infty$: $e^{-y}$ kills the polynomial, $0$. Lower limit $y = 0$: $-e^{0}(0+0+2) = -2$. Subtract: $0-(-2) = 2$. So $\hat\theta_{MMSE} = \frac{2}{x+a}$.

**Step 5 · Sanity.** Positive, and larger than the MAP $\frac{1}{x+a}$ of the same posterior (U6, do it cold 4): correct for a right-skewed posterior.

!!! answer "Answer"
    $\hat\theta_{MMSE} = \dfrac{2}{x+a}$.

</div>

## Do it cold · 1 (discrete unknown)

!!! exam "January 2022 resit · 2g · 0.6 p"
    Find the minimum mean square error estimate $\hat{X}_{\text{MMSE}}$ of $X$ given $Y$ (with $X\in\{+1,-1\}$ equiprobable, $Y = X + N$, $N\sim\mathcal N(0,\sigma^2)$). If you were not able to solve 2f you can use $P[X = 1|Y] = \frac{1}{e^{-\frac{y}{\sigma^2}} \left( e^{\frac{y}{\sigma^2}} + e^{-\frac{y}{\sigma^2}} \right)}$ and $P[X = -1|Y] = \frac{1}{e^{\frac{y}{\sigma^2}} \left( e^{\frac{y}{\sigma^2}} + e^{-\frac{y}{\sigma^2}} \right)}$. Useful identity: $\frac{e^{2u} - 1}{e^{2u} + 1} = \frac{e^u - e^{-u}}{e^u + e^{-u}} = \tanh(u)$.

???+ solution "Solution"
    **Step 2 (discrete).** $\hat X = (+1)P[X=1\mid Y] + (-1)P[X=-1\mid Y]$. With the posteriors from U6 (do it cold 6), writing $E_+ = e^{-(y-1)^2/(2\sigma^2)}$ and $E_- = e^{-(y+1)^2/(2\sigma^2)}$: $\hat X = \dfrac{E_+ - E_-}{E_+ + E_-}$.

    **Simplify.** Divide top and bottom by $E_-$: $\dfrac{E_+/E_- - 1}{E_+/E_- + 1}$, and $E_+/E_- = e^{[(y+1)^2 - (y-1)^2]/(2\sigma^2)} = e^{4y/(2\sigma^2)} = e^{2y/\sigma^2}$. So $\hat X = \dfrac{e^{2y/\sigma^2} - 1}{e^{2y/\sigma^2} + 1} = \tanh\!\left(\dfrac{y}{\sigma^2}\right)$ by the identity with $u = y/\sigma^2$.

    !!! answer "Answer"
        $\hat X_{MMSE} = \tanh(y/\sigma^2)$: a soft version of the MAP decision ($\pm1$ at $y\gtrless0$); for small $|y|$ it hedges near 0.

## Do it cold · 2 (uniform prior, both integrals by hand)

!!! exam "January 2019 · 2b · 1 p"
    $p(x\mid\lambda) = \lambda e^{-\lambda x}$ and prior $p(\lambda) = \frac12$ on $0\le\lambda\le2$. (1) Provide the formula for the Bayesian MMSE, specifying each distribution explicitly. (2) Determine the Bayesian MMSE (one observation $x$). Useful integrals: $\int e^{ax}dx = \frac1ae^{ax}$, $\int xe^{ax}dx = (\frac xa - \frac1{a^2})e^{ax}$, $\int x^2e^{ax}dx = (\frac{x^2}a - \frac{2x}{a^2} + \frac2{a^3})e^{ax}$.

???+ solution "Solution"
    **(1) Formula.** $\hat\lambda_{MMSE} = \int\lambda\,p(\lambda\mid x)d\lambda = \dfrac{\int_0^2\lambda\cdot\lambda e^{-\lambda x}\cdot\frac12\,d\lambda}{\int_0^2\lambda e^{-\lambda x}\cdot\frac12\,d\lambda}$: numerator = $\int\lambda\,p(x\mid\lambda)p(\lambda)$, denominator = evidence $p(x)$. The $\frac12$ cancels.

    **(2) Denominator.** $\int_0^2\lambda e^{-\lambda x}d\lambda$ with $a = -x$: antiderivative $\left(\frac{\lambda}{-x} - \frac{1}{x^2}\right)e^{-\lambda x} = -\left(\frac\lambda x + \frac1{x^2}\right)e^{-\lambda x}$. At $2$: $-\left(\frac2x + \frac1{x^2}\right)e^{-2x}$. At $0$: $-\frac{1}{x^2}$. Subtract: $D = \frac{1}{x^2} - \left(\frac2x + \frac1{x^2}\right)e^{-2x} = \frac{1 - (2x+1)e^{-2x}}{x^2}$.

    **Numerator.** $\int_0^2\lambda^2e^{-\lambda x}d\lambda$: antiderivative $\left(\frac{\lambda^2}{-x} - \frac{2\lambda}{x^2} + \frac{2}{-x^3}\right)e^{-\lambda x} = -\left(\frac{\lambda^2}{x} + \frac{2\lambda}{x^2} + \frac{2}{x^3}\right)e^{-\lambda x}$. At $2$: $-\left(\frac4x + \frac4{x^2} + \frac2{x^3}\right)e^{-2x}$. At $0$: $-\frac{2}{x^3}$. Subtract: $N = \frac{2 - (4x^2 + 4x + 2)e^{-2x}}{x^3}$.

    **Ratio.** $\hat\lambda = \frac{N}{D} = \dfrac{2 - (4x^2+4x+2)e^{-2x}}{x\left[1 - (2x+1)e^{-2x}\right]} = \frac2x - \dfrac{4x\,e^{-2x}}{1 - (2x+1)e^{-2x}}$ (split the numerator as $2[1-(2x+1)e^{-2x}] - 4x^2e^{-2x}$).

    !!! answer "Answer"
        $\hat\lambda_{MMSE} = \dfrac{2 - (4x^2+4x+2)e^{-2x}}{x\left[1-(2x+1)e^{-2x}\right]}$. Sanity: for large $x$ the exponentials vanish and $\hat\lambda\to 2/x$, the mean of a Gamma(2, rate $x$) posterior on an unbounded range. (The 2019 key prints $2x$ instead of $4x$ in the second term; the version here is verified symbolically in `scripts/verify.py`.)

## Do it cold · 3 (from the review deck: mixture posterior)

!!! exam "Exam Q3 2022-23 · 2f (review deck)"
    Posterior $p(\theta\mid x) = \frac{c}{\sqrt{2\pi}}\exp[-\frac12(\theta-x)^2] + \frac{1-c}{\sqrt{2\pi}}\exp[-\frac12(\theta+x)^2]$. Find the MMSE estimator for $c = \frac12$ and $c = \frac34$. Hint: $\int_{-\infty}^{\infty}xe^{-a(x-b)^2}dx = b\sqrt{\pi/a}$.

???+ solution "Solution"
    Each term is a Gaussian with unit variance: the first centred at $+x$ with weight $c$, the second at $-x$ with weight $1-c$. The mean of a Gaussian is its centre, so $E[\theta\mid x] = c\cdot x + (1-c)\cdot(-x) = x(2c-1)$. With the hint: $a = \frac12$, $b = \pm x$, $\sqrt{\pi/a} = \sqrt{2\pi}$ cancels the $\frac{1}{\sqrt{2\pi}}$.

    !!! answer "Answer"
        $c = \frac12$: $\hat\theta_{MMSE} = 0$ (halfway between two equal bumps, where the posterior is tiny: least squared error is not the most plausible value). $c = \frac34$: $\hat\theta_{MMSE} = x/2$. The MAP is the higher bump: undefined/either for $c=\frac12$, $+x$ for $c = \frac34$.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $\hat\theta_{MMSE} = \int\theta\,p(x\mid\theta)p(\theta)d\theta$ | Divide by the evidence $\int p(x\mid\theta)p(\theta)d\theta$, or use the normalised posterior. |
    | Forgetting $d\theta = dy/(x+a)$ in the substitution | Every substitution changes three things: the variable, the differential, the limits. |
    | $[-e^{-y}(y^2+2y+2)]_0^\infty = 0$ | Lower limit gives $-2$; the result is $0 - (-2) = 2$. |
    | MMSE of a Beta posterior $= \frac{a-1}{a+b-2}$ | That is the MAP. The mean is $\frac{a}{a+b}$. |
    | For $X\in\{\pm1\}$, writing an integral | Discrete: $E[X\mid Y] = \sum_x xP[X=x\mid Y]$, two terms. |
    | "MMSE and MAP always differ" (an MC option) | They coincide for symmetric posteriors (Gaussian); they differ for skewed ones. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| In Bayesian estimation, the minimum mean square error estimator is the mean of the posterior pdf. | True | Apr 2024 2b (a), Jan 2022 2d (b). |
| In Bayesian estimation, the minimum mean square error estimator is the maximum of the posterior pdf. | False | Apr 2024 2b (b): the maximum is the MAP. |
| The MMSE estimator and the MAP estimator will always result in a different estimate. | False | Apr 2025 2a (c), Apr 2024 2b (c), Jan 2022 2d (c): for a Gaussian posterior they coincide. *Always* is the swapped word. |
| The MMSE estimate results from minimising the (mean) square error. | True | Apr 2025 2a (b). |
| The invariance property (estimate a transformed parameter, map back) holds for the MMSE estimator. | False | Review deck: $E[g(\alpha)\mid x]\ne g(E[\alpha\mid x])$; the trick is valid for ML and LS only. |

</div>

**You can leave this page when you can:**

- [ ] write the MMSE as one integral with the right limits and a normalised posterior.
- [ ] substitute $y = c\theta$ and track $d\theta$ and the limits.
- [ ] evaluate $\int_0^\infty y^2e^{-y}dy = 2$ from the antiderivative, showing both limits.
- [ ] compute $E[X\mid Y]$ for a two-valued $X$ and reduce it to a tanh.
- [ ] say when MAP and MMSE coincide and when they do not.

*[MMSE]: minimum mean square error estimator: the posterior mean.
*[evidence]: p(x), the integral of likelihood × prior over the parameter; it normalises the posterior.
*[skewed]: a pdf with a longer tail on one side, so its mean and its peak are at different places.
