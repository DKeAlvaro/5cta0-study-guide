# U6 · Posterior and MAP: prior × likelihood, then maximise

<div class="meta"><span class="hot">Rank 2 · 7.6 points over 8 sittings</span><span>2 p in Jun 2026, 1.5 p in Apr 2024</span><span>90 min</span></div>

!!! need "Before this page"
    [U5 MLE](u05-mle.md) (the six steps are reused unchanged), [M1 ln rules](maths.md#m1-exponents-and-logarithms), [M9 integrals](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty) only if you must normalise.

## The idea in plain words

Maximum likelihood listens only to the data. **Bayesian** estimation also listens to what you believed before the data arrived: the **prior** pdf of $\theta$. Multiply "how plausible is $\theta$ before" by "how well does $\theta$ explain the data" and you get "how plausible is $\theta$ now": the **posterior**. The **MAP** estimate is the $\theta$ where the posterior peaks. Mechanically: multiply prior and likelihood, drop constants, then run the MLE six steps on the product.

!!! idea "The thing that confused me"
    The posterior formula has a denominator $p(x)$ that looks scary. It is a **number** (it does not contain $\theta$), so for the MAP you can ignore it completely: $\arg\max_\theta$ of $\frac{\text{stuff}(\theta)}{\text{number}}$ is the $\arg\max$ of stuff$(\theta)$. You only compute it if the exam asks for the posterior *as a proper pdf* or for the MMSE ([U7](u07-mmse.md)).

## A tiny example with numbers

Coin with unknown $P(\text{heads}) = \theta$. Data: 3 heads, 1 tail. Prior: $p(\theta)\propto\theta(1-\theta)$ (you think fair-ish).

1. Likelihood: $\theta^3(1-\theta)^1$. Prior: $\theta^1(1-\theta)^1$.
2. Posterior $\propto \theta^{3+1}(1-\theta)^{1+1} = \theta^4(1-\theta)^2$.
3. $\ln$: $4\ln\theta + 2\ln(1-\theta)$. Derivative: $\frac4\theta - \frac{2}{1-\theta} = 0 \Rightarrow 4(1-\theta) = 2\theta \Rightarrow 4 = 6\theta \Rightarrow \hat\theta_{MAP} = \frac23 = 0.667$.

The MLE would be $3/4 = 0.75$ (same steps without the prior). The prior, peaked at $0.5$, pulled the estimate from $0.75$ toward $0.5$.

!!! question "Your turn"
    Same prior, but now 30 heads and 10 tails. Posterior exponents? $\hat\theta_{MAP}$? Compare with the MLE $30/40 = 0.75$.

    ???+ solution "Answer"
        Posterior $\propto\theta^{31}(1-\theta)^{11}$; $\frac{31}{\theta} = \frac{11}{1-\theta} \Rightarrow 31 - 31\theta = 11\theta \Rightarrow \hat\theta = 31/42 = 0.738$. Much closer to $0.75$: with more data the prior matters less. That is the sentence Jun 2026 2d asks you to write.

## The formulas, every symbol named

<div class="key" markdown>

$$p(\theta\mid\mathbf x) = \frac{p(\mathbf x\mid\theta)\,p(\theta)}{p(\mathbf x)} \;\propto\; p(\mathbf x\mid\theta)\,p(\theta), \qquad \hat\theta_{MAP} = \arg\max_\theta\,p(\theta\mid\mathbf x) = \arg\max_\theta\left[\ln p(\mathbf x\mid\theta) + \ln p(\theta)\right]$$

</div>

| Symbol | Meaning |
|---|---|
| $p(\theta)$ | prior: pdf of $\theta$ before seeing data (Beta, Gamma, exponential, uniform… given in the question) |
| $p(\mathbf x\mid\theta)$ | likelihood, the product over the samples as in [U5](u05-mle.md) |
| $p(\theta\mid\mathbf x)$ | posterior: pdf of $\theta$ after the data |
| $p(\mathbf x)$ | evidence $= \int p(\mathbf x\mid\theta)p(\theta)\,d\theta$: a number that makes the posterior integrate to 1 |
| $\propto$ | "proportional to": equal up to a factor that does not contain $\theta$ |
| $\hat\theta_{MAP}$ | maximum a posteriori: the mode (peak) of the posterior |

**Two shapes to recognise** (they save all the calculus):

| If the posterior looks like | it is | and its peak (MAP) is |
|---|---|---|
| $\theta^{a-1}(1-\theta)^{b-1}$ on $0<\theta<1$ | Beta$(a,b)$ | $\dfrac{a-1}{a+b-2}$ |
| $\lambda^{a-1}e^{-b\lambda}$ on $\lambda>0$ | Gamma$(a, \text{rate } b)$ | $\dfrac{a-1}{b}$ |

Both come from "derivative of the $\ln$ = 0": for Beta, $\frac{a-1}{\theta} - \frac{b-1}{1-\theta} = 0$; for Gamma, $\frac{a-1}{\lambda} - b = 0$. Always show that line in the exam, then quote the result.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "assume a Beta / Gamma / exponential prior on $\theta$" | that is $p(\theta)$; write it down with the given numbers |
| "write the likelihood function for $\theta$" | [U5](u05-mle.md) step 1: product over the data, numbers plugged in |
| "derive the posterior distribution for $\theta$" | multiply likelihood by prior, keep the $\theta$ factors, name the family and its new parameters |
| "compute the MAP estimate" | peak of the posterior: $\ln$, differentiate, zero, solve (or the shape shortcut) |
| "compare the MAP with the MLE and explain the effect of the prior" | compute both numbers; the prior pulls the MAP toward the prior's own peak; more data → MAP → MLE |
| "the posterior takes the form $\ldots$" | the posterior is handed to you: skip straight to the maximisation |
| "find a threshold $y_{th}$ such that the decision on $X$ depends on whether it is exceeded" (discrete $X$) | compare the two posterior probabilities; their ratio $\gtrless1$ reduces to $y\gtrless y_{th}$ |
| "evaluate the a posteriori probabilities $P[X = 1\mid Y]$" | Bayes with a sum (not an integral) in the denominator: $P[Y\mid X=1]P[X=1]/\sum_x P[Y\mid x]P[x]$ |

## Recipe

!!! recipe key "U6 · Posterior, then MAP"
    1. **Likelihood** $p(\mathbf x\mid\theta)$ as a product; plug in the data numbers if given ($\sum x_i$, $n$).
    2. **Prior** $p(\theta)$ copied from the question, constants dropped.
    3. **Multiply.** Collect powers of $\theta$ and exponentials: $\theta^{p}\cdot\theta^{q} = \theta^{p+q}$, $e^{-a\theta}e^{-b\theta} = e^{-(a+b)\theta}$. The result is "posterior $\propto$ …".
    4. **Name it** if it matches Beta or Gamma (table above). If the exam wants the proper pdf, divide by $\int(\ldots)d\theta$ ([M9](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty)).
    5. **MAP:** take $\ln$, differentiate in $\theta$, set to zero, solve (U5 steps 2 to 5). For nested functions (sigmoid) use the chain rule and the hint.
    6. **Compare** with the MLE if asked: MLE = same steps without the prior. Write one sentence on the direction of the pull.

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 2c · 1 p"
    A genomics researcher screens patients sequentially to recruit eligible participants for a trial. Each patient is independently eligible with unknown probability $\theta \in (0, 1)$. The researcher records the number of patients screened $X_i$ until exactly $k = 2$ eligible participants are found. This is modelled as $X_i \sim \text{NegBin}(k, \theta)$, $k = 2$ (known), with PMF

    $$P(X = x \mid \theta) = \binom{x-1}{k-1} \theta^k (1-\theta)^{x-k}, \quad x = k, k+1, k+2, \dots$$

    The observed screening counts over five recruitment rounds are $x = \{3, 5, 4, 6, 4\}$. Assume a Beta prior on $\theta$: $\theta \sim \text{Beta}(\alpha = 2, \beta = 3)$.

    - Write the likelihood function for $\theta$.
    - Derive the posterior distribution for $\theta$.
    - Compute the MAP estimate for $\theta$.

    Hint: $X \sim \text{Beta}(\alpha, \beta)$ has pdf $p(x \mid \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1}$, $0 < x < 1$, where $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$.

<div class="stepper" markdown>

**Step 1 · Likelihood.** With $k = 2$: $P(x_i\mid\theta) = \binom{x_i-1}{1}\theta^2(1-\theta)^{x_i-2} = (x_i - 1)\,\theta^2(1-\theta)^{x_i-2}$. Product over the five rounds:

$$L(\theta) = \prod_{i=1}^{5}(x_i-1)\;\theta^{2\cdot5}\;(1-\theta)^{\sum_i(x_i-2)}.$$

Numbers: $\prod(x_i - 1) = 2\cdot4\cdot3\cdot5\cdot3 = 360$. $\sum x_i = 3+5+4+6+4 = 22$, so $\sum(x_i-2) = 22 - 10 = 12$. Hence $L(\theta) = 360\,\theta^{10}(1-\theta)^{12}$.

**Now do step 2 yourself:** write the prior with $\alpha = 2$, $\beta = 3$, dropping the constant $1/B(\alpha,\beta)$.

---

**Step 2 · Prior.** $p(\theta) \propto \theta^{2-1}(1-\theta)^{3-1} = \theta^{1}(1-\theta)^{2}$.

**Now do step 3 yourself:** multiply likelihood and prior; add the exponents.

---

**Step 3 · Multiply.** $p(\theta\mid\mathbf x) \propto \theta^{10}(1-\theta)^{12}\cdot\theta^{1}(1-\theta)^{2} = \theta^{11}(1-\theta)^{14}$.

**Now do step 4 yourself:** which Beta is that? ($\theta^{a-1}(1-\theta)^{b-1}$.)

---

**Step 4 · Name it.** $a - 1 = 11 \Rightarrow a = 12$; $b - 1 = 14 \Rightarrow b = 15$. Posterior $= \text{Beta}(12, 15)$: $p(\theta\mid\mathbf x) = \frac{1}{B(12,15)}\theta^{11}(1-\theta)^{14}$. (General rule you can quote: Beta$(\alpha + nk,\ \beta + \sum x_i - nk)$.)

**Now do step 5 yourself:** take $\ln$ of $\theta^{11}(1-\theta)^{14}$, differentiate, set to zero, solve.

---

**Step 5 · MAP.** $\ln = 11\ln\theta + 14\ln(1-\theta)$. Derivative: $\frac{11}{\theta} - \frac{14}{1-\theta}$ (the second term is negative because $\frac{d}{d\theta}\ln(1-\theta) = \frac{-1}{1-\theta}$). Zero: $\frac{11}{\theta} = \frac{14}{1-\theta} \Rightarrow 11(1-\theta) = 14\theta \Rightarrow 11 = 25\theta \Rightarrow \hat\theta_{MAP} = \frac{11}{25} = 0.44$. Shortcut check: $\frac{a-1}{a+b-2} = \frac{11}{25}$. Same.

**Step 6 · Compare (not asked, but one line costs nothing).** MLE from $\theta^{10}(1-\theta)^{12}$: $\frac{10}{22} = 0.4545$. Prior peak: $\frac{2-1}{2+3-2} = \frac13 = 0.333$. MAP $= 0.44$ sits between them, pulled toward the prior.

!!! answer "Answer"
    $L(\theta) = 360\,\theta^{10}(1-\theta)^{12}$; posterior $\theta\mid\mathbf x\sim\text{Beta}(12,15)$, i.e. $\propto\theta^{11}(1-\theta)^{14}$; $\hat\theta_{MAP} = 11/25 = 0.44$.

</div>

## Do it cold · 1

!!! exam "June 2026 resit · 2d · 1 p"
    An environmental scientist monitors the number of pollution spikes recorded per day at an air quality monitoring station on the outskirts of a city. The daily spike count is modelled as $X_i \sim \text{Poisson}(\lambda)$, where $\lambda > 0$ is the unknown average number of pollution spikes per day. The observed counts over six days are $x = \{2, 4, 3, 5, 2, 4\}$. Assume a Gamma prior on $\lambda$ with pdf $p(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}$, $\lambda > 0$, $\alpha = 3$, $\beta = 2$.

    - Write the likelihood function for $\lambda$.
    - Derive the posterior distribution for $\lambda$.
    - Find the MAP estimate for $\lambda$.
    - Compare the MAP estimate with the MLE and explain the effect of the prior.

???+ solution "Solution"
    **Step 1.** Poisson PMF: $P(x\mid\lambda) = \frac{\lambda^{x}e^{-\lambda}}{x!}$. Product over $n = 6$ days: $L(\lambda) = \frac{\lambda^{\sum x_i}e^{-6\lambda}}{\prod x_i!}$. $\sum x_i = 2+4+3+5+2+4 = 20$. $\prod x_i! = 2\cdot24\cdot6\cdot120\cdot2\cdot24 = 1\,658\,880$. So $L(\lambda) = \dfrac{\lambda^{20}e^{-6\lambda}}{1\,658\,880} \propto \lambda^{20}e^{-6\lambda}$.

    **Step 2.** Prior $\propto\lambda^{3-1}e^{-2\lambda} = \lambda^{2}e^{-2\lambda}$.

    **Step 3.** Posterior $\propto\lambda^{20}e^{-6\lambda}\lambda^{2}e^{-2\lambda} = \lambda^{22}e^{-8\lambda}$.

    **Step 4.** Gamma with $a - 1 = 22 \Rightarrow a = 23$ and rate $b = 8$: $\lambda\mid\mathbf x\sim\text{Gamma}(23, 8)$. (Rule: Gamma$(\alpha + \sum x_i,\ \beta + n)$.)

    **Step 5.** $\ln = 22\ln\lambda - 8\lambda$; derivative $\frac{22}{\lambda} - 8 = 0 \Rightarrow \hat\lambda_{MAP} = \frac{22}{8} = 2.75$.

    **Step 6.** MLE: $\ln L = 20\ln\lambda - 6\lambda$, derivative $\frac{20}{\lambda} - 6 = 0 \Rightarrow \hat\lambda_{ML} = \frac{20}{6} = 3.333$ (the sample mean). The prior peaks at $\frac{\alpha-1}{\beta} = 1$ (it "expects" about one spike a day), so it pulls the estimate down from $3.33$ to $2.75$. In the formula $\frac{\alpha - 1 + \sum x_i}{\beta + n}$ the data terms $\sum x_i$ and $n$ grow with more days while $\alpha-1 = 2$ and $\beta = 2$ stay fixed, so the MAP converges to the MLE.

    !!! answer "Answer"
        $L(\lambda)\propto\lambda^{20}e^{-6\lambda}$; posterior Gamma$(23, 8)$; $\hat\lambda_{MAP} = 22/8 = 2.75$; $\hat\lambda_{ML} = 20/6 = 3.33$; the prior (mode 1) pulls the estimate down, and the pull fades as $n$ grows.

## Do it cold · 2 (the 1.5-point sigmoid one)

!!! exam "April 2024 · 2d · 1.5 p"
    Consider the posterior distribution $p(\theta | x) = \frac{\lambda(\theta)}{2} e^{-\frac{\lambda(\theta)}{2}x}$, $x > 1$, where $\lambda(\cdot)$ is defined as the logistic sigmoid function $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$. Derive the MAP for the parameter $\theta$. Hint: $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

???+ solution "Solution"
    The posterior is given, so start at step 5. Write $\lambda$ for $\lambda(\theta)$.

    **ln.** $\ln p = \ln\lambda - \ln 2 - \frac{\lambda x}{2}$.

    **Differentiate** (chain rule with the hint): $\frac{d}{d\theta}\ln\lambda = \frac{\lambda'}{\lambda} = \frac{\lambda(1-\lambda)}{\lambda} = 1 - \lambda$. $\frac{d}{d\theta}\left(-\frac{x}{2}\lambda\right) = -\frac x2\lambda(1-\lambda)$. Sum: $(1-\lambda) - \frac x2\lambda(1-\lambda) = (1-\lambda)\left(1 - \frac{x\lambda}{2}\right)$.

    **Zero.** $\lambda = 1$ would need $\theta = \infty$ (discard). So $1 - \frac{x\lambda}{2} = 0 \Rightarrow \lambda = \frac2x$.

    **Undo the sigmoid.** $\frac{1}{1+e^{-\theta}} = \frac2x \Rightarrow 1 + e^{-\theta} = \frac x2 \Rightarrow e^{-\theta} = \frac x2 - 1 \Rightarrow \theta = -\ln\!\left(\frac x2 - 1\right)$.

    **Domain.** Needs $\frac x2 - 1 > 0$, i.e. $x > 2$. For $1 < x \le 2$ the derivative is positive for every $\theta$ (since $\lambda < 1 \le 2/x$), the posterior keeps rising and there is no finite MAP.

    !!! answer "Answer"
        $\hat\theta_{MAP} = -\ln\!\left(\dfrac{x}{2} - 1\right)$ for $x > 2$.

## Do it cold · 3

!!! exam "April 2025 · 2d · 1 p"
    An experiment with binary outcomes Y/N has been independently repeated $N$ times and resulted in a dataset $\mathcal{D} = \{x_1, \dots, x_N\}$ in which $x_n \in \{Y, N\}$. Let $N_0$ and $N_1$ denote the number of obtained Ns and Ys, respectively. Furthermore, let $\theta$ denote the probability of obtaining a Y whereby the posterior distribution takes the form $p(\theta | \mathcal{D}) = \theta^{\beta_1 - 1 + k_1 N_1} (1 - \theta)^{\beta_0 - 1 + k_0 N_0}$. Derive the MAP estimate of $\theta$.

???+ solution "Solution"
    Call the two exponents $A = \beta_1 - 1 + k_1N_1$ and $B = \beta_0 - 1 + k_0N_0$ (known numbers). $\ln p = A\ln\theta + B\ln(1-\theta)$. Derivative: $\frac A\theta - \frac{B}{1-\theta} = 0 \Rightarrow A(1-\theta) = B\theta \Rightarrow A = (A+B)\theta$.

    !!! answer "Answer"
        $\hat\theta_{MAP} = \dfrac{\beta_1 - 1 + k_1N_1}{\beta_1 - 1 + k_1N_1 + \beta_0 - 1 + k_0N_0}$. (It is the Beta shortcut with $a - 1 = A$, $b - 1 = B$.)

## Do it cold · 4

!!! exam "November 2022 · 2g · 0.5 p"
    Posterior $p(\theta|x) = (x+a)^2 \theta e^{-(x+a)\theta}$ for $\theta \geq 0$. Find the maximum a posteriori estimator.

???+ solution "Solution"
    $\ln p = 2\ln(x+a) + \ln\theta - (x+a)\theta$. Derivative in $\theta$ (the first term is constant): $\frac1\theta - (x+a) = 0$.

    !!! answer "Answer"
        $\hat\theta_{MAP} = \dfrac{1}{x+a}$. (Gamma shortcut: $a_{\text{shape}} = 2$, rate $x+a$, mode $\frac{2-1}{x+a}$.) Compare [U7](u07-mmse.md): the MMSE of the same posterior is $\frac{2}{x+a}$, twice as large, because the posterior is skewed to the right.

## Do it cold · 5 (no closed form)

!!! exam "November 2019 · 3c · 1 p"
    $p(x;\theta) = \frac{x}{\theta^2}\exp[-\frac{x^2}{2\theta^2}]$, $x\ge0$, $N$ i.i.d. samples. Now consider the case where $\theta$ is also a random variable with PDF $p(\theta) = \lambda\exp[-\lambda\theta]$. Find the MAP estimator for $\theta$. The answer does **not** have to be in the form $\hat\theta = f(x,\lambda)$.

???+ solution "Solution"
    $\ln[p(\mathbf x;\theta)p(\theta)] = \sum\ln x_n - 2N\ln\theta - \frac{\sum x_n^2}{2\theta^2} + \ln\lambda - \lambda\theta$. Derivative: $-\frac{2N}{\theta} + \frac{\sum x_n^2}{\theta^3} - \lambda = 0$. Multiply by $\theta^3$: $\lambda\theta^3 + 2N\theta^2 - \sum x_n^2 = 0$, a cubic with no nice root.

    !!! answer "Answer"
        $\hat\theta_{MAP}$ solves $-\frac{2N}{\theta} + \frac{1}{\theta^3}\sum_n x_n^2 - \lambda = 0$; it depends on $\lambda$ (for $\lambda\to0$ it becomes the MLE $\sqrt{\sum x^2/(2N)}$).

## Do it cold · 6 (discrete $X$: posterior probabilities and a threshold)

!!! exam "January 2022 resit · 2f + 2h · 0.6 + 0.6 p"
    Let $Y = X + N$ where $X$ and $N$ are independent. $X$ takes the values $+1$ and $-1$ with equal probability, and $N$ is a zero-mean Gaussian random variable with variance $\sigma^2$.

    **2f** Evaluate the a posteriori probabilities $P[X = 1|Y]$ and $P[X = -1|Y]$.

    **2h** Find the maximum a posterior estimator $\hat{X}_{\text{MAP}}$ of $X$ given the observation $Y$. More specifically, find a threshold value $y_{\text{th}}$ such that a decision on $X$ depends on whether or not this threshold value is exceeded. *Hint:* $\hat{X}_{\text{MAP}} = \arg\max_{X \in \{1, -1\}} P[X|Y]$; you can check the ratio of the a posterior probabilities.

???+ solution "Solution"
    **2f, likelihoods.** If $X = 1$ then $Y = 1 + N\sim\mathcal N(1,\sigma^2)$: $p(y\mid X=1) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(y-1)^2/(2\sigma^2)}$. If $X = -1$: $p(y\mid X=-1) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(y+1)^2/(2\sigma^2)}$. Priors: $\frac12$ each.

    **Evidence (a sum, because $X$ is discrete).** $p(y) = \frac12 p(y\mid1) + \frac12 p(y\mid-1) = \frac{1}{2\sqrt{2\pi\sigma^2}}\left(e^{-(y-1)^2/(2\sigma^2)} + e^{-(y+1)^2/(2\sigma^2)}\right)$.

    **Posteriors.** $P[X=1\mid Y] = \frac{\frac12 p(y\mid 1)}{p(y)}$; the $\frac12$ and the $\frac{1}{\sqrt{2\pi\sigma^2}}$ cancel top and bottom:

    $$P[X=1\mid Y] = \frac{e^{-(y-1)^2/(2\sigma^2)}}{e^{-(y-1)^2/(2\sigma^2)} + e^{-(y+1)^2/(2\sigma^2)}},\qquad P[X=-1\mid Y] = \frac{e^{-(y+1)^2/(2\sigma^2)}}{e^{-(y-1)^2/(2\sigma^2)} + e^{-(y+1)^2/(2\sigma^2)}}.$$

    **2h, ratio.** $\frac{P[X=1\mid Y]}{P[X=-1\mid Y]} = \frac{e^{-(y-1)^2/(2\sigma^2)}}{e^{-(y+1)^2/(2\sigma^2)}} = \exp\!\left(\frac{-(y-1)^2 + (y+1)^2}{2\sigma^2}\right)$. Expand: $(y+1)^2 - (y-1)^2 = (y^2+2y+1) - (y^2-2y+1) = 4y$. Ratio $= e^{4y/(2\sigma^2)} = e^{2y/\sigma^2}$. Decide $X = 1$ when the ratio $\ge 1$: $e^{2y/\sigma^2}\ge1 \Leftrightarrow \frac{2y}{\sigma^2}\ge0 \Leftrightarrow y\ge0$.

    !!! answer "Answer"
        Posteriors as above. $\hat X_{MAP} = +1$ if $y > 0$, $-1$ if $y < 0$: $y_{th} = 0$.

## Do it cold · 7 (uniform prior)

!!! exam "January 2019 · 2c · 1 p"
    $p(x\mid\lambda) = \lambda e^{-\lambda x}$, $N$ i.i.d. samples, prior $p(\lambda) = \frac12$ for $0\le\lambda\le2$, $0$ otherwise. Find the MAP estimator for $\lambda$.

???+ solution "Solution"
    Posterior $\propto\lambda^N e^{-\lambda\sum x_i}\cdot\frac12$ on $[0,2]$, zero outside. A flat prior changes nothing inside $[0,2]$, so the peak is the MLE $N/\sum x_i$ ([U5](u05-mle.md), do it cold 5), provided it lies in $[0,2]$; if $N/\sum x_i > 2$ the peak is at the edge, $\hat\lambda = 2$.

    !!! answer "Answer"
        $\hat\lambda_{MAP} = N/\sum_i x_i$ (capped at 2).

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | Posterior $= $ likelihood $\times$ prior, "and the prior is Beta(2,3) so I multiply by $B(2,3)$" | Drop every constant: posterior $\propto\theta^{10}(1-\theta)^{12}\cdot\theta^{1}(1-\theta)^{2}$. Constants never move the peak. |
    | Prior Beta$(\alpha,\beta)$ written as $\theta^{\alpha}(1-\theta)^{\beta}$ | It is $\theta^{\alpha-1}(1-\theta)^{\beta-1}$. The "$-1$" is where most lost points live. |
    | Posterior Beta$(11, 14)$ | Exponents $11$ and $14$ mean $a - 1 = 11$: Beta$(12, 15)$. |
    | $\sum(x_i - k)$ computed as $\sum x_i - k$ | It is $\sum x_i - nk$: subtract $k$ once per sample. |
    | MAP $= \frac{a}{a+b}$ (the mean) | The MAP is the mode $\frac{a-1}{a+b-2}$; $\frac{a}{a+b}$ is the MMSE ([U7](u07-mmse.md)). |
    | Keeping $\lambda(\theta) = 1$ as a MAP | $\lambda=1$ means $\theta=\infty$; say "boundary, discarded". |
    | Stopping at "$\lambda = 2/x$" | The parameter is $\theta$; invert the sigmoid and state the domain $x > 2$. |
    | For discrete $X$, writing $p(y) = \int\ldots$ | With two values of $X$ the evidence is a **sum** of two terms. |
    | "The prior always makes the estimate smaller" | It pulls toward the prior's own peak, which can be above or below the MLE. Say which, with numbers. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution. | True | Jun 2026 2a (c), the correct option. |
| The MAP estimate always equals the posterior mean. | False | Jun 2026 2a (a): only for symmetric posteriors (e.g. Gaussian). Nov 2022 2g vs 2f: $\frac{1}{x+a}$ vs $\frac{2}{x+a}$. |
| As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior. | False | Jun 2026 2a (b): the word *regardless* is the lie; a prior that is zero on part of the range (like the uniform on $[0,2]$) can block convergence. For smooth priors it does converge. |
| Unlike classical estimators, Bayesian estimators do not incorporate prior knowledge about the unknown parameter. | False | Nov 2022 2c (a): it is the other way round. |
| The Bayesian estimate is the estimate that minimises the Bayes risk $\iint C(e)p(\theta\mid\mathbf x)d\theta\,p(\mathbf x)d\mathbf x$. | True | Nov 2022 2c (b). Quadratic cost gives the MMSE, hit-or-miss cost gives the MAP. |
| Minimising the Bayes risk for the uniform (hit-or-miss) error cost results in the minimum mean square error estimator. | False | Nov 2022 2c (c): uniform cost gives the MAP; the *quadratic* cost gives the MMSE. |

</div>

**You can leave this page when you can:**

- [ ] multiply a likelihood by a Beta or Gamma prior and read off the posterior family and parameters.
- [ ] compute a MAP by the $\ln$-derivative-zero route and check it with the mode shortcut.
- [ ] handle a sigmoid inside the posterior with the chain rule and invert it at the end.
- [ ] write posterior probabilities for a discrete unknown (sum in the denominator) and turn their ratio into a threshold.
- [ ] explain in one sentence what the prior does to the estimate and why it fades with more data.

*[prior]: the pdf you assign to the parameter before seeing data.
*[posterior]: the pdf of the parameter after seeing the data: likelihood × prior, normalised.
*[MAP]: maximum a posteriori: the parameter value where the posterior is highest.
*[mode]: the location of the peak of a pdf.
*[conjugate]: a prior whose family is preserved by the likelihood (Beta with binomial-type data, Gamma with Poisson data).
