---
hide:
  - toc
  - navigation
---

<div class="cheat" markdown>

# 5CTA0 cheat sheet · one A4, front and back · boxes numbered as the guide (U1 to U19) · print at 100 % (`cheatsheet.pdf`)

<div class="cheat-cols" markdown>

<div markdown>

## PART 1 · Probability and random signals

### U1 · Total probability and Bayes

IF YOU SEE "machine $M_i$ produces 40 % … defective 2 % for $M_1$ … probability that a chip is defective / given that it is defective, which machine": sources with shares and rates.
{: .see }

1. Shares $P(A_i)$: percentages, or counts divided by the total (18 of 55 patients → $18/55$). They add to 1.
2. Rate of the asked event in each source $P(B\mid A_i)$. If the text gives the opposite event (85 % pass, you want "not pass"), use $1 - 0.85$.
3. Forward ("probability that an item is $B$"): $P(B) = \sum_i P(B\mid A_i)P(A_i)$; write each product, then add.
4. Backward ("given that it is $B$, probability it came from $A_k$"): $P(A_k\mid B) = \dfrac{P(B\mid A_k)P(A_k)}{P(B)}$: that source's product over the sum. All backward answers add to 1.

*Jun26 1b: $0.4(0.02)+0.35(0.04)+0.25(0.05) = 0.0345$; $P(M_2\mid D) = 0.014/0.0345 = 0.41$. Apr24 1b (TB, "99 % accurate" = 0.99 both ways): $0.000495/0.01049 = 0.047$. Lifetime $\Pr[T\ge t] = e^{-t/5}$, "breaks in year 3 given alive at 2": $(e^{-2/5}-e^{-3/5})/e^{-2/5} = 1 - e^{-1/5} = 0.18$.*
Independent events: $P(A\cap B) = P(A)P(B)$, i.e. $P(A\mid B) = P(A)$. Not "$P(A\cap B) = 0$" (disjoint) and not "$P(A\cup B) = P(A)+P(B)$".

### U2 · Joint pdf: constant, marginal, conditional, independence

IF YOU SEE "joint PDF $p_{X,Y}(x,y) = \ldots$ for $0\le x\le1$, $0\le y\le1$ (square) or $x+y<1$ / $0\le y\le x\le1$ (triangle)": limits are the whole job.
{: .see }

1. Draw the region. Square: both limits are numbers. Triangle: choose the order, freeze the outer letter, inner limits depend on it ($x$ from $0$ to $1-y$), outer limits are numbers ($y$ from $0$ to $1$).
2. Constant $c$: double integral $= 1$. Inner antiderivative, evaluate at both limits, then outer. *Apr25 1c: $\int_0^1\!\int_0^{1-y}(cx+1)\,dx\,dy = \frac c6 + \frac12 = 1 \Rightarrow c = 3$.*
3. Marginal $p_X(x) = \int p_{X,Y}\,dy$ with the $y$ limits for that fixed $x$; always write the domain ("for $0\le x\le1$"). *Jun26 1c: $\int_0^1 6x^2y\,dy = 3x^2$. Apr24 1c: $p_Y(y) = \int_y^1 2\,dx = 2(1-y)$.*
4. Conditional $p_{X\mid Y}(x\mid y) = p_{X,Y}/p_Y(y)$, domain = the $x$ range for that $y$. *Apr24 1c: $2/(2(1-y)) = 1/(1-y)$ for $y\le x\le1$.*
5. Independent only if the region is a rectangle AND the formula factors ($6x^2y = 3x^2\cdot2y$: yes; anything on a triangle: no).
6. Discrete table: marginal of $X$ = add across the row ($\frac16+\frac14+\frac18 = \frac{13}{24}$).

### U3 · Random variables and processes (MC facts)

IF YOU SEE "WSS", "ergodic", "expected value", "discrete or continuous", "realisation", "legitimate autocorrelation":
{: .see }

- Expected value = average of the outcomes weighted by the pmf/pdf = mean over infinitely many observations. Not the most probable, not the largest.
- Discrete = countable values (counts, phone numbers, pixel 0–255). Continuous = any value in a range (time, weight).
- A picture is a realisation of a random process; one pixel is a random variable. The ensemble is all realisations.
- WSS: mean constant in time AND autocorrelation depends only on the lag $t-s$ (constant pdf = strict-sense; flat PSD = white noise; time averages = ergodicity).
- Ergodic in the mean: the time average of ONE realisation equals the ensemble mean. i.i.d. dice rolls: ergodic in mean and variance. A random amplitude drawn once per realisation ($A\cos t$, uniform on $[-A,A]$): not ergodic in variance; $A\cos t$ is not even WSS (mean $\cos t$ moves); uniform on $[-A,A]$ has mean 0 and is ergodic in the mean.
- Recipe (Apr24 1d): (1) $E[X(t)]$ over the random ingredient: constant? (2) $E[X(t)X(s)]$ with $\cos\alpha\cos\beta = \frac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$ (terms with $2U$ average to 0): function of $t-s$ only? (3) time average of one realisation equals (1)? $\cos(t+U)$: $0$, $\frac12\cos(t-s)$, $0$ → WSS and ergodic.
- Legitimate autocorrelation: $r[-l] = r[l]$ and $|r[l]|\le r[0]$..
- Covariance: direction by its sign, scale-dependent, unbounded ("all of the above"); correlation coefficient = cov/($\sigma_X\sigma_Y$) in $[-1,1]$. Binomial "exactly $k$ of $n$": $\binom nk p^k(1-p)^{n-k}$; $\binom86 0.8^6 0.2^2 = 0.2936$.

### U4 · Spectral factorisation (PSD → $L(z)$, $\sigma_i^2$)

IF YOU SEE "find the spectral factorization / the innovation filter $L(z)$ and the variance of the input noise" with $P(e^{j\theta}) = \dfrac{\text{number}}{\alpha \pm \beta\cos\theta}$:
{: .see }

1. $\cos\theta = \frac{z+z^{-1}}{2}$, so $\alpha + \beta\cos\theta = \alpha + \frac\beta2 z + \frac\beta2 z^{-1}$.
2. Match to $C(1\pm az^{-1})(1\pm az) = C(1+a^2) \pm Ca(z+z^{-1})$ (sign $+$ if $\beta>0$, $-$ if $\beta<0$): $Ca = |\beta|/2$ and $C(1+a^2) = \alpha$.
3. Divide: $|\beta|a^2 - 2\alpha a + |\beta| = 0$; $a = \dfrac{2\alpha\pm\sqrt{4\alpha^2-4\beta^2}}{2|\beta|}$. Keep the root with $|a|<1$ (minimum phase; the other is $1/a$). $C = |\beta|/(2a)$.
4. $\sigma_i^2 = C_{\text{numerator}}/C_{\text{denominator}}$; $L(z)$ = the $z^{-1}$ halves only: $\dfrac{1\pm bz^{-1}}{1\pm az^{-1}}$.
5. Check by expanding $\sigma_i^2|L(e^{j\theta})|^2 = \sigma_i^2\frac{1+b^2\pm2b\cos\theta}{1+a^2\pm2a\cos\theta}$ back.

*Apr25 1e: $1/(61+60\cos\theta)$: $Ca = 30$, $C(1+a^2) = 61$, $30a^2-61a+30 = 0$, $a = 5/6$ (not 1.2), $C = 36$: $\sigma_i^2 = 1/36$, $L = 1/(1+\frac56z^{-1})$.*
*Apr24 1e: $7/(25-24\cos\theta)$: $12a^2-25a+12=0$, $a = 3/4$, $C = 16$: $\sigma_i^2 = 7/16$, $L = 1/(1-\frac34z^{-1})$. Nov22 1d: $1/(\frac53-\cos\theta)$: $a = \frac13$, $C = \frac32$: $\sigma_i^2 = \frac23$, $L = 1/(1-\frac13z^{-1})$.*
MC: the innovation filter is minimum phase (poles and zeros inside the unit circle), causal, stable; $L(z^{-1})$ (zeros outside) is the wrong mirror; the constant in front of the factorised PSD is $\sigma_i^2$ (Jan22 1d: 2, option c).

## PART 2 · Estimation

### U5 · Maximum likelihood (MLE)

IF YOU SEE "write the likelihood and log-likelihood … derive the MLE for $\theta$", "find an estimator for the parameter" with a pdf $p(x;\theta)$ and $N$ i.i.d. samples:
{: .see }

1. Likelihood = product of the pdf over the samples: constants become $c^N$, exponentials merge: $\exp(\sum\cdot)$, $\theta^k$ in a denominator becomes $\theta^{Nk}$.
2. $\ln$ of the product = sum of $\ln$s: $\ln(ab) = \ln a + \ln b$, $\ln a^n = n\ln a$, $\ln e^u = u$, denominator terms get a minus.
3. Drop every term without $\theta$.
4. Differentiate in $\theta$: $\frac{d}{d\theta}c\ln\theta = c/\theta$; $\frac{d}{d\theta}(c/\theta) = -c/\theta^2$; $\frac{d}{d\theta}(c/\theta^2) = -2c/\theta^3$; $\frac{d}{d\theta}c\theta = c$; nested $\lambda(\theta)$: $\frac{d}{d\theta}\ln\lambda = \lambda'/\lambda$ (sigmoid: $\lambda' = \lambda(1-\lambda)$ so $\lambda'/\lambda = 1-\lambda$).
5. Set to zero, multiply by the denominators, solve for $\theta$. Discard solutions at the boundary ($\lambda = 1$ means $\theta = \infty$). If the question's parameter is inside a sigmoid, invert at the end: $\frac{1}{1+e^{-\theta}} = v \Rightarrow \theta = -\ln(\frac1v - 1)$.
6. One sentence of meaning ("the sample mean divided by $k$").

*Gamma, known $k$ (Jun26 2b): $\ln L = (k-1)\sum\ln x_i - \frac{\sum x_i}{\theta} - nk\ln\theta - n\ln\Gamma(k)$; $\frac{S}{\theta^2} - \frac{nk}{\theta} = 0 \Rightarrow \hat\theta = \frac{\sum x_i}{nk} = \bar x/k$.*
*$\frac{x}{2\theta}e^{-x^2/(2\theta)}$ (Apr24 2c): $\hat\theta = \frac{1}{2N}\sum x_n^2$. Rayleigh $\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}$ (Nov19 3a): $\hat\theta = \sqrt{\frac{1}{2N}\sum x^2}$. $\lambda e^{-\lambda x}$: $\hat\lambda = N/\sum x_i$. Sigmoid (Apr25 2c) $3\lambda e^{-4\lambda x/7}$: $(1-\lambda)(1-\frac47\lambda x) = 0 \Rightarrow \lambda = \frac{7}{4x} \Rightarrow \hat\theta = -\ln(\frac{4x}{7}-1)$. Angle (Nov22 2d): $\hat\theta = \tan^{-1}(x_2/x_1)$, quadrant of $(x_1,x_2)$.*

### U6 · Posterior and MAP

IF YOU SEE "assume a Beta/Gamma/exponential prior … write the likelihood, derive the posterior, compute the MAP, compare with the MLE":
{: .see }

1. Likelihood with the data numbers in ($\sum x_i$, $n$). Prior with constants dropped: Beta$(\alpha,\beta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$; Gamma$(\alpha,\beta)\propto\lambda^{\alpha-1}e^{-\beta\lambda}$.
2. Posterior $\propto$ likelihood × prior: add exponents of $\theta$ and of $e$. Name it: $\theta^{a-1}(1-\theta)^{b-1}$ is Beta$(a,b)$; $\lambda^{a-1}e^{-b\lambda}$ is Gamma$(a,b)$. The denominator $p(x)$ is a number: ignore it for the MAP.
3. MAP = peak: $\ln$, differentiate, zero, solve. Beta: $\frac{a-1}{\theta} = \frac{b-1}{1-\theta} \Rightarrow \hat\theta = \frac{a-1}{a+b-2}$. Gamma: $\frac{a-1}{\lambda} = b \Rightarrow \hat\lambda = \frac{a-1}{b}$.
4. MLE = same without the prior. The prior pulls the MAP toward its own peak; the pull fades as $n$ grows (data terms grow, prior terms do not).

*NegBin $k=2$, Beta(2,3), $x = \{3,5,4,6,4\}$ (Jun26 2c): $L = \prod(x_i-1)\,\theta^{10}(1-\theta)^{12}$ ($\sum x_i = 22$, $\sum(x_i-2) = 12$); posterior $\theta^{11}(1-\theta)^{14}$ = Beta(12,15); MAP $= 11/25 = 0.44$ (MLE $10/22$, prior peak $1/3$).*
*Poisson, Gamma(3,2), $x = \{2,4,3,5,2,4\}$ (Jun26 2d): $L\propto\lambda^{20}e^{-6\lambda}$; posterior $\lambda^{22}e^{-8\lambda}$ = Gamma(23,8); MAP $22/8 = 2.75$; MLE $20/6 = 3.33$; the prior (mode 1) pulls down.*
*Posterior given (Apr25 2d) $\theta^{A}(1-\theta)^{B}$: MAP $= A/(A+B)$ with $A = \beta_1-1+k_1N_1$, $B = \beta_0-1+k_0N_0$. Nov22 2g $(x+a)^2\theta e^{-(x+a)\theta}$: $\frac1\theta - (x+a) = 0 \Rightarrow \frac{1}{x+a}$.*
*Sigmoid posterior (Apr24 2d) $\frac\lambda2 e^{-\lambda x/2}$: $(1-\lambda)(1-\frac{x\lambda}{2}) = 0 \Rightarrow \lambda = \frac2x \Rightarrow \hat\theta = -\ln(\frac x2-1)$, $x>2$. No closed form (Nov19 3c): stop at the equation "derivative $= 0$".*
*Discrete $X\in\{\pm1\}$, $Y = X+N$ (Jan22 2f, 2h): $P[X=1\mid Y] = \frac{e^{-(y-1)^2/2\sigma^2}}{e^{-(y-1)^2/2\sigma^2}+e^{-(y+1)^2/2\sigma^2}}$ (a sum in the denominator); ratio $e^{2y/\sigma^2}\gtrless1 \Rightarrow y_{th} = 0$.*

### U7 · MMSE = posterior mean

IF YOU SEE "find the minimum mean square error estimator" (posterior given or derived in the previous part):
{: .see }

1. $\hat\theta_{MMSE} = E[\theta\mid x] = \int\theta\,p(\theta\mid x)\,d\theta$ over the posterior's range; the posterior must integrate to 1 (divide likelihood × prior by $\int$ likelihood × prior if needed). Discrete: $\sum_x x\,P[X=x\mid Y]$.
2. Substitute to match the handed-out integral ($y = (x+a)\theta$: $\theta = y/(x+a)$, $d\theta = dy/(x+a)$), evaluate antiderivative at $\infty$ (0) and at 0, subtract.

*Nov22 2f: $(x+a)^2\int_0^\infty\theta^2e^{-(x+a)\theta}d\theta = \frac{1}{x+a}\int_0^\infty y^2e^{-y}dy = \frac{2}{x+a}$ (MAP was $\frac1{x+a}$: skewed posterior). Jan22 2g: $(+1)P[1\mid Y] - P[-1\mid Y] = \tanh(y/\sigma^2)$. Mixture $c\,\mathcal N(x,1) + (1-c)\mathcal N(-x,1)$: $x(2c-1)$.*
Means: Beta$(a,b)$: $\frac{a}{a+b}$; Gamma$(a,b)$: $\frac ab$; exponential rate $r$: $\frac1r$. MAP = MMSE only for symmetric posteriors (Gaussian); "always different" is false.

### U8 · Fisher information and CRLB

IF YOU SEE "derive the Fisher information", "find the Cramér–Rao lower bound", "check whether the CRLB can be derived":
{: .see }

0. If the pdf's range depends on $\theta$ ($0\le x\le\theta$): regularity condition violated, no CRLB. Stop (Jan22 2e).
1. $\ln p$ of the full data ($\theta$ terms only). 2. Differentiate twice. 3. Expectation: replace $x$, $x^2$ by $E[x]$, $E[x^2]$ (given in a hint, or integrate). 4. $\mathcal I(\theta) = -E[\partial^2\ln p/\partial\theta^2]$; $N$ samples: $\mathcal I = N\,i(\theta)$; CRLB $= 1/\mathcal I$.

*Nov22 2e: $\ln p \ni \frac{A}{\sigma^2}(x_1\cos\theta + x_2\sin\theta)$; second derivative $\frac{A}{\sigma^2}(-x_1\cos\theta - x_2\sin\theta)$; $E[x_1] = A\cos\theta$, $E[x_2] = A\sin\theta$ → $\mathcal I = A^2/\sigma^2$.*
*Rayleigh (Nov19 3b): $\ln p = \ln x - 2\ln\theta - \frac{x^2}{2\theta^2}$; second derivative $\frac2{\theta^2} - \frac{3x^2}{\theta^4}$; $E[x^2] = 2\theta^2$ → $i = 4/\theta^2$, CRLB $= \theta^2/(4N)$.*
MC: $\operatorname{Var}\ge1/\mathcal I$ (not $\ge\mathcal I$); $\mathcal I\ge0$ (never "strictly negative"); $\mathcal I_N = N i$ so the bound falls as $1/N$; efficient = unbiased AND variance equal to the bound; MLE is asymptotically unbiased/efficient/Gaussian, not "always" at the bound; invariance $\hat\theta = \psi^{-1}(\hat\alpha)$ holds for ML and LS, not MMSE.

### U9 · Least squares

IF YOU SEE "find the linear function having least squares error for the data $\{(x_i,y_i)\}$":
{: .see }

$J(a,b) = \sum(y_i - ax_i - b)^2$; $\partial J/\partial a = -2\sum x_i(y_i - ax_i - b) = 0$, $\partial J/\partial b = -2\sum(y_i - ax_i - b) = 0$; solve the $2\times2$ system by substitution, fractions kept. Closed form: $a = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - (\sum x)^2}$, $b = \frac{\sum y - a\sum x}{n}$. *Apr25 2b, $(0,3),(2,4),(3,3)$: $26a+10b = 34$, $10a+6b = 20$ → $a = \frac1{14}$, $b = \frac{45}{14}$.*
"Which estimator, no noise pdf given": least squares (needs no statistics). Linear in the unknown ($\phi$ known in $Ae^{\phi n}$): closed form $\hat A = \sum x[n]e^{\phi n}/\sum e^{2\phi n}$. Non-linear: write the cost, iterate (Gauss–Newton or Newton–Raphson) or transform ($x = \ln\theta + w \Rightarrow \hat\theta = e^{\bar x}$). The error vector, not the solution, is orthogonal to the columns of $\mathbf H$.

### U10 · Estimation MC: the swap test

A false option is a true sentence with one word swapped: *always · regardless · only · strictly · $x\leftrightarrow\theta$ · mean $\leftrightarrow$ maximum · $\mathcal I\leftrightarrow1/\mathcal I$ · negative*. True: MLE = $\arg\max_\theta p(x\mid\theta)$ ($\arg\min\sum(\cdot)^2$ is LS, $\arg\max p(\theta\mid x)$ is MAP); MMSE = posterior mean; MAP = posterior maximum, needs a prior; Bayes risk $\iint C(e)p(\theta\mid x)d\theta\,p(x)dx$ is minimised: quadratic cost → MMSE, hit-or-miss → MAP; Bayesian estimators DO use prior knowledge.

</div>
<div markdown>

## PART 3 · Spectral estimation

### U11 · Correlogram from lags

IF YOU SEE "calculate the correlogram / the PSD in a non-parametric fashion … as a function of cosines" with $r[0], r[\pm1], r[\pm2]$ and "assume $r[k] = 0$ beyond":
{: .see }

$\hat P_{corr}(e^{j\theta}) = r[0] + 2r[1]\cos\theta + 2r[2]\cos2\theta + \cdots$ (every lag except 0 is doubled; comes from $r[k]e^{-jk\theta} + r[-k]e^{jk\theta} = 2r[k]\cos k\theta$). Values: at $\theta = 0$ all cosines are 1; at $\pi$ they alternate $-1, +1, -1$; at $\pi/2$: $0, -1, 0, +1$. It may go negative (a flaw of truncation); a parametric PSD never does.
*Jun26 3c ($3,2,1$): $3+4\cos\theta+2\cos2\theta$ (9 at 0, 1 at $\pi$). Apr25 3d ($2,-\frac14,-\frac3{16}$): $2 - \frac12\cos\theta - \frac38\cos2\theta$ (1.125 at 0, 2.125 at $\pi$). Apr24 3d: $\frac{25}{16} - \frac32\cos\theta + \cos2\theta - \cos3\theta$ (0.06 at 0, 5.06 at $\pi$). Jan22 3c: $\frac{13}8 - \frac{15}8\cos\theta + \frac12\cos2\theta$.*

### U12 · AR model by Yule–Walker

IF YOU SEE "model as an AR($p$) process, find the parameters / state the Yule–Walker equations in matrix form / variance of the driving noise / PSD as a function of $\cos\theta$":
{: .see }

Model (course signs): $x[n] = i[n] - a_1x[n-1] - a_2x[n-2]$, $H(z) = 1/(1 + a_1z^{-1} + a_2z^{-2})$.

1. Yule–Walker, one line per lag $m = 1..p$: $r[m] + a_1r[m-1] + a_2r[m-2] = 0$ (use $r[-1] = r[1]$). Matrix: $\begin{bmatrix}r_0&r_1\\r_1&r_0\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix} = -\begin{bmatrix}r_1\\r_2\end{bmatrix}$ (or augmented $\begin{bmatrix}r_0&r_1&r_2\\r_1&r_0&r_1\\r_2&r_1&r_0\end{bmatrix}\begin{bmatrix}1\\a_1\\a_2\end{bmatrix} = \begin{bmatrix}\sigma_i^2\\0\\0\end{bmatrix}$). AR(1): $a_1 = -r[1]/r[0]$.
2. $\sigma_i^2 = r[0] + a_1r[1] + a_2r[2]$ (must be between 0 and $r[0]$).
3. $P_{AR} = \dfrac{\sigma_i^2}{|1 + a_1e^{-j\theta} + a_2e^{-j2\theta}|^2}$; AR(1) denominator $1 + a_1^2 + 2a_1\cos\theta$; AR(2) denominator $(1+a_1^2+a_2^2) + 2(a_1 + a_1a_2)\cos\theta + 2a_2\cos2\theta$. Clear fractions by multiplying top and bottom.

*Jun26 3d ($3,2,1$): $3a_1+2a_2 = -2$, $2a_1+3a_2 = -1$ → $a_1 = -0.8$, $a_2 = 0.2$, $\sigma_i^2 = 3-1.6+0.2 = 1.6$, $P = 1.6/(1.68 - 1.92\cos\theta + 0.4\cos2\theta)$ (10 at 0, 0.4 at $\pi$).*
*Apr25 3e ($2,-\frac14$): $a_1 = \frac18$, $\sigma_i^2 = 2-\frac1{32} = \frac{63}{32}$, $P = \frac{63/32}{65/64+\frac14\cos\theta} = \frac{126}{65+16\cos\theta}$. Nov22 3f ($1,-\frac18$): $a_1 = \frac18$, $\sigma_i^2 = \frac{63}{64}$, $P = \frac{63}{65+16\cos\theta}$. Jan22 3d ($\frac{13}8,-\frac{15}{16}$): $a_1 = \frac{15}{26}$, $\sigma_i^2 = \frac{451}{416}$. Apr24 3e ($\frac{25}{16},-\frac34,\frac12$): $a_1 = \frac{204}{481}$, $a_2 = -\frac{56}{481}$, $\sigma_i^2 = 1.19$.*

### U13 · MA model from lags

IF YOU SEE "model as an MA(1) process, find the parameters … PSD as a function of cosines", "MA(2) … calculate $a$ and $b$":
{: .see }

MA(1) $x = i + b_1i[n-1]$: $r[0] = \sigma_i^2(1+b_1^2)$, $r[1] = \sigma_i^2b_1$, $r[k\ge2] = 0$.

1. $\rho = r[1]/r[0] = \dfrac{b_1}{1+b_1^2}$ → $\rho b_1^2 - b_1 + \rho = 0$ → $b_1 = \dfrac{1\pm\sqrt{1-4\rho^2}}{2\rho}$; the roots multiply to 1; keep $|b_1|<1$ (minimum phase).
2. $\sigma_i^2 = r[1]/b_1$ (check $\sigma_i^2(1+b_1^2) = r[0]$).
3. $P_{MA} = \sigma_i^2(1 + b_1^2 + 2b_1\cos\theta) = r[0] + 2r[1]\cos\theta$ (ignores $r[2]$ and beyond). If the process is truly MA(1) (only lags $0,\pm1$ given), this equals the correlogram exactly (Jan20 3b).

MA(2) with unit-variance input, $x = i + ai_1 + bi_2$: $r[2] = b$, $r[1] = a(1+b)$, $r[0] = 1+a^2+b^2$. *Jan22 3b: $b = \frac14$, $a = -\frac{15}{16}/\frac54 = -\frac34$, $r[0] = \frac{13}8$.*
*Apr25 3f and Nov22 3g: $\rho = -\frac18$ → $b_1^2 + 8b_1 + 1 = 0$ → $b_1 = -4+\sqrt{15} = -0.127$; $\sigma_i^2 = -0.25/-0.127 = 1.97$ (Apr25) or $0.984$ (Nov22); $P = 2 - 0.5\cos\theta$ / $1 - 0.25\cos\theta$.*
MC: MA fit needs non-linear equations (Jan19 1d C true); MA($q$) autocorrelation is zero beyond lag $q$; linear prediction (Wiener) gives AR, not MA, coefficients.

### U14 · Difference equation → model name, PSD, autocorrelation

IF YOU SEE "$x[k] = i[k] - i[k-1] + \frac34x[k-1]$ … which kind of process / PSD / autocorrelation" or "filtered with $H(z) = \ldots$":
{: .see }

- Name: only $i$ terms → MA($q$), $q$ = oldest kick; $i[n]$ + past $x$ → AR($p$); both → ARMA($p,q$). $H(z)$: numerator = $i$ coefficients, denominator = $1 - $(coefficients of past $x$ on the right side).
- PSD $= \sigma_i^2|H(e^{j\theta})|^2$; $|1 + ce^{-j\theta}|^2 = 1 + c^2 + 2c\cos\theta$ top and bottom. *Nov22 3d: $\frac78\cdot\frac{2-2\cos\theta}{\frac{25}{16}-\frac32\cos\theta} = 28\frac{1-\cos\theta}{25-24\cos\theta}$ (0 at $\theta=0$).*
- MA lags: slide the coefficient list $[1,b_1,b_2,\ldots]$ over itself by $k$, add the products, times $\sigma_i^2$. *Apr24 3c, $[1,-\frac12,\frac14,-\frac12]$: $r_0 = \frac{25}{16}$, $r_1 = -\frac12-\frac18-\frac18 = -\frac34$, $r_2 = \frac14+\frac14 = \frac12$, $r_3 = -\frac12$.*
- ARMA(1,1) $x = i + b_1i_1 - a_1x_1$ (here $b_1 = -1$, $-a_1 = \frac34$): multiply by $x$ and by $x_1$, take $E$. Rules: $E[i^2] = \sigma_i^2$; $E[i\,x_1] = 0$ (future kick); $E[i_1x_1] = \sigma_i^2$ (the past signal contains the past kick with coefficient 1); $E[x_1^2] = r_0$. *Nov22 3e: $r_0 = \frac78+\frac78+\frac9{16}r_0 - \frac32\cdot\frac78 \Rightarrow r_0 = 1$; $r_1 = -\frac78 + \frac34r_0 = -\frac18$; $r[\tau] = \frac34r[\tau-1]$ for $\tau\ge2$, so $r[\tau] = -\frac18(\frac34)^{|\tau|-1}$.*

### U15 · Spectral estimation theory

IF YOU SEE "which statement is TRUE/FALSE about the periodogram / windows / zero padding", "fill the table of PSD estimators", "energy or power signal", "Welch: how many segments", "AR model order":
{: .see }

| Method | Idea | Bias | Variance |
|---|---|---|---|
| Periodogram (= correlogram, FT of the biased $\hat r$) | $\frac1N\lvert\sum x[n]e^{-jn\theta}\rvert^2$ | asymptotically unbiased (FT of the biased $\hat r$) | $\propto P^2$, does not fall with $N$: NOT consistent |
| Bartlett | $K$ non-overlapping segments, average periodograms | increases (shorter segments) | $/K$ |
| Welch (WOSA) | overlapping (50 %) windowed segments, average | like Bartlett | roughly $/K$ but not exactly (correlated segments); lower than Bartlett for the same $N$ |
| Blackman–Tukey | window the autocorrelation (lag window $M<N$), then FT | more with shorter $M$ | less; consistent |

- Consistent: Bartlett, Welch, Blackman–Tukey, parametric. FT of autocorrelation: correlogram, Blackman–Tukey. Averages periodograms: Bartlett, Welch. Overlap: Welch. "Variance ∝ square of the true spectrum": periodogram (if the table says "bias", the intended answer is still periodogram).
- Welch segments: $K = \frac{N-L}{L(1-\text{overlap})} + 1$; variance ratio $1/K$ if independent. *Jun26 3b: $N = 1000$, $L = 200$, 50 %: $K = 800/100+1 = 9$, ratio $1/9$.* Bartlett: $K = N/L$.
- Windows: main-lobe width → resolution (wider = worse); side-lobe height → leakage (higher = more). Same length: rectangular = narrowest main lobe (best resolution), highest side lobes (most leakage); triangular/Hanning/Hamming widen the lobe, lower the side lobes. Longer window → better resolution, leakage (relative side-lobe level) unchanged. Zero padding to $L$ points = sampling the same FTD at $\theta = 2\pi k/L$: interpolation, NO resolution gain, no variance change.
- Jan22 3a: infinite cosine → two lines (B); windowed → sinc with side lobes (D); zero-padded DFT → circles sampling D (C); 24-point DFT at $f_s/2$ → only the peaks (A): 1B 2D 3C 4A.
- Energy $E = \int|x|^2dt$ or $\sum|x[n]|^2$; power $P = \lim\frac1T\int_{-T/2}^{T/2}|x|^2dt$. Finite $E$ → energy signal, $P = 0$. Periodic → power signal, $E = \infty$. *$A\sin\omega t$: $P = A^2/2$ (via $\sin^2 = \frac{1-\cos2\omega t}2$). $e^{-n}u[n]$: $E = \sum(e^{-2})^n = \frac1{1-e^{-2}} = 1.157$. $e^{-t}u(t)$: $E = \frac12$; $\cos t\,u(t)$: $P = \frac14$.*
- AR order (Jun26 3e): residual variance always decreases with $p$ → cannot choose $p$; risk = overfitting (spurious peaks, parameter variance). Criteria add a penalty growing with $p$: AIC $= N\ln\hat\sigma_p^2 + 2p$, MDL $= N\ln\hat\sigma_p^2 + p\ln N$, FPE $= \hat\sigma_p^2\frac{N+p+1}{N-p-1}$; pick the minimum. Any spectrum (even MA nulls) is approximated by AR with a sufficiently high order $p$.
- Which plot: evaluate each PSD at $\theta = 0$ (cosines $= 1$) and $\pi$ (alternate signs); AR and MA fitted to the same two lags nearly overlap; a parametric PSD is never negative. *Apr25 3g: corr 1.125 / 2.125, AR 1.56 / 2.57, MA 1.5 / 2.5 → plot D (option a). Apr24 3f: corr 0.06 / 5.06, AR 0.69 / 5.6 → plot B (option c).*

## PART 4 · Detection

### U16 · Likelihood ratio test → threshold on $x$

IF YOU SEE "construct the likelihood-ratio test for a threshold $\eta$", "show that the LRT takes the form $\sum|x_n|\gtrless\gamma'$", "for which $x$ should $H_1$ be accepted", "derive the log-likelihood ratio test":
{: .see }

1. $L(x) = \dfrac{p(x;H_1)}{p(x;H_0)}$, $H_1$ on top. $N$ samples: products → $c^N$ and $\exp(\sum)$.
2. Cancel common factors ($x$, $k_1$); $e^a/e^b = e^{a-b}$; $x^a/x^b = x^{a-b}$.
3. $L\gtrless\gamma$, take $\ln$ (direction kept). 4. Isolate the data term; dividing by a negative flips the inequality AND swaps the $H_0/H_1$ labels. 5. $x^2>c$ with $x>0$ → $x>\sqrt c$; $e^x>c$ → $x>\ln c$. 6. Say "decide $H_1$ when …"; the answer is a range. 7. Test a far point.

*Rayleigh$(\sigma_0)$ vs Rayleigh$(\sigma_1)$ (Jun26 4b): $L = \frac{\sigma_0^2}{\sigma_1^2}\exp[\frac{x^2}{2}(\frac1{\sigma_0^2}-\frac1{\sigma_1^2})]$ (bracket $>0$); decide $H_1$ when $x > \sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln(\eta\sigma_1^2/\sigma_0^2)}$. Closer $\sigma$'s → curves overlap → $P_D\to P_{FA}$, ROC → diagonal.*
*Apr25 4a, $p = k_1\theta x^{k_2\theta-1}$, $\theta = 3$ vs $6$, $\lambda = 0.2$: $L = \frac{6x^{11}}{3x^5} = 2x^6\ge0.2 \Rightarrow x\ge0.1^{1/6} = 0.68$.*
*Laplacian (Nov22 4c) $\frac12e^{-|x|}$ vs $e^{-2|x|}$: $L = 2^Ne^{-\sum|x_n|}$; $\sum|x_n|\underset{H_1}{\overset{H_0}{\gtrless}}N\ln2 - \ln\gamma$ (small sum → $H_1$). Gaussian variances (Nov19 4c, Oct21 4b): $\ln L = N\ln\frac{\sigma_0}{\sigma_1} - \frac{\sum x^2}{2\sigma_1^2} + \frac{\sum x^2}{2\sigma_0^2} > \ln\gamma$. Rayleigh 1 vs $\frac14$ (deck): $L = \frac14e^{3x^2/8}$, $x>\sqrt{\frac83\ln4\lambda} = 1.92$.*
Definitions (Jan19 3a): $P_{fa} = \int_{\{L>\gamma\}}p(x;H_0)dx$, $P_d = \int_{\{L>\gamma\}}p(x;H_1)dx$.

### U17 · $P_{FA}$, $P_D$, $P_M$: shade and compute

IF YOU SEE "sketch the likelihoods … indicate $P_{FA}$ and $P_M$ … calculate $P_D$ and $P_{FA}$ for $\gamma = 1$", "for $P_{FA} = 0.1$ calculate the threshold", "plot the ROC":
{: .see }

Curve = the truth, side = what you said. $P_{FA}$ = $H_0$ curve on the $H_1$ side. $P_D$ = $H_1$ curve on the $H_1$ side. $P_M = 1 - P_D$ = $H_1$ curve on the $H_0$ side.

1. $\gamma = 1$: threshold on the axis = where the curves cross: set $p_1 = p_0$, divide, take $\ln$, solve (quadratic if Gaussian vs exponential).
2. Which side is $H_1$: test $y = 0$ (or a large $y$); the side where $p_1 > \gamma p_0$. It can be the LEFT (Nov22, Jan20). "Pay attention to the inequality" = this.
3. Integrals with explicit limits; two-sided region $|y|>y_{th}$: double one tail.
4. Evaluate: $\int_0^\gamma\lambda e^{-\lambda y}dy = 1 - e^{-\lambda\gamma}$; $\int_\gamma^\infty\lambda e^{-\lambda y}dy = e^{-\lambda\gamma}$; Gaussian: standardise, $P(X>a) = Q(\frac{a-\mu}{\sigma})$, area to the left $= 1-Q$; erf table: left area $= \frac12(1+\text{erf})$, right $= \frac12(1-\text{erf})$; band values: tail beyond $3\sigma = 0.5-0.341-0.136-0.021 = 0.002$, beyond $1\sigma = 0.159$.
5. Threshold from a target: write $P_{FA}(\gamma') = $ target, solve with $\ln$. Then $P_D$ at that $\gamma'$; reuse $e^{-\gamma'}$: $e^{-2\gamma'} = (e^{-\gamma'})^2$.
6. Check $P_D > P_{FA}$. ROC: $P_D$ vertical, $P_{FA}$ horizontal, through $(0,0)$ and $(1,1)$, above the diagonal; more separation → closer to the top-left.

*Apr24 4b / Jan22 4b-c: $\frac14e^{-y/2} = \frac{1}{\sqrt{2\pi}}e^{-y^2/2}$ → $e^{y^2/2-y/2} = \frac4{\sqrt{2\pi}} = 1.596$ → $y^2 - y - 0.935 = 0$ → $y_{th} = 1.588$; $H_1$ outside ($|y|>1.588$). $P_{FA} = 2Q(1.59) = 0.112$; $P_D = 2\cdot\frac14\int_{1.588}^\infty e^{-y/2}dy = e^{-0.794} = 0.452$ (one-sided, as printed in Apr24: $0.056$ and $0.226$).*
*Nov22 4d-e, $e^{-y}$ vs $2e^{-2y}$, $H_1$ when $y<\gamma'$: $P_{FA} = 1 - e^{-\gamma'} = 0.1 \Rightarrow \gamma' = -\ln0.9 = 0.105$; $P_D = 1 - e^{-2\gamma'} = 1 - 0.81 = 0.19$.*
*Nov19 4b, $\sigma_1 = 3\sigma_0$, $x_{th} = \sigma_1$: $P_{fa} = 2(0.002) = 0.004$, $P_d = 2(0.159) = 0.318$. Gaussian means (Oct21 4a): $H_1$ when $y>y_{th}$, $P_{fa} = \frac12(1-\text{erf}(\frac{y_{th}}{\sqrt2}))$, $P_d = \frac12(1-\text{erf}(\frac{y_{th}-\mu}{\sqrt2}))$. Exponentials (Jan20 5): $H_1$ on the left, $P_d = 1-e^{-\lambda_1x_{th}}$, $P_{fa} = 1-e^{-\lambda_0x_{th}}$.*

### U18 · Bayesian detector: priors and costs

IF YOU SEE "prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$ … equal costs … when should $H_1$ be accepted", "$C_{0,1} = 100C_{1,0}$ … the posterior of $H_0$ is 5 times smaller", "find $\gamma''$ where $p(y|H_1)P_1 = p(y|H_0)P_0$":
{: .see }

$C_{ij}$ = cost of deciding $H_i$ when $H_j$ is true: $C_{10}$ false alarm, $C_{01}$ miss.
$L(x)\gtrless\eta = \dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$; equivalently $\dfrac{p(H_1\mid x)}{p(H_0\mid x)}\gtrless\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$ (posteriors already contain the priors). Equal costs: $\eta = P_0/P_1$ (minimises $P_e = P_0P_{FA} + P_1P_M$). Equal costs and priors: $\eta = 1$ (ML). Scaling all costs changes nothing. Larger $P_0$ or $C_{10}$ → larger $\eta$; larger $P_1$ or $C_{01}$ → smaller $\eta$.
*Jun26 4c: $\eta = 0.9/0.1 = 9$ → plug into the Rayleigh LRT: $x\ge\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{9\sigma_1^2}{\sigma_0^2}}$. Apr25 4c: threshold $C_{10}/(100C_{10}) = 0.01$; posterior ratio $5\ge0.01$ → $H_1$: the student fails. Nov22 4f-g: $1.2e^{-2y} = 0.4e^{-y} \Rightarrow e^y = 3$, $\gamma'' = \ln3$, $H_1$ when $y<\ln3$; $P_{FA} = 1-e^{-\ln3} = \frac23$, $P_M = e^{-2\ln3} = \frac19$, $P_e = 0.4\cdot\frac23 + 0.6\cdot\frac19 = \frac13$.*

### U19 · Detection MC

Decide $H_1$, truth $H_0$: false alarm = false positive = type I ($P_{FA}$). Decide $H_0$, truth $H_1$: miss = false negative = type II ($P_M$). Neyman–Pearson: for a FIXED $P_{FA}$, $P_D$ is MAXIMISED (lies: "minimised", "fixed $P_D$", "$P_{FA} = P_D$"); always a threshold on the likelihood ratio. Bayesian: Bayes risk MINIMISED; $C_{01} = C_{10}$ (1 or 10), $C_{00} = C_{11} = 0$ minimises $P_e$. Matched filter: maximises output SNR; $h[n] = s[N-1-n]$ (time-reversed, not $s[n]$); correlated noise → prewhiten, so "only uncorrelated noise" is false. ROC below the diagonal = swapped hypotheses or axes, or CDF used for $P_d$; a large $H_0$ variance cannot cause it (Oct21 1e).

## Calculations · the algebra under every answer

- $\ln$: $\ln(ab) = \ln a+\ln b$; $\ln a^n = n\ln a$; $\ln e^u = u$; $\ln\prod = \sum\ln$; $e^ae^b = e^{a+b}$; $e^a/e^b = e^{a-b}$; $(e^a)^n = e^{an}$; $e^{-2\ln3} = 3^{-2} = \frac19$; $e^{-\ln3} = \frac13$; solve $e^{ku} = c$: $u = \ln c/k$.
- Derivatives: $(\ln\theta)' = 1/\theta$; $(\ln(1-\theta))' = -1/(1-\theta)$; $(c/\theta)' = -c/\theta^2$; $(c/\theta^2)' = -2c/\theta^3$; $(e^{a\theta})' = ae^{a\theta}$; $(\ln f)' = f'/f$.
- Integrals: $\int e^{ax} = \frac1ae^{ax}$; $\int xe^{ax} = (\frac xa - \frac1{a^2})e^{ax}$; $\int x^2e^{ax} = (\frac{x^2}a - \frac{2x}{a^2} + \frac2{a^3})e^{ax}$; $\int_0^\infty x^ne^{-x}dx = n!$ ($\int_0^\infty x^2e^{-x} = 2$, $\int_0^\infty xe^{-x} = 1$); $\int_0^\infty\theta e^{-c\theta}d\theta = 1/c^2$; $\int_0^\infty\theta^2e^{-c\theta}d\theta = 2/c^3$; $[F]_a^b = F(b) - F(a)$; at $\infty$, polynomial $\times e^{-cx}\to0$; $\int_0^1 y\,dy = \frac12$, $\int_0^1y^2dy = \frac13$. Substitution $y = c\theta$: $d\theta = dy/c$.
- Rayleigh moment: $E[x^2] = \int_0^\infty x^2\frac{x}{\theta^2}e^{-x^2/2\theta^2}dx = 2\theta^2$ (put $u = x^2/2\theta^2$). $E[X^2] = \operatorname{Var} + \mu^2$.
- Cosines: $e^{jk\theta}+e^{-jk\theta} = 2\cos k\theta$; $|1+ae^{-j\theta}|^2 = 1+a^2+2a\cos\theta$; $|1+a_1e^{-j\theta}+a_2e^{-j2\theta}|^2 = (1+a_1^2+a_2^2) + 2(a_1+a_1a_2)\cos\theta + 2a_2\cos2\theta$; $\cos\theta = \frac{z+z^{-1}}2$; $\cos\alpha\cos\beta = \frac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$; $\sin^2 = \frac{1-\cos2\alpha}2$; $\cos^2 = \frac{1+\cos2\alpha}2$; at $\theta=\pi$: $\cos k\pi = (-1)^k$; at $\pi/2$: $0,-1,0,1$.
- Quadratic $Ax^2+Bx+C = 0$: $x = \frac{-B\pm\sqrt{B^2-4AC}}{2A}$; $b^2+8b+1 = 0$: $-4\pm\sqrt{15}$; $y^2-y-0.935 = 0$: $\frac{1\pm2.177}2$.
- Geometric: $\sum_{n\ge0}q^n = \frac1{1-q}$ ($|q|<1$).
- Inequalities: $\ln$ keeps the direction; multiplying by a negative flips it (and swaps $H_0/H_1$); $\sqrt{\cdot}$ keeps it for positives.

## Numbers

$e^{-1} = 0.3679$, $e^{-2} = 0.1353$, $e^{-0.5} = 0.6065$, $e^{-0.794} = 0.452$, $\ln2 = 0.693$, $\ln3 = 1.099$, $\ln4 = 1.386$, $\ln10 = 2.303$, $\ln20 = 2.996$, $\ln0.9 = -0.1054$, $\ln0.1 = -2.303$, $\sqrt{2\pi} = 2.5066$, $1/\sqrt{2\pi} = 0.3989$, $4/\sqrt{2\pi} = 1.596$, $\sqrt{15} = 3.873$, $1/(1-e^{-2}) = 1.1565$, $0.1^{1/6} = 0.681$.
$Q(x)$ = area right of $x$ for $\mathcal N(0,1)$; $Q(-x) = 1-Q(x)$; $Q(0) = 0.5$, $Q(1) = 0.1587$, $Q(1.28) = 0.100$, $Q(1.5) = 0.0668$, $Q(1.59) = 0.0559$, $Q(1.645) = 0.050$, $Q(1.96) = 0.025$, $Q(2) = 0.0228$, $Q(3) = 0.00135$. erf$(x/\sqrt2)$, $x = 1,2,3$: $0.683, 0.954, 0.997$ ($\frac12(1-0.683) = 0.1585 = Q(1)$).

</div>
</div>
</div>
