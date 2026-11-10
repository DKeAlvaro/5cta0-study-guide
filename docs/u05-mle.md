# U5 · Maximum likelihood: likelihood, log-likelihood, derivative, solve

<div class="meta"><span class="hot">Rank 4 · 6.5 points over 7 sittings</span><span>1 p in each of the last three exams</span><span>75 min</span></div>

!!! need "Before this page"
    [M1 exponents, ln and their derivatives](maths.md#m1-exponents-and-logarithms), [M8 argmax](maths.md#m8-argmax-set-the-derivative-to-zero-quadratics). Nothing else.

## The idea in plain words

You measured some numbers. The pdf that produced them has an unknown knob $\theta$. Turn the knob until the numbers you actually got become as probable as possible. The knob position that does that is the **maximum likelihood estimate**. Mechanically it is: multiply the pdf over all data, take $\ln$, differentiate, set to zero, solve.

!!! idea "The thing that confused me"
    The pdf $p(x;\theta)$ is a function of **two** things. As a pdf we vary $x$ with $\theta$ fixed. As a **likelihood** we plug in the data for $x$ and vary $\theta$. Same formula, different variable. When you differentiate, differentiate with respect to $\theta$, and treat every $x_n$ as a known number.

## A tiny example with numbers

Exponential pdf $p(x;\lambda) = \lambda e^{-\lambda x}$. Data: $x_1 = 2$, $x_2 = 4$ ($N=2$).

1. Likelihood: $p(\mathbf x;\lambda) = \lambda e^{-2\lambda}\cdot\lambda e^{-4\lambda} = \lambda^{2}e^{-6\lambda}$ (rule $e^ae^b = e^{a+b}$).
2. Log: $\ln(\lambda^2 e^{-6\lambda}) = 2\ln\lambda - 6\lambda$.
3. Derivative: $\frac{2}{\lambda} - 6$.
4. Zero: $\frac2\lambda = 6 \Rightarrow \hat\lambda = \frac26 = \frac13$.

That is $N/\sum x_n = 2/6$: the MLE of the exponential rate is one over the sample mean.

!!! question "Your turn"
    Same pdf, data $x = \{1, 2, 3, 6\}$. Write the likelihood as $\lambda^{a}e^{-b\lambda}$ (give $a$, $b$), then $\hat\lambda$.

    ???+ solution "Answer"
        $a = N = 4$, $b = \sum x = 12$: $\lambda^4 e^{-12\lambda}$. $\ln = 4\ln\lambda - 12\lambda$; derivative $4/\lambda - 12 = 0 \Rightarrow \hat\lambda = 4/12 = 1/3$.

## The formulas, every symbol named

<div class="key" markdown>

$$\hat\theta_{ML} = \arg\max_\theta\, p(\mathbf x;\theta), \qquad p(\mathbf x;\theta) = \prod_{n=1}^{N}p(x_n;\theta), \qquad \frac{\partial}{\partial\theta}\ln p(\mathbf x;\theta)\Big|_{\hat\theta} = 0$$

</div>

| Symbol | Meaning |
|---|---|
| $\theta$ | the unknown parameter (could be called $\lambda$, $\sigma^2$, $A$, an angle…) |
| $x_n$ | the $n$-th observation, a known number |
| $N$ | number of observations; if the question has one $x$, $N = 1$ |
| $p(\mathbf x;\theta)$ (or $p(\mathbf x\mid\theta)$) | likelihood: product of the single-sample pdfs because the samples are independent |
| $\ln p(\mathbf x;\theta)$ | log-likelihood; same maximiser, far easier to differentiate |
| $\arg\max$ | "the $\theta$ at which the maximum happens" |

**Why ln.** $\ln$ is increasing, so the $\theta$ that maximises $p$ also maximises $\ln p$ ([M8](maths.md#m8-argmax-set-the-derivative-to-zero-quadratics)). And $\ln$ of a product of exponentials is a sum of simple terms ([M1](maths.md#m1-exponents-and-logarithms)).

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "write the likelihood and log-likelihood functions for $\theta$ given $x_1,\ldots,x_n$" | step 1 and step 2 of the recipe, written out explicitly; the product with $\prod$, then the sum with $\sum$ |
| "derive the maximum likelihood estimator for $\theta$" | all six steps, ending with $\hat\theta = $ formula in the $x_n$ |
| "find an estimator for the parameter $\theta$" (no method named, a pdf given) | MLE is the intended method |
| "known shape parameter $k$" / "$k_1, k_2$ known constants" | they are numbers, not variables; they survive in the answer |
| "explain what the MLE tells us" | one sentence: it is the value of $\theta$ that makes the observed data most probable; here it equals (sample mean)/$k$, etc. |
| "the derivative of the logistic sigmoid is $\lambda(1-\lambda)$" | you will need the chain rule: $\frac{d}{d\theta}\ln\lambda(\theta) = \lambda'/\lambda = 1-\lambda$ |
| "the answer does not have to be in the form $\hat\theta = f(x)$" | you may stop at the equation "derivative $= 0$" if it cannot be solved in closed form |

## Recipe

!!! recipe key "U5 · MLE in six steps"
    1. **Likelihood.** Write the pdf once with $x_n$, then the product over $n = 1..N$. Collect: constants multiply to $c^N$, powers of $x_n$ stay as $\prod x_n^{\,a}$, exponentials merge into $\exp(\sum\cdot)$.
    2. **Log-likelihood.** $\ln$ of the product = sum of $\ln$s. Expand each with $\ln(ab) = \ln a + \ln b$, $\ln a^n = n\ln a$, $\ln e^{u} = u$.
    3. **Drop** every term that does not contain $\theta$ (its derivative is zero anyway). Say so.
    4. **Differentiate** with respect to $\theta$. Table in [M1](maths.md#m1-exponents-and-logarithms): $\frac{d}{d\theta}\ln\theta = 1/\theta$, $\frac{d}{d\theta}(c/\theta) = -c/\theta^2$, $\frac{d}{d\theta}(c\theta) = c$, chain rule for anything nested.
    5. **Set to zero and solve** for $\theta$. Multiply through by the denominators first.
    6. **Write the estimator** with a hat and, if asked, one sentence of meaning. Optionally check the second derivative is negative (a maximum, not a minimum).

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 2b · 1 p"
    A hospital administrator records the recovery time $X$ (in days) for patients following a routine surgical procedure. Recovery times are modelled as $X \sim \text{Gamma}(k, \theta)$, where $k > 0$ is a *known* shape parameter and $\theta > 0$ is the unknown scale parameter (average recovery contribution per stage). The Gamma pdf is

    $$p(x \mid \theta) = x^{k-1} e^{-x/\theta} / (\theta^k \Gamma(k)), \quad x > 0.$$

    - Write the likelihood and log-likelihood functions for $\theta$ given observations $x_1, \dots, x_n$.
    - Derive the maximum likelihood estimator (MLE) for $\theta$.
    - Explain what the MLE tells us about patient recovery at the hospital.

<div class="stepper" markdown>

**Step 1 · Likelihood.** For one observation: $p(x_i\mid\theta) = \dfrac{x_i^{k-1}e^{-x_i/\theta}}{\theta^k\Gamma(k)}$. Product over $i = 1..n$:

$$L(\theta) = \prod_{i=1}^{n}\frac{x_i^{k-1}e^{-x_i/\theta}}{\theta^k\Gamma(k)} = \frac{\left(\prod_i x_i\right)^{k-1}\exp\!\left(-\frac1\theta\sum_i x_i\right)}{\theta^{nk}\,\Gamma(k)^n}.$$

(Constants: $\theta^k$ appears $n$ times → $\theta^{nk}$; $\Gamma(k)$ appears $n$ times → $\Gamma(k)^n$; exponentials add their exponents.)

**Now do step 2 yourself:** take $\ln$ and expand into four terms.

---

**Step 2 · Log-likelihood.** $\ln L = (k-1)\sum_i\ln x_i - \frac{1}{\theta}\sum_i x_i - nk\ln\theta - n\ln\Gamma(k)$.

Where each term comes from: $\ln(\prod x_i)^{k-1} = (k-1)\sum\ln x_i$; $\ln\exp(u) = u$; $\ln\theta^{nk} = nk\ln\theta$ with a minus because it is in the denominator; same for $\Gamma(k)^n$.

**Now do step 3 yourself:** which terms contain $\theta$?

---

**Step 3 · Drop.** Only $-\frac1\theta\sum x_i$ and $-nk\ln\theta$ contain $\theta$. Keep $\ell(\theta) = -\frac{S}{\theta} - nk\ln\theta$ with $S = \sum_i x_i$.

**Now do step 4 yourself:** differentiate $\ell$ with respect to $\theta$.

---

**Step 4 · Differentiate.** $\frac{d}{d\theta}\left(-\frac S\theta\right) = -S\cdot\left(-\frac{1}{\theta^2}\right) = \frac{S}{\theta^2}$. $\frac{d}{d\theta}(-nk\ln\theta) = -\frac{nk}{\theta}$. So $\ell'(\theta) = \dfrac{S}{\theta^2} - \dfrac{nk}{\theta}$.

**Now do step 5 yourself:** set to zero, multiply by $\theta^2$, solve.

---

**Step 5 · Solve.** $\frac{S}{\theta^2} = \frac{nk}{\theta}$. Multiply both sides by $\theta^2$: $S = nk\theta$. So $\hat\theta = \dfrac{S}{nk} = \dfrac{1}{k}\cdot\dfrac{1}{n}\sum_i x_i = \dfrac{\bar x}{k}$.

**Step 6 · Meaning.** The MLE is the sample mean of the recovery times divided by the known shape $k$. Since a Gamma$(k,\theta)$ variable has mean $k\theta$, this says: choose $\theta$ so that the model's mean recovery time equals the hospital's observed average recovery time. (Second derivative at $\hat\theta$: $-2S/\theta^3 + nk/\theta^2 = -nk/\hat\theta^2 < 0$: a maximum.)

!!! answer "Answer"
    $L(\theta) = \dfrac{(\prod x_i)^{k-1}e^{-\sum x_i/\theta}}{\theta^{nk}\Gamma(k)^n}$; $\ln L = (k-1)\sum\ln x_i - \frac{\sum x_i}{\theta} - nk\ln\theta - n\ln\Gamma(k)$; $\hat\theta_{ML} = \dfrac{\sum_i x_i}{nk} = \bar x/k$.

</div>

## Do it cold · 1 (the sigmoid one)

!!! exam "April 2025 · 2c · 1 p"
    Consider the likelihood $p(x|\theta) = 3\lambda(\theta)e^{-4\frac{\lambda(\theta)x}{7}}$, $x > 1$, where $\lambda(\cdot)$ is defined as the logistic sigmoid function $\lambda(\theta) = \frac{1}{1+e^{-\theta}}$. Derive the MLE for the parameter $\theta$. Hint: The derivative of the logistic sigmoid is $\frac{\partial \lambda(\theta)}{\partial \theta} = \lambda(\theta)(1 - \lambda(\theta))$.

???+ solution "Solution"
    **Step 1.** One observation, so the likelihood is the pdf itself: $3\lambda e^{-4\lambda x/7}$ (write $\lambda$ for $\lambda(\theta)$).

    **Step 2.** $\ln p = \ln 3 + \ln\lambda - \frac{4}{7}\lambda x$.

    **Step 3.** Drop $\ln 3$.

    **Step 4.** Chain rule, with $\lambda' = \lambda(1-\lambda)$: $\frac{d}{d\theta}\ln\lambda = \frac{\lambda'}{\lambda} = 1-\lambda$; $\frac{d}{d\theta}\left(-\frac47\lambda x\right) = -\frac47 x\lambda' = -\frac47 x\lambda(1-\lambda)$. Sum: $(1-\lambda) - \frac47x\lambda(1-\lambda) = (1-\lambda)\left(1 - \frac47\lambda x\right)$. (Expanded, as the official key writes it: $1 - \lambda - \frac47\lambda x + \frac47\lambda^2 x$.)

    **Step 5.** Zero when $\lambda = 1$ or $1 - \frac47\lambda x = 0$. $\lambda = 1$ means $e^{-\theta} = 0$, i.e. $\theta\to\infty$: not a finite solution, discard. So $\lambda = \frac{7}{4x}$. Undo the sigmoid: $\frac{1}{1+e^{-\theta}} = \frac{7}{4x} \Rightarrow 1 + e^{-\theta} = \frac{4x}{7} \Rightarrow e^{-\theta} = \frac{4x}{7} - 1 \Rightarrow -\theta = \ln\!\left(\frac{4x}{7}-1\right)$.

    **Step 6.** $\hat\theta = -\ln\!\left(\frac{4x}{7}-1\right)$, which needs $\frac{4x}{7} - 1 > 0$, i.e. $x > 7/4$ (the official clarification says exactly this).

    !!! answer "Answer"
        $\hat\theta_{ML} = -\ln\!\left(\frac{4}{7}x - 1\right)$, valid for $x > 7/4$.

## Do it cold · 2

!!! exam "April 2024 · 2c · 1 p"
    For the data vector $\mathbf{x} = \{x_1, \dots, x_N\}$ consisting of independent samples with probability density function $p(x_n | \theta) = \frac{x_n}{2\theta} e^{-\frac{x_n^2}{2\theta}}$, derive the MLE for the parameter $\theta$.

???+ solution "Solution"
    **Step 1.** $L = \prod_n\frac{x_n}{2\theta}e^{-x_n^2/(2\theta)} = \dfrac{\prod x_n}{(2\theta)^N}\exp\!\left(-\frac{\sum x_n^2}{2\theta}\right)$.

    **Step 2.** $\ln L = \sum\ln x_n - N\ln(2\theta) - \frac{\sum x_n^2}{2\theta}$. Note $\ln(2\theta) = \ln2 + \ln\theta$.

    **Step 3.** Keep $-N\ln\theta - \frac{T}{2\theta}$ with $T = \sum x_n^2$.

    **Step 4.** $-\frac N\theta + \frac{T}{2\theta^2}$ (derivative of $-\frac{T}{2}\theta^{-1}$ is $+\frac T2\theta^{-2}$).

    **Step 5.** $\frac{T}{2\theta^2} = \frac N\theta \Rightarrow T = 2N\theta \Rightarrow \hat\theta = \frac{T}{2N}$.

    !!! answer "Answer"
        $\hat\theta_{ML} = \dfrac{1}{2N}\sum_{n=1}^{N}x_n^2$. (October 2021 2b has $\frac{x}{\theta}$ instead of $\frac{x}{2\theta}$ in front; the front constant does not contain $\theta$ in the exponent and the answer is the same.)

## Do it cold · 3 (the angle)

!!! exam "November 2022 · 2d · 0.5 p"
    Consider the observation $\mathbf{x} = A \begin{bmatrix} \cos(\theta) \\ \sin(\theta) \end{bmatrix} + \mathbf{w}$, where $\mathbf{w}$ is white Gaussian noise. The probability density function of the observation is $p(\mathbf{x}; \theta) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{1}{2\sigma^2} \left((x_1 - A \cos(\theta))^2 + (x_2 - A \sin(\theta))^2\right)\right)$. Find the maximum likelihood estimator of the parameter $\theta$.

???+ solution "Solution"
    **Step 2.** $\ln p = -\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\left[(x_1 - A\cos\theta)^2 + (x_2 - A\sin\theta)^2\right]$.

    **Expand the squares** $(a-b)^2 = a^2 - 2ab + b^2$: $x_1^2 - 2Ax_1\cos\theta + A^2\cos^2\theta + x_2^2 - 2Ax_2\sin\theta + A^2\sin^2\theta$. Use $\cos^2+\sin^2 = 1$: $= x_1^2 + x_2^2 + A^2 - 2A(x_1\cos\theta + x_2\sin\theta)$.

    **Step 3.** Only $-2A(x_1\cos\theta + x_2\sin\theta)$ depends on $\theta$; with the $-\frac{1}{2\sigma^2}$ in front it is $+\frac{A}{\sigma^2}(x_1\cos\theta + x_2\sin\theta)$.

    **Step 4.** $\frac{A}{\sigma^2}(-x_1\sin\theta + x_2\cos\theta)$.

    **Step 5.** $x_2\cos\theta = x_1\sin\theta \Rightarrow \frac{\sin\theta}{\cos\theta} = \frac{x_2}{x_1} \Rightarrow \tan\theta = \frac{x_2}{x_1}$.

    !!! answer "Answer"
        $\hat\theta_{ML} = \tan^{-1}(x_2/x_1)$, taken in the quadrant of the point $(x_1, x_2)$: the estimate is the angle of the observed vector.

## Do it cold · 4

!!! exam "November 2019 · 3a · 1 p"
    The data $x[0], \ldots, x[N-1]$ are i.i.d. according to $p(x; \theta) = \frac{x}{\theta^2} \exp \left[ -\frac{x^2}{2\theta^2} \right]$, $x \geq 0$. Find the maximum likelihood estimator for $\theta$.

???+ solution "Solution"
    $\ln L = \sum\ln x[n] - 2N\ln\theta - \frac{\sum x[n]^2}{2\theta^2}$ (because $\ln\theta^2 = 2\ln\theta$ and there are $N$ of them). Derivative: $-\frac{2N}{\theta} + \frac{\sum x^2}{\theta^3}$ (derivative of $-\frac T2\theta^{-2}$ is $+T\theta^{-3}$). Zero: $\frac{T}{\theta^3} = \frac{2N}{\theta} \Rightarrow T = 2N\theta^2 \Rightarrow \theta^2 = \frac{T}{2N}$.

    !!! answer "Answer"
        $\hat\theta_{ML} = \sqrt{\dfrac{1}{2N}\sum_{n=0}^{N-1}x^2[n]}$.

## Do it cold · 5

!!! exam "January 2019 · 2a · 1 p"
    For the random variable $x$ with distribution $p(x; \lambda) = \lambda e^{-\lambda x}$, find the maximum likelihood estimator for $\lambda$, given $N$ i.i.d. observations $x_i$.

???+ solution "Solution"
    $L = \lambda^N e^{-\lambda\sum x_i}$; $\ln L = N\ln\lambda - \lambda\sum x_i$; derivative $\frac N\lambda - \sum x_i = 0$.

    !!! answer "Answer"
        $\hat\lambda_{ML} = \dfrac{N}{\sum_i x_i}$.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $\ln\prod_i f_i = \prod_i\ln f_i$ | $\ln$ of a product is the **sum** of the logs. |
    | $\ln(\theta^k\Gamma(k))$ in the numerator | It was in the denominator: $-k\ln\theta - \ln\Gamma(k)$, and $n$ times. |
    | $\frac{d}{d\theta}\frac{S}{\theta} = \frac{S}{\theta^2}$ | $\frac{d}{d\theta}\frac S\theta = -\frac{S}{\theta^2}$ (the minus matters: with the leading minus of the term it becomes $+$). |
    | $\frac{d}{d\theta}\ln\lambda(\theta) = \frac{1}{\lambda}$ | Chain rule: $\frac{\lambda'(\theta)}{\lambda(\theta)}$; with the hint, $= 1-\lambda$. |
    | Keeping $\lambda = 1$ as a solution | It corresponds to $\theta = \infty$; discard and say why. |
    | Stopping at $\lambda = 7/(4x)$ | The question asks for $\theta$: undo the sigmoid. |
    | $\tan^{-1}(x_2/x_1)$ without the quadrant remark | Add "in the quadrant of $(x_1,x_2)$"; the key explicitly mentions it. |
    | Writing $\hat\theta = $ (a number) when $N$ data are symbolic | The estimator is a formula in the $x_n$; plug numbers only if the exam gives them. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| The MLE is the argument maximising the likelihood. | True | Apr 2025 2a option a. |
| The maximum likelihood estimate is the value of $x$ that maximises the likelihood function. | False | Jan 2022 2b (a): it is the value of $\theta$, not of $x$. |
| The maximum likelihood estimator always achieves the Cramér–Rao lower bound. | False | Nov 2022 2b (a): only asymptotically (large $N$), or for special models. |
| The maximum likelihood estimator is asymptotically unbiased. | True | Nov 2022 2b (c). |
| For a one-to-one transformation $\alpha = \psi(\theta)$, $\hat\theta_{ML} = \psi^{-1}(\hat\alpha_{ML})$. | True | Jan 2022 2b (c): the invariance property. Used in Apr 2025 2c when we undo the sigmoid. |
| For large sample sizes the ML estimate is uniformly distributed. | False | Jan 2022 2b (b): it is Gaussian, $\hat\theta\sim\mathcal N(\theta, \mathcal I^{-1}(\theta))$. |

</div>

**You can leave this page when you can:**

- [ ] write the likelihood of $N$ i.i.d. samples as one expression with $\prod$, $c^N$ and $\exp(\sum)$.
- [ ] expand its $\ln$ term by term and drop the $\theta$-free terms.
- [ ] differentiate $c\ln\theta$, $c/\theta$, $c/\theta^2$ and $\ln\lambda(\theta)$ (chain rule) without looking.
- [ ] solve "derivative $= 0$" by clearing denominators.
- [ ] say in one sentence what the estimate means.

*[likelihood]: the pdf of the data, read as a function of the unknown parameter with the data plugged in.
*[estimator]: a formula that turns data into a guess of the parameter; the estimate is the number you get for specific data.
*[logistic sigmoid]: λ(θ) = 1/(1+e^(−θ)), a smooth S-curve from 0 to 1.
