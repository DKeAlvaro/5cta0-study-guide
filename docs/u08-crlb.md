# U8 · Fisher information and the Cramér–Rao lower bound

<div class="meta"><span class="hot">Rank 12 · 3.0 points over 4 sittings</span><span>last derivation Nov 2022 (0.5 p); MC facts every year</span><span>50 min</span></div>

!!! need "Before this page"
    [U5](u05-mle.md) (log-likelihood and its derivative), [M1 second derivatives](maths.md#m1-exponents-and-logarithms), [M6 expectation](maths.md#m6-expectation-and-variance-rules) (you will need $E[x^2]$ or $E[x]$ of the pdf).

## The idea in plain words

No unbiased estimator can be arbitrarily precise. The data carry a fixed amount of **information** about $\theta$; the **Cramér–Rao lower bound (CRLB)** is the smallest variance any unbiased estimator can have, and it equals one over that information. Mechanically: take the log-likelihood, differentiate **twice**, take the expectation, flip the sign, invert.

!!! idea "The thing that confused me"
    Why a *second* derivative? The first derivative of $\ln p$ at the true $\theta$ averages to zero (that is the regularity condition). The second derivative measures how sharply peaked the likelihood is: a sharp peak (very negative curvature) means the data pin $\theta$ down well, so the information is large and the bound is small.

## A tiny example with numbers

Exponential pdf, $N$ samples: $\ln p = N\ln\lambda - \lambda\sum x_n$ ([U5](u05-mle.md)).
First derivative: $\frac N\lambda - \sum x_n$. Second: $-\frac{N}{\lambda^2}$ (no $x$ left, so the expectation does nothing).
$\mathcal I(\lambda) = -E\left[-\frac{N}{\lambda^2}\right] = \frac{N}{\lambda^2}$. CRLB $= \frac{\lambda^2}{N}$.
With $\lambda = 2$ and $N = 50$: any unbiased estimator has variance at least $4/50 = 0.08$.

!!! question "Your turn"
    $\ln p = 20\ln\theta - 8\theta + \text{const}$ (the Gamma posterior shape from U6, treated as a likelihood). Second derivative? Information? Bound?

    ???+ solution "Answer"
        First: $\frac{20}{\theta} - 8$. Second: $-\frac{20}{\theta^2}$. $\mathcal I = \frac{20}{\theta^2}$, CRLB $= \frac{\theta^2}{20}$.

## The formulas, every symbol named

<div class="key" markdown>

$$\mathcal I(\theta) = -E\!\left[\frac{\partial^2\ln p(\mathbf x;\theta)}{\partial\theta^2}\right] = E\!\left[\left(\frac{\partial\ln p(\mathbf x;\theta)}{\partial\theta}\right)^{2}\right],\qquad \operatorname{Var}(\hat\theta)\ \ge\ \frac{1}{\mathcal I(\theta)}$$

</div>

| Symbol | Meaning |
|---|---|
| $\mathcal I(\theta)$ | Fisher information of the whole data set. For $N$ i.i.d. samples $\mathcal I(\theta) = N\,i(\theta)$, with $i$ the information of one sample |
| $E[\cdot]$ | expectation over the data $\mathbf x$ (not over $\theta$): replace $x^2$ by $E[x^2]$, $x$ by $E[x]$, using the pdf |
| CRLB | $1/\mathcal I(\theta)$: lower bound on the variance of any **unbiased** estimator |
| efficient | an unbiased estimator whose variance **equals** the CRLB |
| regularity condition | $E\left[\frac{\partial\ln p}{\partial\theta}\right] = 0$ for all $\theta$. It fails when the **range of $x$ depends on $\theta$** (e.g. $0\le x\le\theta$); then the CRLB cannot be derived |

**Why "$-E$"**: the second derivative of a peaked function is negative at the peak; the minus makes the information positive.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "derive the Fisher information $\mathcal I(\theta)$" | second derivative of $\ln p$, expectation, minus sign. Use the hint for $E[x_1]$, $E[x_2]$ if given |
| "find the Cramér–Rao lower bound for the MLE" | same, then invert; for $N$ samples multiply the single-sample information by $N$ first |
| "check whether it is possible to derive the CRLB" | look at the pdf's domain: if it contains $\theta$ (like $0\le x\le\theta$), say the regularity condition is violated and stop |
| "the expected values of $x_1$ and $x_2$ are …" (hint) | after the second derivative you will have $x_1$, $x_2$ linearly; replace them by the hint values |
| "given the MVUE … with variance $A^2/N$, find the pdf" (Oct 2021) | run the recipe backwards: $\frac{\partial\ln p}{\partial\theta} = \mathcal I(\theta)(\hat\theta - \theta)$, integrate in $\theta$ |

## Recipe

!!! recipe key "U8 · Information in four moves"
    1. **Log-likelihood** of the full data ([U5](u05-mle.md) steps 1 to 3). Keep only $\theta$ terms.
    2. **Differentiate twice** with respect to $\theta$.
    3. **Expectation**: every $x$-dependent piece becomes its mean under $p(x;\theta)$ ($E[x]$, $E[x^2]$…). Compute that mean by integration if not given ($E[x^2] = \int x^2p(x;\theta)dx$), or use a known moment.
    4. **Minus sign and invert**: $\mathcal I = -E[\cdot]$, CRLB $= 1/\mathcal I$. For $N$ samples the answer carries an $N$ in $\mathcal I$ and a $1/N$ in the bound.
    0. **Before step 1**: if the domain of $x$ depends on $\theta$, write "regularity condition violated, CRLB does not exist" and collect the points.

## Worked exam question, one step at a time

!!! exam "November 2022 · 2e · 0.5 p"
    (Same model as 2d.) $p(\mathbf{x}; \theta) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{1}{2\sigma^2} \left((x_1 - A \cos(\theta))^2 + (x_2 - A \sin(\theta))^2\right)\right)$. Derive the Fisher information $\mathcal{I}(\theta)$. **Hint:** The expected values of $x_1$ and $x_2$ are $A \cos(\theta)$ and $A \sin(\theta)$, respectively.

<div class="stepper" markdown>

**Step 1 · Log-likelihood, $\theta$ part only.** From U5 (do it cold 3): $\ln p = \text{const} + \frac{A}{\sigma^2}\left(x_1\cos\theta + x_2\sin\theta\right)$.

**Now do step 2 yourself:** differentiate twice.

---

**Step 2 · Two derivatives.** First: $\frac{A}{\sigma^2}(-x_1\sin\theta + x_2\cos\theta)$. Second: $\frac{A}{\sigma^2}(-x_1\cos\theta - x_2\sin\theta)$.

**Now do step 3 yourself:** take the expectation using the hint.

---

**Step 3 · Expectation.** $E[\cdot] = \frac{A}{\sigma^2}\left(-E[x_1]\cos\theta - E[x_2]\sin\theta\right) = \frac{A}{\sigma^2}\left(-A\cos^2\theta - A\sin^2\theta\right) = -\frac{A^2}{\sigma^2}(\cos^2\theta + \sin^2\theta) = -\frac{A^2}{\sigma^2}$.

**Now do step 4 yourself:** sign, and (bonus) the CRLB.

---

**Step 4 · Minus and invert.** $\mathcal I(\theta) = -\left(-\frac{A^2}{\sigma^2}\right) = \frac{A^2}{\sigma^2}$. CRLB $= \frac{\sigma^2}{A^2}$: a stronger signal ($A$) or quieter noise ($\sigma$) pins the angle down better.

!!! answer "Answer"
    $\mathcal I(\theta) = A^2/\sigma^2$ (independent of $\theta$).

</div>

## Do it cold · 1

!!! exam "November 2019 · 3b · 1 p"
    $p(x;\theta) = \frac{x}{\theta^2}\exp[-\frac{x^2}{2\theta^2}]$, $x\ge0$, $N$ i.i.d. samples. Find the Cramér–Rao lower bound for the MLE.

???+ solution "Solution"
    **Step 1.** One sample: $\ln p = \ln x - 2\ln\theta - \frac{x^2}{2\theta^2}$.

    **Step 2.** First derivative: $-\frac2\theta + \frac{x^2}{\theta^3}$. Second: $\frac{2}{\theta^2} - \frac{3x^2}{\theta^4}$ (derivative of $x^2\theta^{-3}$ is $-3x^2\theta^{-4}$).

    **Step 3.** Need $E[x^2]$: $\int_0^\infty x^2\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}dx$. Substitute $u = \frac{x^2}{2\theta^2}$, so $x^2 = 2\theta^2u$ and $x\,dx = \theta^2du$: the integral becomes $\int_0^\infty 2\theta^2u\cdot e^{-u}du = 2\theta^2\int_0^\infty ue^{-u}du = 2\theta^2\cdot1 = 2\theta^2$ ([M9](maths.md#m9-integrals-the-exam-hands-out-and-evaluating-at-0-and-infty): $\int_0^\infty u e^{-u}du = 1! = 1$). So $E[\text{second}] = \frac2{\theta^2} - \frac{3\cdot2\theta^2}{\theta^4} = \frac{2}{\theta^2} - \frac{6}{\theta^2} = -\frac{4}{\theta^2}$.

    **Step 4.** $i(\theta) = \frac{4}{\theta^2}$ per sample; $\mathcal I = \frac{4N}{\theta^2}$; CRLB $= \frac{\theta^2}{4N}$.

    !!! answer "Answer"
        $\operatorname{Var}(\hat\theta)\ge\dfrac{\theta^2}{4N}$.

## Do it cold · 2 (regularity)

!!! exam "January 2022 resit · 2e · 0.5 p"
    Let $p(x;\theta) = \frac{2}{\theta^2}x$ for $0\le x\le\theta$, $0$ else (corrected pdf). Check whether or not it is possible to derive the Cramér–Rao lower bound. In case it is possible, derive it. If it is not possible, justify why.

???+ solution "Solution"
    **Step 0.** The pdf is nonzero only for $0\le x\le\theta$: the **domain of $x$ depends on $\theta$**. Then $\int p\,dx = 1$ cannot be differentiated under the integral sign (the limit moves), so $E[\partial\ln p/\partial\theta]\ne0$: the regularity condition fails and the CRLB is not defined.

    !!! answer "Answer"
        Not possible: the support of $p(x;\theta)$ depends on $\theta$, which violates the regularity condition.

## Do it cold · 3 (the backwards one, Oct 2021 · 2a · 1 p)

!!! exam "October 2021 · 2a"
    Given the minimum variance unbiased estimator (MVUE) $\hat{\theta} = \sum_{n=0}^{N-1} x[n]/N$ with variance $\sigma_{\hat{\theta}}^2 = A^2/N$, find the pdf $p(\mathbf{x}; \theta)$ for the data vector. Use the MVUE condition and show the derivation. Assume i.i.d. noise samples. **Hint:** $\int (x+a)dx = x^2/2 + ax + b$ and $b$ can be chosen as $b = a^2/2$ to obtain $0.5(x+a)^2$.

???+ solution "Solution"
    The MVUE (efficiency) condition is $\frac{\partial\ln p}{\partial\theta} = \mathcal I(\theta)(\hat\theta - \theta)$. With $\operatorname{Var}(\hat\theta) = A^2/N = 1/\mathcal I$, $\mathcal I = N/A^2$. So $\frac{\partial\ln p}{\partial\theta} = \frac{N}{A^2}\left(\frac1N\sum x[n] - \theta\right) = \frac{1}{A^2}\sum_n(x[n] - \theta)$. Integrate in $\theta$ (hint, with the constant chosen as a square): $\ln p = -\frac{1}{2A^2}\sum_n(x[n]-\theta)^2 + c$, hence $p(\mathbf x;\theta) = \prod_n\frac{1}{\sqrt{2\pi A^2}}\exp\!\left(-\frac{(x[n]-\theta)^2}{2A^2}\right)$: i.i.d. Gaussian noise of variance $A^2$ around $\theta$.

    !!! answer "Answer"
        $p(\mathbf x;\theta) = (2\pi A^2)^{-N/2}\exp\!\left(-\frac{1}{2A^2}\sum_n(x[n]-\theta)^2\right)$.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $\mathcal I(\theta) = E[\partial^2\ln p/\partial\theta^2]$ | With a **minus** sign. |
    | Leaving $x_1$, $x_2$ in the final $\mathcal I$ | Information is an expectation: no data left. Replace by $E[x_1] = A\cos\theta$ etc. |
    | CRLB $= \theta^2/4$ for $N$ samples | Information adds: $\mathcal I = N\,i(\theta)$, bound $= \theta^2/(4N)$. |
    | Deriving a CRLB for $0\le x\le\theta$ | The support depends on $\theta$: say "regularity violated", no bound. |
    | "An estimator with variance below the CRLB is efficient" | No estimator goes below; efficient = **equals** the bound. |
    | "The bound is $\mathcal I(\theta)$" | The bound is $1/\mathcal I(\theta)$; the variance is bounded *below* by the inverse. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| The Fisher information for $N$ i.i.d. observations is $N\,i(\theta)$, where $i(\theta)$ is the information for a single observation. | True | Nov 2022 2a (a), Apr 2024 2a (c). |
| The variance of any unbiased estimator is lower bounded by the Fisher information, i.e. $\operatorname{Var}(\hat\theta)\ge\mathcal I(\theta)$. | False | Nov 2022 2a (b), Apr 2024 2a (a): it is bounded by $1/\mathcal I(\theta)$. |
| The Fisher information is strictly negative. | False | Nov 2022 2a (c), Apr 2024 2a (b): it is an expected squared derivative, never negative. |
| The Cramér–Rao lower bound can always be derived. | False | Jan 2022 2a (a): only when the regularity conditions hold. |
| For i.i.d. observations the CRLB decreases linearly with the number of observations. | True | Jan 2022 2a (b): $1/(N i(\theta))$. (Strictly "as $1/N$"; this is the option the key marks correct.) |
| An estimator whose variance is lower than the CRLB is called efficient. | False | Jan 2022 2a (c): efficient means *attains* the bound. |

</div>

**You can leave this page when you can:**

- [ ] differentiate a log-likelihood twice and take the expectation of what is left.
- [ ] compute $E[x^2]$ for a Rayleigh-type pdf by the substitution $u = x^2/(2\theta^2)$.
- [ ] write $\mathcal I$ for $N$ samples and the bound with $1/N$.
- [ ] spot a $\theta$-dependent domain and name the regularity condition.
- [ ] state what "efficient" means.

*[Fisher information]: the expected curvature of the log-likelihood at the true parameter; large = data very informative.
*[unbiased]: an estimator whose average over many data sets equals the true parameter.
*[efficient]: unbiased and with variance equal to the CRLB.
*[regularity condition]: E[∂ ln p/∂θ] = 0; it fails when the range of x depends on θ.
