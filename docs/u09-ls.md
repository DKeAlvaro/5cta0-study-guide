# U9 · Least squares: fit a line, and when the model is not linear

<div class="meta"><span class="hot">Rank 11 · 1 p in Apr 2025; 2.5 p outliers in 2019 and 2020</span><span>40 min</span></div>

!!! need "Before this page"
    Differentiation of a sum of squares (you know this), [M10 two equations in two unknowns](maths.md#m10-matrices-you-will-actually-invert).

## The idea in plain words

You have points and a model with knobs. **Least squares** turns the knobs until the sum of the squared vertical gaps between the points and the model is as small as possible. No pdf, no noise model: it only needs the data and the model. That is also its weakness and its selling point in MC questions.

!!! idea "The thing that confused me"
    "Linear" least squares does not mean the fitted curve is a straight line. It means the model is linear **in the unknowns**: $A e^{\phi n}$ is linear in $A$ (if $\phi$ is known) and non-linear in $\phi$. Linear in the unknowns → one closed formula. Non-linear → iterate (Gauss–Newton) or transform.

## A tiny example with numbers

Points $(0, 1)$, $(1, 3)$, $(2, 5)$; model $y = ax + b$.
$J(a,b) = (1 - b)^2 + (3 - a - b)^2 + (5 - 2a - b)^2$.
$\frac{\partial J}{\partial a} = 2(3-a-b)(-1) + 2(5-2a-b)(-2) = -6 + 2a + 2b - 20 + 8a + 4b = 10a + 6b - 26$.
$\frac{\partial J}{\partial b} = -2(1-b) - 2(3-a-b) - 2(5-2a-b) = -18 + 6a + 6b$.
Set both to zero: $10a + 6b = 26$ and $6a + 6b = 18$. Subtract: $4a = 8 \Rightarrow a = 2$; then $12 + 6b = 18 \Rightarrow b = 1$. The line $y = 2x + 1$ passes exactly through all three points, $J = 0$.

!!! question "Your turn"
    Points $(0,0)$, $(1,1)$, $(2,3)$. Write $J(a,b)$, the two derivatives, and solve.

    ???+ solution "Answer"
        $J = b^2 + (1-a-b)^2 + (3-2a-b)^2$. $\partial_a$: $-2(1-a-b) - 4(3-2a-b) = 10a + 6b - 14$. $\partial_b$: $2b - 2(1-a-b) - 2(3-2a-b) = 6a + 6b - 8$. From the second, $6b = 8 - 6a$; into the first: $10a + 8 - 6a - 14 = 0 \Rightarrow a = 1.5$, $b = (8-9)/6 = -1/6$.

## The formulas, every symbol named

<div class="key" markdown>

$$J(\boldsymbol\theta) = \sum_n\left(x[n] - s[n;\boldsymbol\theta]\right)^2,\qquad \hat{\boldsymbol\theta}_{LS} = \arg\min_{\boldsymbol\theta}J,\qquad \text{linear model } \mathbf x = \mathbf H\boldsymbol\theta + \mathbf w:\ \hat{\boldsymbol\theta} = (\mathbf H^T\mathbf H)^{-1}\mathbf H^T\mathbf x$$

</div>

| Symbol | Meaning |
|---|---|
| $x[n]$ | the measured values |
| $s[n;\boldsymbol\theta]$ | the model's prediction for sample $n$ with parameters $\boldsymbol\theta$ |
| $\mathbf H$ | observation matrix: one row per sample, one column per unknown; for a line, row $n$ is $[x_n\ \ 1]$ |
| $(\mathbf H^T\mathbf H)^{-1}\mathbf H^T\mathbf x$ | the "normal equations" solved; for two unknowns it is the same as setting the two partial derivatives to zero |
| orthogonality principle | the error vector $\mathbf x - \mathbf H\hat{\boldsymbol\theta}$ is perpendicular to the columns of $\mathbf H$ (the fit $\mathbf H\hat{\boldsymbol\theta}$ lies in their span) |

**Line through points, closed form** (same as the derivative method): with $n$ points,
$a = \dfrac{n\sum x_iy_i - \sum x_i\sum y_i}{n\sum x_i^2 - (\sum x_i)^2}$, $b = \dfrac{\sum y_i - a\sum x_i}{n}$.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "find the linear function having least squares error for the data $\{(x_i, y_i)\}$" | fit $y = ax + b$: write $J$, two partial derivatives, solve the $2\times2$ system (or the closed form) |
| "what kind of estimators can be used … explain your reasoning" | no noise pdf given → least squares (needs no statistics); if the noise were Gaussian, MLE coincides with LS |
| "for the case where $\phi$ is known but $A$ is unknown, find an estimator for $A$" | the model is linear in $A$: differentiate $J$ in $A$ only, one line |
| "write the cost function … the expression will be non-linear" | write $J(\boldsymbol\theta) = \sum(x[n] - s[n;\boldsymbol\theta])^2$ and say which parameter enters non-linearly |
| "formulate the Gauss–Newton solution … show the iterative formulation" | write the update $\boldsymbol\theta_{k+1} = \boldsymbol\theta_k + (\mathbf H_k^T\mathbf H_k)^{-1}\mathbf H_k^T(\mathbf x - \mathbf s(\boldsymbol\theta_k))$ with $\mathbf H_k = \partial\mathbf s/\partial\boldsymbol\theta$ at $\boldsymbol\theta_k$ |
| "can you find a closed-form solution" for $x[n] = \ln\theta + w[n]$ | transform: $\alpha = \ln\theta$ makes it linear; $\hat\alpha = \bar x$; map back $\hat\theta = e^{\bar x}$ |

## Recipe

!!! recipe key "U9 · Line fit by hand"
    1. Write $J(a,b) = \sum_i(y_i - ax_i - b)^2$ with the numbers in.
    2. Differentiate with respect to $a$: $\sum -2x_i(y_i - ax_i - b)$; with respect to $b$: $\sum -2(y_i - ax_i - b)$.
    3. Set both to zero; you get $a\sum x_i^2 + b\sum x_i = \sum x_iy_i$ and $a\sum x_i + nb = \sum y_i$.
    4. Solve the $2\times2$ system by substitution ([M10](maths.md#m10-matrices-you-will-actually-invert)). Keep fractions.
    5. Check: plug one point into the line; the residual should be small, and residuals should sum to zero.

## Worked exam question, one step at a time

!!! exam "April 2025 · 2b · 1 p"
    Find the linear function having least squares error for the data $\{(0, 3), (2, 4), (3, 3)\}$.

<div class="stepper" markdown>

**Step 1 · Cost.** Model $y = ax + b$. $J(a,b) = (3 - b)^2 + (4 - 2a - b)^2 + (3 - 3a - b)^2$.

**Now do step 2 yourself:** expand $J$ (or differentiate directly) and get the two partial derivatives.

---

**Step 2 · Derivatives.** Expanding: $J = 13a^2 + 3b^2 + 10ab - 34a - 20b + 34$ (the $a^2$ terms: $4 + 9 = 13$; $ab$ terms: $2\cdot2 + 2\cdot3 = 10$; $a$ terms: $-2\cdot2\cdot4 - 2\cdot3\cdot3 = -16 - 18 = -34$; $b$ terms: $-6 - 8 - 6 = -20$). $\frac{\partial J}{\partial a} = 26a + 10b - 34$, $\frac{\partial J}{\partial b} = 6b + 10a - 20$.

**Now do step 3 and 4 yourself:** set both to zero and solve.

---

**Steps 3 and 4 · Solve.** From the second: $6b = 20 - 10a \Rightarrow b = \frac{20 - 10a}{6}$. Into the first: $26a + 10\cdot\frac{20-10a}{6} - 34 = 0$. Multiply by 6: $156a + 200 - 100a - 204 = 0 \Rightarrow 56a = 4 \Rightarrow a = \frac{1}{14}$. Then $b = \frac{20 - 10/14}{6} = \frac{280/14 - 10/14}{6} = \frac{270}{14\cdot6} = \frac{270}{84} = \frac{45}{14}$.

**Step 5 · Check.** Closed form: $n = 3$, $\sum x = 5$, $\sum y = 10$, $\sum x^2 = 13$, $\sum xy = 0 + 8 + 9 = 17$. $a = \frac{3\cdot17 - 5\cdot10}{3\cdot13 - 25} = \frac{51-50}{39-25} = \frac1{14}$. Same. Residuals at $x = 0, 2, 3$: $3 - 3.214 = -0.214$, $4 - 3.357 = 0.643$, $3 - 3.429 = -0.429$; sum $= 0$.

!!! answer "Answer"
    $y = \frac{1}{14}x + \frac{45}{14} \approx 0.071x + 3.214$.

</div>

## Do it cold · 1 (the 2020 non-linear one, all four parts)

!!! exam "January 2020 retake · 4 · 2.5 p"
    Observed data $x[0], \ldots, x[n]$, i.i.d., generated by the model $s[n] = Ae^{\phi n}$ where the amplitude $A$ and the power term $\phi < 0$ are to be estimated.

    - (a) What kind of estimators can be used to solve this problem? Explain your reasoning and write down the formulations. [0.5]
    - (b) For the case where $\phi$ is known but $A$ is unknown, find an estimator for $A$ in closed form. [0.5]
    - (c) For both unknown, write the cost function for an estimator of $\theta = [\phi\ A]^T$. [0.5]
    - (d) Formulate the Gauss–Newton solution for the cost function in (c). Clearly show the iterative formulation. [1]

???+ solution "Solution"
    **(a)** No pdf of the noise is given, so **least squares**: $\hat\theta = \arg\min_\theta\sum_n(x[n] - Ae^{\phi n})^2$. (If the noise were known Gaussian, the MLE would give the same minimisation.)

    **(b)** $J(A) = \sum_n(x[n] - Ae^{\phi n})^2$. $\frac{dJ}{dA} = \sum_n -2e^{\phi n}(x[n] - Ae^{\phi n}) = 0 \Rightarrow \sum x[n]e^{\phi n} = A\sum e^{2\phi n}$.
    $\hat A_{LS} = \dfrac{\sum_n x[n]e^{\phi n}}{\sum_n e^{2\phi n}}$.

    **(c)** $J(\theta) = \sum_{n}(x[n] - Ae^{\phi n})^2$. Setting $\partial J/\partial\phi = \sum 2Ane^{\phi n}(Ae^{\phi n} - x[n]) = 0$ and $\partial J/\partial A = \sum 2e^{\phi n}(Ae^{\phi n} - x[n]) = 0$ gives equations that are non-linear in $\phi$ (it sits inside the exponential): no closed form.

    **(d)** Gauss–Newton linearises $s[n;\theta]$ around the current guess. With $\mathbf s(\theta) = [Ae^{\phi n}]_n$ and Jacobian $\mathbf H(\theta) = \left[\frac{\partial s[n]}{\partial\phi}\ \ \frac{\partial s[n]}{\partial A}\right]_n = \left[Ane^{\phi n}\ \ e^{\phi n}\right]_n$:

    $$\theta_{k+1} = \theta_k + \left(\mathbf H_k^T\mathbf H_k\right)^{-1}\mathbf H_k^T\left(\mathbf x - \mathbf s(\theta_k)\right),\quad \mathbf H_k = \mathbf H(\theta_k).$$

    Equivalent Newton–Raphson form used by the key: $\theta_{k+1} = \theta_k - \left[\frac{\partial^2J}{\partial\theta^2}\right]^{-1}\frac{\partial J}{\partial\theta}$ with the $2\times2$ Hessian of $J$. Iterate from a starting guess until the update is tiny.

    !!! answer "Answer"
        (a) LS. (b) $\hat A = \sum x[n]e^{\phi n}/\sum e^{2\phi n}$. (c) $J = \sum(x[n]-Ae^{\phi n})^2$, non-linear in $\phi$. (d) the update above.

## Do it cold · 2 (review deck: transform to linear)

!!! exam "Exam Q3 2022 · 2d (review deck)"
    Model $x[n] = \ln(\theta) + w[n]$. Can you avoid the non-linear optimisation and find a closed-form $\hat\theta_{LS}$?

???+ solution "Solution"
    Let $\alpha = \ln\theta$ (invertible for $\theta>0$, inverse $\theta = e^\alpha$). The model becomes $x[n] = \alpha + w[n]$: a constant in noise. $J(\alpha) = \sum(x[n] - \alpha)^2$, $\frac{dJ}{d\alpha} = -2\sum(x[n]-\alpha) = 0 \Rightarrow \hat\alpha = \frac1N\sum x[n] = \bar x$. Map back: $\hat\theta_{LS} = e^{\bar x}$. (Invariance holds for LS and ML, not for MMSE.)

    !!! answer "Answer"
        $\hat\theta_{LS} = e^{\bar x}$.

## Out of scope, in one paragraph

**Wiener filter (Jan 2019 · 4, 2.5 p).** Two-tap FIR $w_0, w_1$ chosen to minimise $E[(e[k] - \hat e[k])^2]$: solve $\mathbf R_x\mathbf w = \mathbf r_{ex}$ with $\mathbf R_x = \begin{bmatrix}r_x[0]&r_x[1]\\r_x[1]&r_x[0]\end{bmatrix}$, $\mathbf r_{ex} = [\rho_{ex}[0], \rho_{ex}[1]]^T$, $J_{min} = \sigma_e^2 - \mathbf r_{ex}^T\mathbf w$. For the AR(1) $x[k] = i[k] + \frac12x[k-1]$, $\sigma_i^2 = \frac14$: $r_x[0] = \frac{1/4}{1-1/4} = \frac13$, $r_x[1] = \frac16$; with $\rho_{ex} = [\frac23, \frac56]$ the key gives $\mathbf w = [1, 2]^T$, $J = 0$. The course dropped Wiener filtering (Jan 2022 key, 2c: "no longer part of the content"); it is not drilled here.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | Differentiating $(4 - 2a - b)^2$ as $2(4-2a-b)$ | Chain rule: $2(4-2a-b)\cdot(-2)$ for $a$, $\cdot(-1)$ for $b$. |
    | Rounding $a$ to $0.07$ before computing $b$ | Keep $\frac1{14}$; round only in the last line. |
    | "LS requires Gaussian noise" | LS requires **no** noise model; that is why it is the answer to "which estimator" when no pdf is given. |
    | "The solution vector $\hat\theta$ is orthogonal to the columns of $\mathbf H$" | The **error** $\mathbf x - \mathbf H\hat\theta$ is orthogonal; the fit $\mathbf H\hat\theta$ lies in their span. |
    | "Only Gauss–Newton works for non-linear LS" | Newton–Raphson works too (Jan 2022 2c). |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| Some non-linear LS problems can be solved analytically by separating into linear and non-linear parts or by transforming the problem into a linear one. | True | Jan 2022 2c (a), the correct option; the $\ln\theta$ example above. |
| For linear signal models, the solution vector $\hat\theta$ is orthogonal to the span of the columns of $\mathbf H$. | False | Jan 2022 2c (b): the error vector is orthogonal, not the solution. |
| Only the Gauss–Newton method can be applied to non-linear LS problems, not Newton–Raphson. | False | Jan 2022 2c (c). |
| The expression $\hat\theta = \arg\min_\theta\sum(x[n] - s[n;\theta])^2$ describes the maximum likelihood estimator. | False | Jan 2019 1b (A): that is least squares; MLE is $\arg\max p(x\mid\theta)$. |

</div>

**You can leave this page when you can:**

- [ ] fit a line to three points by hand in under five minutes, fractions kept.
- [ ] say in one sentence why LS is the estimator "when no noise pdf is given".
- [ ] write the Gauss–Newton update with its Jacobian.
- [ ] turn $\ln\theta$ or $Ae^{\phi n}$ with known $\phi$ into a linear problem.

*[least squares]: choose the parameters that minimise the sum of squared differences between data and model.
*[observation matrix]: H, the matrix whose columns multiply the unknowns in a linear model.
*[Gauss–Newton]: iterative method for non-linear least squares that linearises the model at each step.
