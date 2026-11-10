# M · Maths the course assumes

<div class="meta"><span class="hot">Read before any unit</span><span>45 min</span><span>Every unit links here</span></div>

!!! need "Before this page"
    You can differentiate, read the limits of an integral, handle fractions and multiply matrices. Nothing else is assumed. Every unit links back to the section here that it needs.

## M1 · Exponents and logarithms

**Plain words.** $e^{a}$ is the number $2.718\ldots$ raised to the power $a$. $\ln$ is the question "$e$ to what power gives this?". They undo each other: $\ln(e^{a}) = a$ and $e^{\ln a} = a$.

| Rule | Example with numbers |
|---|---|
| $e^{a}\,e^{b} = e^{a+b}$ | $e^{2}e^{3} = e^{5}$ |
| $e^{a}/e^{b} = e^{a-b}$ | $e^{-2x}/e^{-x} = e^{-2x+x} = e^{-x}$ |
| $(e^{a})^{n} = e^{an}$ | $(e^{-2})^{n} = e^{-2n}$ |
| $\ln(ab) = \ln a + \ln b$ | $\ln(3\cdot 5) = \ln 3 + \ln 5$ |
| $\ln(a/b) = \ln a - \ln b$ | $\ln(1/4) = -\ln 4$ |
| $\ln(a^{n}) = n\ln a$ | $\ln(\theta^{k}) = k\ln\theta$ |
| $\ln(e^{a}) = a$ | $\ln(e^{-x/\theta}) = -x/\theta$ |
| $\ln 1 = 0$, $\ln e = 1$ | |
| $\ln\prod_i f_i = \sum_i \ln f_i$ | product of 5 terms becomes a sum of 5 logs |

**Why the course cares.** A likelihood is a product of $N$ copies of a pdf. Taking $\ln$ turns the product into a sum, and $\ln$ of $e^{\text{stuff}}$ is just "stuff". That is the whole trick behind every MLE and MAP question.

**Worked line.** $\ln\!\left(\theta^{2}(1-\theta)^{3}\right)$: use $\ln(ab)=\ln a+\ln b$, then $\ln(a^{n}) = n\ln a$: $= 2\ln\theta + 3\ln(1-\theta)$.

**Solving $e^{\text{something}} = c$.** Take $\ln$ of both sides: $\text{something} = \ln c$. Example: $e^{1.9x} = 20 \Rightarrow 1.9x = \ln 20 = 2.9957 \Rightarrow x = 1.5767$.

**Numbers to know.** $e^{-1} = 0.3679$, $e^{-2} = 0.1353$, $e^{-0.5} = 0.6065$, $\ln 2 = 0.6931$, $\ln 3 = 1.0986$, $\ln 10 = 2.3026$, $\ln 0.9 = -0.1054$, $\ln 0.1 = -2.3026$.

!!! question "Your turn"
    Write $\ln\!\left(\dfrac{x}{2\theta}\,e^{-x^{2}/(2\theta)}\right)$ as a sum of simple terms. Then solve $e^{-\gamma} = 0.9$ for $\gamma$ (4 decimals).

    ???+ solution "Answer"
        $\ln(x/(2\theta)) + \ln(e^{-x^2/(2\theta)}) = \ln x - \ln(2\theta) - \dfrac{x^{2}}{2\theta}$. Note $\ln(2\theta) = \ln 2 + \ln\theta$.

        $e^{-\gamma} = 0.9 \Rightarrow -\gamma = \ln 0.9 = -0.1054 \Rightarrow \gamma = 0.1054$.

### Derivative of $\ln$ and of $e^{\cdot}$

| Function of $\theta$ | Derivative | Example |
|---|---|---|
| $\ln\theta$ | $1/\theta$ | $\frac{d}{d\theta}(5\ln\theta) = 5/\theta$ |
| $\ln(1-\theta)$ | $-1/(1-\theta)$ | chain rule: inside derivative is $-1$ |
| $e^{a\theta}$ | $a e^{a\theta}$ | $\frac{d}{d\theta}e^{-2\theta} = -2e^{-2\theta}$ |
| $c/\theta = c\theta^{-1}$ | $-c/\theta^{2}$ | $\frac{d}{d\theta}\frac{x}{\theta} = -\frac{x}{\theta^{2}}$ |
| $c/\theta^{2}$ | $-2c/\theta^{3}$ | |
| $\ln f(\theta)$ | $f'(\theta)/f(\theta)$ | $\frac{d}{d\theta}\ln\lambda(\theta) = \lambda'(\theta)/\lambda(\theta)$ |

**Setting a derivative to zero and solving.** Example: $\frac{d}{d\theta}\left(20\ln\theta - 8\theta\right) = \frac{20}{\theta} - 8 = 0 \Rightarrow \frac{20}{\theta} = 8 \Rightarrow \theta = \frac{20}{8} = 2.5$.

!!! question "Your turn"
    Differentiate $g(\theta) = 11\ln\theta + 14\ln(1-\theta)$, set to zero, solve for $\theta$.

    ???+ solution "Answer"
        $g'(\theta) = \dfrac{11}{\theta} - \dfrac{14}{1-\theta} = 0 \Rightarrow 11(1-\theta) = 14\theta \Rightarrow 11 = 25\theta \Rightarrow \theta = 11/25 = 0.44$.

## M2 · The Gaussian pdf and the Q function

**Plain words.** The Gaussian (normal) pdf is the bell curve. $\mathcal N(\mu,\sigma^{2})$ means centre $\mu$, spread $\sigma$ (standard deviation; $\sigma^{2}$ is the variance).

$$p(x) = \frac{1}{\sqrt{2\pi\sigma^{2}}}\exp\!\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right)$$

| Symbol | Meaning |
|---|---|
| $\mu$ | mean, where the peak sits |
| $\sigma^{2}$ | variance; $\sigma$ = standard deviation |
| $\frac{1}{\sqrt{2\pi\sigma^2}}$ | the height-fixing constant so the area is 1. For $\sigma=1$ it is $1/\sqrt{2\pi} = 0.3989$ |

**The area to the right.** $Q(x)$ = probability that a standard Gaussian ($\mu=0,\sigma=1$) is larger than $x$:

$$Q(x) = \int_{x}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}\,du$$

Facts you use constantly: $Q(0) = 0.5$. $Q(-x) = 1 - Q(x)$ (symmetry). Area to the left of $x$ is $1 - Q(x)$ (this is the CDF $\Phi(x)$). For a general Gaussian, standardise first: $P(X > a) = Q\!\left(\frac{a-\mu}{\sigma}\right)$.

| $x$ | $Q(x)$ | $x$ | $Q(x)$ |
|---|---|---|---|
| 0 | 0.5000 | 1.5 | 0.0668 |
| 0.5 | 0.3085 | 1.59 | 0.0559 |
| 1.0 | 0.1587 | 1.645 | 0.0500 |
| 1.28 | 0.1003 | 1.96 | 0.0250 |
| 2.0 | 0.0228 | 2.33 | 0.0099 |
| 3.0 | 0.00135 | 2.58 | 0.0049 |

**Exam variant: the erf table.** Some exams give $\operatorname{erf}$ instead of $Q$: CDF $= \frac12\left[1+\operatorname{erf}\!\left(\frac{X-\mu}{\sigma\sqrt2}\right)\right]$ and a table of $\operatorname{erf}(X/\sqrt2)$. Then "area to the left of $X$" $= \frac12(1+\text{table value})$ and "area to the right" $= 1 - $ that $= \frac12(1-\text{table value})$. Example: table says $\operatorname{erf}(1/\sqrt2) = 0.683$, so $P(X>1) = \frac12(1-0.683) = 0.1585$ (which is $Q(1)$, matches above).

**Exam variant: band probabilities.** Nov 2019 gives $P(0\le x\le\sigma) = 0.341$, $P(\sigma\le x\le2\sigma)=0.136$, $P(2\sigma\le x\le3\sigma) = 0.021$. Then $P(x>3\sigma) = 0.5 - 0.341 - 0.136 - 0.021 = 0.002$ and $P(x > \sigma) = 0.5 - 0.341 = 0.159$.

!!! question "Your turn"
    $X\sim\mathcal N(2, 4)$ (so $\sigma = 2$). What is $P(X > 5)$? Use the table.

    ???+ solution "Answer"
        Standardise: $(5-2)/2 = 1.5$. $P = Q(1.5) = 0.0668$.

## M3 · Complex exponentials and cosine identities

**Plain words.** $e^{j\theta}$ is a point on the unit circle at angle $\theta$; $j$ is the imaginary unit. You never need to picture it in this course. You only need three mechanical rules.

<div class="key" markdown>

1. $e^{j\theta} + e^{-j\theta} = 2\cos\theta$. Hence $r\,e^{jk\theta} + r\,e^{-jk\theta} = 2r\cos(k\theta)$.
2. $|1 + a e^{-j\theta}|^{2} = 1 + a^{2} + 2a\cos\theta$ (real $a$). Sign follows $a$: $|1 - a e^{-j\theta}|^{2} = 1 + a^{2} - 2a\cos\theta$.
3. $|1 + a_1 e^{-j\theta} + a_2 e^{-j2\theta}|^{2} = (1 + a_1^{2} + a_2^{2}) + 2(a_1 + a_1 a_2)\cos\theta + 2a_2\cos 2\theta$.

</div>

**Where rule 2 comes from.** $|w|^{2} = w\cdot\bar w$ where $\bar w$ flips the sign of $j$: $(1+ae^{-j\theta})(1+ae^{j\theta}) = 1 + ae^{j\theta} + ae^{-j\theta} + a^{2}e^{0} = 1 + a^{2} + 2a\cos\theta$ by rule 1.

**Worked line.** $|1 + \tfrac18 e^{-j\theta}|^{2} = 1 + \tfrac{1}{64} + 2\cdot\tfrac18\cos\theta = \tfrac{65}{64} + \tfrac14\cos\theta$.

**The $z$ version of the same thing.** Replace $e^{-j\theta}$ by $z^{-1}$ and $e^{j\theta}$ by $z$: $\cos\theta = \frac{z + z^{-1}}{2}$, so a PSD written as "number $+$ number $\cdot\cos\theta$" becomes "$C(1+a^{2}) + Ca(z+z^{-1})$" when it equals $C(1+az^{-1})(1+az)$. Used in [U4](u04-factorisation.md).

**Trig identities the exam hands out.** $\cos\alpha\cos\beta = \frac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$. $\cos^{2}\alpha = \frac{1+\cos2\alpha}{2}$. $\sin^{2}\alpha + \cos^{2}\alpha = 1$. $\tan\alpha = \sin\alpha/\cos\alpha$.

!!! question "Your turn"
    Expand $|1 - \tfrac34 e^{-j\theta}|^{2}$ and $3 + 2e^{j\theta} + 2e^{-j\theta} + e^{j2\theta} + e^{-j2\theta}$ into cosines.

    ???+ solution "Answer"
        $1 + \tfrac{9}{16} - \tfrac32\cos\theta = \tfrac{25}{16} - \tfrac32\cos\theta$.

        $3 + 4\cos\theta + 2\cos2\theta$.

## M4 · Geometric sums

$$\sum_{n=0}^{\infty} q^{n} = \frac{1}{1-q}\quad\text{if } |q|<1,\qquad \sum_{n=0}^{N-1} q^{n} = \frac{1-q^{N}}{1-q}$$

**Worked line (Apr 2025 3a).** Energy of $x[n] = e^{-n}$, $n\ge0$: $\sum_{n\ge0}|e^{-n}|^{2} = \sum_{n\ge0}(e^{-2})^{n}$. Here $q = e^{-2} = 0.1353$, so the sum is $\frac{1}{1-0.1353} = \frac{1}{0.8647} = 1.1565$.

!!! question "Your turn"
    $\sum_{n=0}^{\infty}(1/2)^{2n}$ equals?

    ???+ solution "Answer"
        $(1/2)^{2n} = (1/4)^{n}$, $q = 1/4$: $\frac{1}{1-1/4} = \frac{1}{3/4} = \frac43$.

## M5 · Double integrals: rectangle versus triangle

**Plain words.** $\iint p(x,y)\,dx\,dy$ over a region is "add up $p$ over every point of the region". You do it as two ordinary integrals, inner one first. The only difficulty is writing the limits.

**Rectangle** $0\le x\le1$, $0\le y\le1$: limits are numbers for both: $\int_{0}^{1}\int_{0}^{1}(\cdots)\,dx\,dy$.

**Triangle** $x\ge0$, $y\ge0$, $x+y<1$: the inner limit depends on the outer variable. Four moves:

1. Choose the order: inner $dx$, outer $dy$ (or the reverse, both work).
2. Freeze the outer letter ($y$) as if it were a number.
3. Inner limits: where does $x$ run for that fixed $y$? From $0$ up to $1-y$ (from $x+y<1$).
4. Outer limits: numbers: $y$ from $0$ to $1$.

So $\int_{0}^{1}\int_{0}^{1-y}(\cdots)\,dx\,dy$.

**Worked line (Apr 2025 1c).** Find $c$ so that $\iint (cx+1) = 1$ over the triangle.
Inner: $\int_{0}^{1-y}(cx+1)\,dx$. Antiderivative in $x$: $c\frac{x^{2}}{2} + x$. At $x=1-y$: $c\frac{(1-y)^{2}}{2} + (1-y)$. At $x=0$: $0$. Inner result: $c\frac{(1-y)^{2}}{2} + (1-y)$.
Outer: $\int_{0}^{1}\left[c\frac{(1-y)^{2}}{2} + (1-y)\right]dy$. Substitute $u = 1-y$ (as $y$ goes $0\to1$, $u$ goes $1\to0$, and $du = -dy$, so the integral equals $\int_{0}^{1}[c\frac{u^2}{2}+u]\,du$). Antiderivative: $c\frac{u^{3}}{6} + \frac{u^{2}}{2}$. At $1$: $\frac c6 + \frac12$. At $0$: $0$. Set $\frac c6 + \frac12 = 1 \Rightarrow \frac c6 = \frac12 \Rightarrow c = 3$.

**Marginal pdf = integrate the other variable out.** $p_X(x) = \int p_{X,Y}(x,y)\,dy$ with $y$ running over all values allowed *for that $x$*. On the triangle $0\le y\le x\le1$ (Apr 2024 1c): for fixed $y$, $x$ runs from $y$ to $1$, so $p_Y(y) = \int_{y}^{1}2\,dx = 2(1-y)$.

!!! question "Your turn"
    Region $0\le y\le x\le 1$, pdf $= 2$. Compute $p_X(x) = \int p(x,y)\,dy$. First write the limits of $y$ for a fixed $x$.

    ???+ solution "Answer"
        For fixed $x$, $y$ runs from $0$ to $x$. $p_X(x) = \int_{0}^{x}2\,dy = [2y]_{0}^{x} = 2x - 0 = 2x$, for $0\le x\le1$.

## M6 · Expectation and variance rules

**Plain words.** $E[X]$ is the long-run average of $X$. $\operatorname{Var}(X) = E[(X-\mu)^{2}] = E[X^{2}] - \mu^{2}$ measures spread.

| Rule | Note |
|---|---|
| $E[aX + b] = aE[X] + b$ | constants come out |
| $E[X + Y] = E[X] + E[Y]$ | always |
| $E[XY] = E[X]E[Y]$ | only if independent (or uncorrelated) |
| $E[X^{2}] = \operatorname{Var}(X) + (E[X])^{2}$ | the most used line in this course |
| $\operatorname{Var}(aX) = a^{2}\operatorname{Var}(X)$ | |
| $\operatorname{Var}(X+Y) = \operatorname{Var}X + \operatorname{Var}Y$ | if independent |
| $E[X] = \sum_x x\,p(x)$ or $\int x\,p(x)\,dx$ | "average of the outcomes, weighted by the probability" |

**White noise** $i[n]$ with variance $\sigma_i^{2}$ and zero mean: $E[i[n]] = 0$, $E[i[n]^{2}] = \sigma_i^{2}$, $E[i[n]\,i[m]] = 0$ for $n\ne m$. So when you expand $E[(i[n] + b\,i[n-1])^{2}]$ every cross term dies: $= \sigma_i^{2} + b^{2}\sigma_i^{2}$.

!!! question "Your turn"
    $i[n]$ white, $\sigma_i^2 = 1$. Compute $E[(i[n] - \tfrac12 i[n-1] + \tfrac14 i[n-2])\,(i[n-1] - \tfrac12 i[n-2] + \tfrac14 i[n-3])]$. Hint: only pairs with the same time index survive.

    ???+ solution "Answer"
        Pairs with equal index: $i[n-1]$ appears with coefficient $-\frac12$ in the first bracket and $1$ in the second: $(-\frac12)(1)$. $i[n-2]$: $\frac14$ and $-\frac12$: $(\frac14)(-\frac12)$. Sum: $-\frac12 - \frac18 = -\frac58$.

## M7 · The $z$ domain in four facts

1. $z^{-1}$ means "delay by one sample". A difference equation $x[n] = i[n] - \tfrac12 i[n-1] + \tfrac34 x[n-1]$ becomes $X(z) = I(z) - \tfrac12 z^{-1}I(z) + \tfrac34 z^{-1}X(z)$, so the filter is $H(z) = \dfrac{X(z)}{I(z)} = \dfrac{1 - \tfrac12 z^{-1}}{1 - \tfrac34 z^{-1}}$. Numerator = the $i$ terms, denominator = $1$ minus the $x$ terms moved to the left.
2. The PSD of the output is $P_x(e^{j\theta}) = \sigma_i^{2}\,|H(e^{j\theta})|^{2}$: put $z = e^{j\theta}$ and use [M3](#m3-complex-exponentials-and-cosine-identities) rule 2 top and bottom.
3. Zeros = roots of the numerator, poles = roots of the denominator. $1 - a z^{-1}$ has its root at $z = a$. **Minimum phase** means every pole and zero has $|z|<1$ (inside the unit circle). The innovation filter must be minimum phase, so whenever a quadratic gives two candidates ($a$ and $1/a$) keep the one with $|a| < 1$.
4. Going back from $z$ to time: $(1 + a z^{-1})$ in the numerator means "$+ a\,i[n-1]$"; in the denominator it means "$- a\,x[n-1]$ on the right-hand side".

!!! question "Your turn"
    Write $H(z)$ for $x[n] = i[n] + a\,i[n-1] + b\,i[n-2]$ and name the type (AR, MA or ARMA) and the order.

    ???+ solution "Answer"
        $H(z) = 1 + a z^{-1} + b z^{-2}$. Only $i$ terms, no past $x$: moving average, MA(2).

## M8 · Argmax, "set the derivative to zero", quadratics

**argmax.** $\hat\theta = \arg\max_\theta f(\theta)$ means "the value of $\theta$ where $f$ is biggest", not the biggest value itself. Recipe: differentiate, set to zero, solve. Maximising $f$ and maximising $\ln f$ give the same $\theta$ (ln is increasing), which is why we always take $\ln$ first. Constants that do not contain $\theta$ can be dropped before differentiating.

**Quadratic formula.** $Ax^{2} + Bx + C = 0 \Rightarrow x = \dfrac{-B \pm\sqrt{B^{2}-4AC}}{2A}$. Example: $30a^{2} - 61a + 30 = 0$: $\sqrt{3721 - 3600} = \sqrt{121} = 11$, so $a = \frac{61\pm11}{60}$: $1.2$ or $0.8333 = 5/6$.

**Inequalities and $\ln$.** Taking $\ln$ of both sides keeps the direction of $>$ (ln is increasing). Multiplying both sides by a negative number flips it. Taking the square root of both sides of $x^{2} > c$ (with $x>0$) keeps it: $x > \sqrt c$.

!!! question "Your turn"
    Solve $12a^{2} - 25a + 12 = 0$ and pick the root with $|a|<1$.

    ???+ solution "Answer"
        $\sqrt{625 - 576} = \sqrt{49} = 7$. $a = \frac{25\pm7}{24}$: $\frac{32}{24} = \frac43$ or $\frac{18}{24} = \frac34$. Keep $a = 3/4$.

## M9 · Integrals the exam hands out, and evaluating at $0$ and $\infty$

| Integral | Antiderivative |
|---|---|
| $\int e^{ax}\,dx$ | $\frac1a e^{ax}$ |
| $\int x e^{ax}\,dx$ | $\left(\frac xa - \frac1{a^{2}}\right)e^{ax}$ |
| $\int x^{2}e^{ax}\,dx$ | $\left(\frac{x^{2}}a - \frac{2x}{a^{2}} + \frac2{a^{3}}\right)e^{ax}$ |
| $\int x^{2}e^{-x}\,dx$ | $-e^{-x}(x^{2}+2x+2)$ |
| $\int x^{n}\,dx$ | $\frac{x^{n+1}}{n+1}$ |
| $\int_{0}^{\infty}x^{n}e^{-x}\,dx$ | $n!$ (so $\int_0^\infty x^2 e^{-x}dx = 2$) |

**Evaluating.** $[F(x)]_{a}^{b} = F(b) - F(a)$. At $x\to\infty$ anything of the form (polynomial)$\cdot e^{-cx}$ with $c>0$ goes to $0$ (the exponential wins). At $x = 0$: $e^{0} = 1$.

**Worked line (Nov 2022 2f).** $\int_{0}^{\infty}y^{2}e^{-y}\,dy = [-e^{-y}(y^{2}+2y+2)]_{0}^{\infty}$. Upper limit: $0$. Lower limit: $-e^{0}(0+0+2) = -2$. Subtract: $0 - (-2) = 2$.

**Exponential-tail integrals (detection).** $\int_{\gamma}^{\infty}\lambda e^{-\lambda x}\,dx = e^{-\lambda\gamma}$ and $\int_{0}^{\gamma}\lambda e^{-\lambda x}\,dx = 1 - e^{-\lambda\gamma}$.

!!! question "Your turn"
    Compute $\int_{0}^{\ln 3} e^{-y}\,dy$ and $\int_{\ln3}^{\infty}2e^{-2y}\,dy$ exactly.

    ???+ solution "Answer"
        First: $[-e^{-y}]_{0}^{\ln3} = -e^{-\ln3} - (-e^{0}) = -\frac13 + 1 = \frac23$.

        Second: $[-e^{-2y}]_{\ln3}^{\infty} = 0 - (-e^{-2\ln3}) = e^{-2\ln 3} = (e^{\ln3})^{-2} = 3^{-2} = \frac19$.

## M10 · Matrices you will actually invert

Only $2\times2$ ever appears. $\begin{bmatrix}p&q\\q&p\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix} = \begin{bmatrix}u\\v\end{bmatrix}$ is just two equations: $p a_1 + q a_2 = u$ and $q a_1 + p a_2 = v$. Solve by substitution: from the first, $a_1 = (u - q a_2)/p$; put into the second.

**Worked line (Jun 2026 3d).** $3a_1 + 2a_2 = -2$, $2a_1 + 3a_2 = -1$. Multiply the first by 3 and the second by 2: $9a_1 + 6a_2 = -6$, $4a_1 + 6a_2 = -2$. Subtract: $5a_1 = -4 \Rightarrow a_1 = -0.8$. Back: $2(-0.8) + 3a_2 = -1 \Rightarrow 3a_2 = 0.6 \Rightarrow a_2 = 0.2$.

---

**You can leave this page when you can:**

- [ ] turn $\ln$ of a product of exponentials into a sum, and differentiate it.
- [ ] read $Q(x)$ from a table and standardise a Gaussian.
- [ ] expand $|1 + ae^{-j\theta}|^{2}$ into cosines without thinking.
- [ ] write the limits of a double integral over a triangle in four moves.
- [ ] evaluate an antiderivative at $0$ and $\infty$.

*[pdf]: probability density function: a curve whose area over an interval gives the probability of landing in that interval.
*[variance]: average squared distance from the mean.
*[minimum phase]: all poles and zeros inside the unit circle.
