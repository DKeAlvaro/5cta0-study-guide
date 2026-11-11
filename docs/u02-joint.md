# U2 · Joint pdf: the constant, the marginal, the conditional, independence

<div class="meta"><span class="hot">In every exam since 2022 (0.25 to 0.5 p)</span><span>Jun 2026 1c, Apr 2025 1c, Apr 2024 1c, Nov 2022 1b</span><span>45 min</span></div>

!!! need "Before this page"
    [M5 double integrals, rectangle versus triangle](maths.md#m5-double-integrals-rectangle-versus-triangle). That page does the hard part; this one adds the vocabulary and the exam questions.

## The idea in plain words

A **joint pdf** $p_{X,Y}(x,y)$ is a height over the $(x,y)$ plane; probability is volume under it. Three things the exam asks. **The constant** $c$: the total volume must be 1. **A marginal** $p_X(x)$: squash the surface onto the $x$ axis by integrating $y$ out. **A conditional** $p_{X\mid Y}(x\mid y)$: take the slice at a fixed $y$ and rescale it so its area is 1, i.e. divide by $p_Y(y)$. **Independence**: the joint pdf is the product of the two marginals, on a rectangular region.

!!! idea "The thing that confused me"
    "Indicate the domain" is half the marks. On a triangle the range of $y$ depends on $x$. When you integrate $y$ out, the limits of that integral are the **edges of the region for that $x$**, and the result is valid only for the $x$ values where the region exists. Write "for $0\le x\le1$" after every pdf.

## A tiny example with numbers

$p_{X,Y}(x,y) = c$ on the triangle $0\le y\le x\le 1$ (zero outside). Area of the triangle $= \frac12$, so volume $= c\cdot\frac12 = 1 \Rightarrow c = 2$.
Marginal of $X$: for fixed $x$, $y$ runs $0\to x$: $p_X(x) = \int_0^x2\,dy = 2x$, $0\le x\le1$.
Marginal of $Y$: for fixed $y$, $x$ runs $y\to1$: $p_Y(y) = \int_y^12\,dx = 2(1-y)$, $0\le y\le1$.
Independent? $p_Xp_Y = 4x(1-y) \ne 2$. No (also: the region is not a rectangle, which already rules it out).

!!! question "Your turn"
    $p_{X,Y} = 2$ on $0\le y\le x\le1$. Compute $p_{Y\mid X}(y\mid x) = p_{X,Y}/p_X(x)$ and its domain.

    ???+ solution "Answer"
        $\frac{2}{2x} = \frac1x$ for $0\le y\le x$ (and a given $x\in(0,1]$). It is uniform on $[0,x]$: given $X = x$, $Y$ is equally likely anywhere below $x$.

## The formulas, every symbol named

<div class="key" markdown>

$$\iint_{\text{region}}p_{X,Y}(x,y)\,dx\,dy = 1,\qquad p_X(x) = \int p_{X,Y}(x,y)\,dy,\qquad p_{X\mid Y}(x\mid y) = \frac{p_{X,Y}(x,y)}{p_Y(y)},\qquad \text{independent}\iff p_{X,Y} = p_X(x)\,p_Y(y)$$

</div>

| Symbol | Meaning |
|---|---|
| region | where the joint pdf is nonzero: a square ($0\le x\le1$, $0\le y\le1$) or a triangle ($x,y\ge0$, $x+y<1$; or $0\le y\le x\le1$) |
| $p_X(x)$ | marginal pdf of $X$: integrate the **other** variable out, over its range **for that $x$** |
| $p_{X\mid Y}(x\mid y)$ | conditional pdf: joint divided by the marginal of the **given** variable; a pdf in $x$ for fixed $y$ |
| discrete version | $p_X(x) = \sum_y p_{X,Y}(x,y)$: add the row (Nov 2022 1b) |

**Quick independence test.** Two conditions, both needed: the region is a rectangle with sides parallel to the axes, and the formula factors as $f(x)g(y)$. $6x^2y$ on the unit square: yes. $cx + 1$ on a triangle: no (region). $2$ on $0\le y\le x\le1$: no (region).

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "find the constant $c$" | double integral over the region $= 1$; [M5](maths.md#m5-double-integrals-rectangle-versus-triangle) four moves for the limits |
| "find the marginal PDF $p_X(x)$ and indicate its domain" | integrate $y$ out with limits for fixed $x$; state the $x$ range |
| "find … the conditional PDF $p_{X\mid Y}(x\mid y)$ … correctly indicate the domain" | joint over $p_Y(y)$; domain: the $x$ range for that fixed $y$, plus the $y$ range |
| "determine whether $X$ and $Y$ are independent, and briefly justify" | rectangle + factorisation, or compare $p_{X,Y}$ with $p_Xp_Y$ |
| "note: for the conditions … to be satisfied, $x < 1 - y$ and $y<1$" | the exam is handing you the inner and outer limits |
| "what is the marginal PMF of $X$?" with a table | add across each row |

## Recipe

!!! recipe key "U2 · Four moves plus a division"
    1. **Draw the region** (a square or a triangle) and write the inequalities.
    2. **Constant**: pick the order, freeze the outer letter, write the inner limits in that letter, outer limits as numbers; integrate inner, then outer; set $= 1$, solve for $c$.
    3. **Marginal of $X$**: integrate the joint over $y$ with the limits for fixed $x$; attach the $x$ range. (Same for $Y$ with the roles swapped.)
    4. **Conditional**: divide the joint by the marginal of the given variable; attach both ranges.
    5. **Independence**: rectangle and factorisation, or check $p_{X,Y} = p_Xp_Y$ after step 3.

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 1c · 0.5 p"
    Let $X$ and $Y$ be jointly continuous random variables with joint PDF $p_{X,Y}(x, y) = 6x^2y$ for $0 \leq x \leq 1$ and $0 \leq y \leq 1$, $0$ otherwise. **Please provide only the final answer.** 1. Find the marginal PDF $p_X(x)$ and indicate its domain. [0.25] 2. Determine whether $X$ and $Y$ are independent, and briefly justify why. [0.25]

<div class="stepper" markdown>

**Step 1 · Region.** The unit square: $x$ from 0 to 1, $y$ from 0 to 1, independently. Rectangle: limits are plain numbers.

**Now do step 3 yourself:** $p_X(x) = \int_0^1 6x^2y\,dy$. Treat $x$ as a constant.

---

**Step 3 · Marginal.** $\int_0^1 6x^2y\,dy = 6x^2\int_0^1y\,dy = 6x^2\left[\frac{y^2}{2}\right]_0^1 = 6x^2\cdot\frac12 = 3x^2$, for $0\le x\le1$. (Check: $\int_0^13x^2dx = [x^3]_0^1 = 1$. ✓) By symmetry of roles, $p_Y(y) = \int_0^16x^2y\,dx = 6y\cdot\frac13 = 2y$, $0\le y\le1$.

**Now do step 5 yourself:** is $p_X(x)p_Y(y)$ equal to the joint?

---

**Step 5 · Independence.** $p_X(x)p_Y(y) = 3x^2\cdot2y = 6x^2y = p_{X,Y}(x,y)$ on the whole square. **Independent.** Shortcut justification: rectangular region and the formula factors as $(x^2)(y)$ times a constant.

!!! answer "Answer"
    1. $p_X(x) = 3x^2$ for $0\le x\le1$ (0 elsewhere). 2. Independent: $p_{X,Y} = p_X(x)p_Y(y) = 3x^2\cdot2y$ on a rectangular domain.

</div>

## Do it cold · 1 (the constant on a triangle)

!!! exam "April 2025 · 1c · 0.3 p"
    $p_{X,Y}(x,y) = cx + 1$ for $x,y\ge0$, $x + y < 1$; $0$ otherwise. Note: $x < 1 - y$ and $y < 1$, or equivalently $y < 1-x$ and $x < 1$. Find the constant $c$.

???+ solution "Solution"
    Order: inner $dx$, outer $dy$. Freeze $y$; $x$ runs $0\to1-y$; $y$ runs $0\to1$.
    Inner: $\int_0^{1-y}(cx+1)dx = \left[\frac{cx^2}{2} + x\right]_0^{1-y} = \frac{c(1-y)^2}{2} + (1-y)$.
    Outer: $\int_0^1\left[\frac{c(1-y)^2}{2} + (1-y)\right]dy$. With $u = 1-y$ ($du = -dy$, limits flip, which cancels the sign): $\int_0^1\left[\frac{cu^2}{2} + u\right]du = \left[\frac{cu^3}{6} + \frac{u^2}{2}\right]_0^1 = \frac c6 + \frac12$.
    Set $= 1$: $\frac c6 = \frac12 \Rightarrow c = 3$.

    !!! answer "Answer"
        $c = 3$.

## Do it cold · 2 (marginal and conditional with domains)

!!! exam "April 2024 · 1c · 0.3 p"
    $p_{X,Y}(x,y) = 2$ for $0\le y\le x\le1$, $0$ otherwise. Find the marginal PDF of $Y$, $p_Y(y)$, and the conditional PDF $p_{X\mid Y}(x\mid y)$. For both PDFs make sure to correctly indicate their domain.

???+ solution "Solution"
    **Marginal of $Y$.** Fix $y$; $x$ runs from $y$ to $1$. $p_Y(y) = \int_y^12\,dx = [2x]_y^1 = 2 - 2y = 2(1-y)$, for $0\le y\le1$. (Check: $\int_0^12(1-y)dy = [2y - y^2]_0^1 = 1$. ✓)

    **Conditional.** $p_{X\mid Y}(x\mid y) = \dfrac{p_{X,Y}(x,y)}{p_Y(y)} = \dfrac{2}{2(1-y)} = \dfrac{1}{1-y}$, for $y\le x\le1$, with $0\le y<1$. Given $Y = y$, $X$ is uniform on $[y, 1]$, an interval of length $1-y$: that is why the height is $1/(1-y)$.

    !!! answer "Answer"
        $p_Y(y) = 2(1-y)$, $0\le y\le1$; $p_{X\mid Y}(x\mid y) = \frac{1}{1-y}$, $y\le x\le1$.

## Do it cold · 3 (discrete table)

!!! exam "November 2022 · 1b · 0.25 p"
    Joint PMF: row $X=0$: $\frac16, \frac14, \frac18$ for $Y = 0, 1, 2$; row $X=1$: $\frac18, \frac16, \frac16$. What is the marginal PMF of $X$? (a) $\frac{7}{24}, \frac{5}{24}$ (b) $\frac{13}{24}, \frac{11}{24}$ (c) $\frac{13}{24}, \frac5{24}, \frac{11}{24}$ (d) $\frac7{24}, \frac5{12}, \frac7{24}$

???+ solution "Solution"
    Add each row. $p_X(0) = \frac16 + \frac14 + \frac18 = \frac{4 + 6 + 3}{24} = \frac{13}{24}$. $p_X(1) = \frac18 + \frac16 + \frac16 = \frac{3 + 4 + 4}{24} = \frac{11}{24}$. Sum $= 1$. ✓ **(b)**. (c) and (d) have three values, but $X$ takes only two; (a) does not sum to 1.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $p_Y(y) = \int_0^12\,dx = 2$ | On the triangle $0\le y\le x\le1$ the $x$ limits are $y$ to $1$: $2(1-y)$. |
    | $p_X(x) = 3x^2$ with no domain | "$3x^2$ for $0\le x\le1$, 0 elsewhere." The domain is graded. |
    | Conditional $= p_{X,Y}/p_X$ when $Y$ is the given | Divide by the marginal of the **given** variable: $p_Y(y)$. |
    | "Independent because $6x^2y$ factors" (without checking the region) | Also needs a rectangular region; on a triangle, never independent. |
    | $\int_0^{1-y}(cx+1)dx = c(1-y) + 1$ | Antiderivative of $cx$ is $cx^2/2$: $\frac{c(1-y)^2}{2} + (1-y)$. |
    | Marginal PMF with three values for a two-valued $X$ | One number per value of $X$: add across the row. |

## True or false (fresh wording)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| The marginal pdf of $X$ is obtained by integrating the joint pdf over all values of $Y$ allowed for that $x$. | True | Definition. |
| If the support of a joint pdf is a triangle, $X$ and $Y$ can still be independent provided the formula factors. | False | Independence forces a product support (a rectangle). |
| $p_{X\mid Y}(x\mid y)$ integrates to 1 over $x$ for every fixed $y$. | True | It is the rescaled slice. |
| For $p_{X,Y} = 2$ on $0\le y\le x\le1$, $X$ tends to be larger than $Y$. | True | $Y\le X$ on the whole support; $E[X] = 2/3$, $E[Y] = 1/3$. |

</div>

**You can leave this page when you can:**

- [ ] draw the region from the inequalities and write both orders of limits.
- [ ] find $c$ on a triangle with the four moves.
- [ ] write a marginal with its domain and a conditional with both domains.
- [ ] decide independence in two checks.

*[joint pdf]: a density over two variables; probability is its integral over a region of the plane.
*[marginal]: the pdf of one variable alone, obtained by integrating the other out.
*[conditional pdf]: the pdf of one variable given a fixed value of the other: joint divided by the marginal of the given one.
*[support]: the region where a pdf is nonzero.
