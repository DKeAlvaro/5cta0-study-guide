# U3 · Random variables and random processes: the multiple-choice facts

<div class="meta"><span class="hot">Rank 7 · 5.3 points over 9 sittings</span><span>0.3 to 0.5 p every exam</span><span>50 min</span></div>

!!! need "Before this page"
    [M6 expectation](maths.md#m6-expectation-and-variance-rules), [M3 the $\cos\alpha\cos\beta$ identity](maths.md#m3-complex-exponentials-and-cosine-identities) for the one computational question (Apr 2024 1d).

## The vocabulary in plain words

| Term | Plain words | Exam test |
|---|---|---|
| **random variable** | one number whose value is uncertain (a die roll, a weight, one pixel's colour) | "discrete" if its values can be listed (counts, phone numbers), "continuous" if any value in a range (time, weight) |
| **random process / random signal** | a whole sequence or function in time whose values are random; each run of the experiment gives one **realisation** $x_i[n]$; the set of all realisations is the **ensemble** | a picture is a realisation of a process; a pixel is a random variable |
| **expected value** $E[X]$ | the average of the outcomes weighted by their probabilities, $\sum_xx\,p(x)$ or $\int x\,p(x)dx$; the mean over infinitely many observations | not the most probable value, not the largest, not the simple or geometric average of the pmf |
| **variance, covariance, correlation** | variance $= E[(X-\mu)^2]$; covariance $= E[(X-\mu_X)(Y-\mu_Y)]$ (sign = direction of the relationship, size depends on units, no upper bound); correlation coefficient $= \text{cov}/(\sigma_X\sigma_Y)$ (between $-1$ and $1$, unit-free) | Oct 2021 1b: covariance has all three properties |
| **wide-sense stationary (WSS)** | the mean does not change with time **and** the autocorrelation $E[X(t)X(s)]$ depends only on the lag $t-s$ | Jun 2026 1d (b); anything about "all realisations", "pdf constant", "flat PSD" is a distractor |
| **ergodic (in the mean)** | the time average of **one** realisation equals the ensemble mean; needs stationarity | i.i.d. rolls of a die: ergodic in mean and variance; a random constant amplitude $A$ chosen once per realisation: not ergodic |
| **legitimate autocorrelation** | $r[l] = r[-l]$ (symmetric), $r[0]\ge|r[l]|$ (maximum at lag 0), $r[0]\ge0$ | Jan 2020 1a: reject any asymmetric sequence or one whose lag-0 value is not the largest |
| **cross-correlation** | $r_{xy}[\tau] = E[x[n]y[n-\tau]]$; for ergodic signals estimate it by a time average $\frac1N\sum_nx[n]y[n-\tau]$ | Nov 2019 1a |

!!! idea "The thing that confused me"
    "Ergodic" versus "stationary". Stationary is about the **ensemble**: statistics do not drift with time. Ergodic is about **one realisation**: watching one run long enough tells you the ensemble statistics. The classic non-ergodic process is $X(t) = A\cos t$ or "uniform between $-A$ and $A$" with $A$ drawn **once** per realisation: each run has its own fixed $A$, so a single run can never reveal the spread of $A$ across runs. Yet its mean can still be constant.

## Recipe for the computational variant (WSS and ergodic in the mean)

!!! recipe key "U3 · Is $X(t)$ WSS? Ergodic in the mean?"
    1. **Ensemble mean** $\mu(t) = E[X(t)]$: average over the random ingredient ($U$, $A$…) with $t$ fixed. Constant in $t$? If not → not WSS, and compare with step 3 anyway.
    2. **Autocorrelation** $R(t,s) = E[X(t)X(s)]$: use $\cos\alpha\cos\beta = \frac12[\cos(\alpha+\beta) + \cos(\alpha-\beta)]$; averages of $\cos(\cdot + 2U)$ over a full period vanish. Depends only on $t - s$? Then (with step 1) **WSS**.
    3. **Time average of one realisation** $\lim\frac1T\int_0^TX(t)dt$ with the random ingredient frozen. Equal to the ensemble mean of step 1 for every realisation? Then **ergodic in the mean**.

## Worked exam question, one step at a time

!!! exam "April 2024 · 1d · 0.3 p"
    For the following random processes, indicate if they are WSS and ergodic in the mean: 1. $X(t) = \cos(t + U)$, $U\sim\text{Uniform}(0, 2\pi)$. 2. $X(t) = A\cos(t)$, $A\sim N(1, 2)$. The following formula might be useful: $\cos(\alpha)\cos(\beta) = \frac{\cos(\alpha+\beta) + \cos(\alpha-\beta)}{2}$.

<div class="stepper" markdown>

**Step 1 · Process 1, mean.** $E[\cos(t+U)] = \int_0^{2\pi}\cos(t+u)\frac{1}{2\pi}du = \frac{1}{2\pi}[\sin(t+u)]_0^{2\pi} = \frac{1}{2\pi}(\sin(t+2\pi) - \sin t) = 0$. Constant (zero) for every $t$. ✓

**Now do step 2 yourself:** $E[\cos(t+U)\cos(s+U)]$ with the identity.

---

**Step 2 · Process 1, autocorrelation.** $\cos(t+U)\cos(s+U) = \frac12[\cos(t+s+2U) + \cos(t-s)]$. The first term averages to zero over $U$ (a full cosine period, as in step 1 with $2u$); the second does not contain $U$. $R(t,s) = \frac12\cos(t-s)$: depends on $t-s$ only. **WSS.**

**Now do step 3 yourself:** time average of one realisation with $U = u_0$ fixed.

---

**Step 3 · Process 1, time average.** $\frac1T\int_0^T\cos(t+u_0)dt = \frac{1}{T}[\sin(t+u_0)]_0^T$, bounded by $2/T\to0$. Equals the ensemble mean $0$. **Ergodic in the mean.**

**Now do all three steps for process 2 yourself.**

---

**Process 2.** Mean: $E[A\cos t] = E[A]\cos t = 1\cdot\cos t$: **depends on $t$** → not WSS (no need for the autocorrelation; for the record $R(t,s) = E[A^2]\cos t\cos s = (4+1)\cos t\cos s$, not a function of $t-s$ either; $E[A^2] = \sigma_A^2 + \mu_A^2 = 4 + 1$ by [M6](maths.md#m6-expectation-and-variance-rules)). Time average of one realisation: $\frac1T\int_0^Ta_0\cos t\,dt\to0$, while the ensemble mean is $\cos t$ (and even its own time average, 0, does not equal the ensemble mean at a given $t$). **Not ergodic in the mean.**

!!! answer "Answer"
    | Process | WSS | Ergodic in the mean |
    |---|---|---|
    | 1 | Yes | Yes |
    | 2 | No | No |

</div>

## Every past MC, with each option judged

!!! exam "June 2026 resit · 1d · 0.25 p"
    Which condition is required for a random process to be WSS? (a) Time averages of all realisations are strictly equal to ensemble averages. (b) Its mean is constant and its autocorrelation depends only on the time difference (lag). (c) Its pdf remains strictly constant over all time indices. (d) Its PSD is constant across all frequencies.

???+ solution "Solution"
    **(b)**. (a) is ergodicity. (c) is strict-sense stationarity (stronger than needed). (d) describes white noise.

!!! exam "April 2025 · 1d · 0.25 p (and January 2022 · 1c · 0.3 p)"
    Infinitely many fair dice; the process is the ensemble of the signals obtained by rolling each die infinitely many times. (a) ergodic, but only in the mean; (b) ergodic in both mean and variance; (c) $E[X[n]] = E[x_i[n]] = 0$; (d) stationary but not ergodic.

???+ solution "Solution"
    **(b)**: every roll is i.i.d., so one die's long-run average ($3.5$) and spread ($\frac{35}{12}$) equal the ensemble's. (c) is false because the mean is $3.5$, not $0$.

!!! exam "November 2022 · 1c · 0.25 p"
    A random number generator draws, for each realisation, infinitely many numbers uniformly between $-A$ and $A$, with $A\sim N(1, \sigma_A = 2)$. (a) not ergodic, mean 1; (b) ergodic, mean 1; (c) not ergodic, mean 0; (d) ergodic, mean 0.

???+ solution "Solution"
    Mean: for any $A$ the uniform on $[-A, A]$ has mean 0, so the ensemble mean is 0. Within one realisation $A$ is fixed and the samples are i.i.d. uniform, whose time average is $0$ = ensemble mean: ergodic in the mean (the key's reading of "ergodic"). **(d)**. (Not ergodic in the variance: each realisation has variance $A^2/3$, different from run to run.)

!!! exam "January 2022 resit · 1b · 0.3 p"
    Infinite set of pictures; each pixel's colour is an integer 0–255. (a) the colour of each pixel is a continuous RV; (b) each picture is a realisation of a random process, hence a random signal; (c) the set represents a WSS process; (d) each picture is a random process and the colour of a pixel is a realisation, hence a random signal.

???+ solution "Solution"
    **(b)**. (a) integers are discrete. (c) no information about stationarity. (d) a pixel is a random variable, not a signal.

!!! exam "October 2021 · 1b, 1c, 1d · 0.5 p each"
    **1b** The covariance of two RVs: (a) has no upper bound; (b) indicates the direction of the relationship; (c) is greatly influenced by scaling; (d) all of the above.

    **1c** Expected value of a discrete RV: (a) geometric average over outcomes; (b) weighted average over outcomes; (c) simple average; (d) integral of the pmf.

    **1d** A player makes 80 % of free throws. Probability of exactly 6 of the next 8? (a) 0.1468 (b) 0.3355 (c) 0.1678 (d) 0.2936

???+ solution "Solution"
    1b: **(d)** (the correlation coefficient is the bounded, scale-free version). 1c: **(b)** (Apr 2025 1b and Jan 2020 1d ask the same: "average of the outcomes weighted by the pmf" / "mean over an infinite number of observations"). 1d: binomial $\binom86 0.8^60.2^2 = 28\cdot0.262144\cdot0.04 = 28\cdot0.010486 = 0.2936$: **(d)**.

!!! exam "January 2019 · 1a · 0.5 p (two answers)"
    Which $X$ is discrete? A. weight of a random student; B. number of 4s in $n$ dice rolls; C. phone number of a person; D. travel time to university.

???+ solution "Solution"
    **B and C** (countable values). A and D are continuous.

!!! exam "January 2020 retake · 1a · 0.25 p"
    Which plotted sequences are legitimate autocorrelation functions? Options list combinations of $r_A, r_B, r_C, r_D$.

???+ solution "Solution"
    Test each plot: symmetric about $l = 0$, and $|r[l]|\le r[0]$ with $r[0]$ the maximum. The key's answer is **A: only $r_B[l]$**: the other three fail symmetry or have a lag with a value larger than $r[0]$. (The printed figure is not reproduced here; apply the two tests to whatever is drawn.)

## The flawed one: cross-correlation from plots (Nov 2019 1a · 1 p)

!!! exam "November 2019 · 1a"
    $x[n] = 1, 1, 1, 0$ and $y[n] = 1, 3, 3, 5$ for $n = 0..3$ (zero elsewhere). Assuming $x$ and $y$ ergodic, what is the cross-correlation $r_{xy}[\tau]$? Options give $r_{xy}[0..5]$ as A: $\frac54, -\frac84, \frac{11}{4}, -\frac74, 1, \frac14$; B: $\frac54, \frac84, \frac{11}4, \frac74, 1, \frac14$; C: $\frac54, -\frac84, \frac{13}4, \frac74$; D: $\frac54, \frac84, \frac{13}4, \frac74$.

???+ solution "Solution"
    Ergodic → time average with $N = 4$: $r_{xy}[\tau] = \frac14\sum_nx[n]y[n-\tau]$.
    $\tau = 0$: $x_0y_0 + x_1y_1 + x_2y_2 = 1 + 3 + 3 = 7 \to \frac74$. $\tau = 1$: $x_1y_0 + x_2y_1 + x_3y_2 = 1 + 3 + 0 = 4\to1$. $\tau = 2$: $x_2y_0 + x_3y_1 = 1\to\frac14$. $\tau = -1$: $x_0y_1 + x_1y_2 + x_2y_3 = 3 + 3 + 5 = 11\to\frac{11}4$. $\tau = -2$: $x_0y_2 + x_1y_3 = 8\to\frac84$. $\tau = -3$: $x_0y_3 = 5\to\frac54$.
    So the sequence from $\tau = -3$ to $2$ is $\frac54, \frac84, \frac{11}4, \frac74, 1, \frac14$: exactly option **B's numbers, shifted by 3** in the index. The official key says precisely that: "no correct answer; the closest is B, but it should be shifted by 3". No negative values can appear (all samples are non-negative), which eliminates A and C immediately; D has a $\frac{13}{4}$ that no overlap produces.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | "WSS means every realisation has the same time average" | That is ergodicity. WSS = constant mean + autocorrelation depending on the lag only. |
    | "$A\cos t$ with random $A$ is WSS because $A$ is random" | Its mean $E[A]\cos t$ moves with $t$. |
    | "Expected value = most probable value" | That is the mode. $E[X]$ is the probability-weighted average. |
    | "A pixel's colour (0–255) is continuous" | Integers: discrete. |
    | "Correlation and covariance are the same thing" | The correlation coefficient is covariance divided by both standard deviations: bounded by 1 and unit-free. |
    | Binomial without the $\binom{n}{k}$ | $\binom86 = 28$ ways to place the 6 successes. |

## True or false (from real MC options and fresh wording)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| A WSS process has a constant mean and an autocorrelation that depends only on the lag. | True | Jun 2026 1d (b). |
| For a WSS process the pdf must be the same at every time index. | False | Jun 2026 1d (c): that is strict-sense stationarity; WSS needs only two moments. |
| The process of i.i.d. fair-die rolls is ergodic in mean and variance. | True | Apr 2025 1d, Jan 2022 1c. |
| The covariance of two random variables is bounded between $-1$ and $1$. | False | Oct 2021 1b: that is the correlation coefficient; covariance has no bound. |
| For any random variable the CDF tends to 0 at $-\infty$ and to 1 at $+\infty$. | True | Nov 2019 1b (D). |
| The expected value of a discrete random variable is the integral of its pmf over its range. | False | Apr 2025 1b (c): it is $\sum_x x\,p(x)$. |
| $X(t) = \cos(t + U)$ with $U$ uniform on $[0, 2\pi)$ is WSS. | True | Apr 2024 1d. |

</div>

**You can leave this page when you can:**

- [ ] define random variable, realisation, ensemble, random process in one line each.
- [ ] state WSS and ergodic-in-the-mean and give the standard example of a non-ergodic WSS-looking process.
- [ ] run the three-step WSS/ergodic recipe on $\cos(t+U)$ and $A\cos t$.
- [ ] test a sequence for being a valid autocorrelation (symmetry, maximum at 0).
- [ ] compute a binomial probability with the $\binom nk$ factor.

*[realisation]: one particular outcome sequence of a random process.
*[ensemble]: the collection of all possible realisations.
*[WSS]: wide-sense stationary: constant mean, autocorrelation depending only on the lag.
*[ergodic]: time averages of one realisation equal ensemble averages.
