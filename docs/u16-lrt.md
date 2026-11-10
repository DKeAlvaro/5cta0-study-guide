# U16 · The likelihood ratio test: from two pdfs to "decide H1 when x > γ′"

<div class="meta"><span class="hot">Rank 5 · 5.25 points over 6 sittings</span><span>1 p in Jun 2026</span><span>60 min</span></div>

!!! need "Before this page"
    [M1 exponents and ln](maths.md#m1-exponents-and-logarithms) (the $e^a/e^b$ rule and taking $\ln$ of an inequality), [M8 inequalities](maths.md#m8-argmax-set-the-derivative-to-zero-quadratics). Pairs with [U17](u17-pfa-pd.md): this page finds the threshold, U17 uses it.

## The idea in plain words

You have one number $x$ and two candidate stories, $H_0$ and $H_1$. Ask: "how many times more likely is $x$ under $H_1$ than under $H_0$?". That ratio is the **likelihood ratio** $L(x)$. If it is bigger than some bar $\gamma$ you say $H_1$. All the algebra in this unit is just rewriting "$L(x) > \gamma$" as "$x > \text{some number}$" so you can apply it by looking at $x$.

!!! idea "The thing that confused me"
    Two different thresholds carry similar names. $\gamma$ (also $\lambda$ or $\eta$) is the bar on the **ratio**, usually given. $\gamma'$ (or $x_{th}$, $\lambda'$) is the bar on the **observation axis**, which you compute. The exam asks for the second one.

## A tiny example with numbers

$H_0$: $p_0(x) = e^{-x}$, $H_1$: $p_1(x) = 2e^{-2x}$, $x\ge0$, bar $\gamma = 1$.

$L(x) = \dfrac{2e^{-2x}}{e^{-x}} = 2e^{-2x-(-x)} = 2e^{-x}$ (rule $e^a/e^b = e^{a-b}$).
$L(x) > 1 \Leftrightarrow 2e^{-x} > 1 \Leftrightarrow e^{-x} > \tfrac12 \Leftrightarrow -x > \ln\tfrac12 = -0.6931 \Leftrightarrow x < 0.6931$.
Read the last step carefully: I multiplied by $-1$, so $>$ became $<$. **Decide $H_1$ when $x < 0.693$.**

!!! question "Your turn"
    Same pdfs, but $\gamma = 4$. For which $x$ do we decide $H_1$?

    ???+ solution "Answer"
        $2e^{-x} > 4 \Leftrightarrow e^{-x} > 2 \Leftrightarrow -x > \ln 2 = 0.693 \Leftrightarrow x < -0.693$. No $x\ge0$ satisfies it: with such a high bar we never decide $H_1$. (That is allowed; it just means $P_D = P_{FA} = 0$.)

## The formula, every symbol named

<div class="key" markdown>

$$L(\mathbf x) = \frac{p(\mathbf x; H_1)}{p(\mathbf x; H_0)} \;\underset{H_0}{\overset{H_1}{\gtrless}}\; \gamma$$

</div>

| Symbol | Meaning |
|---|---|
| $\mathbf x$ | the observation: one number $x$, or a vector $x_0,\ldots,x_{N-1}$ |
| $p(\mathbf x;H_i)$ | the pdf of the data if $H_i$ is the truth. For $N$ independent samples it is the **product** $\prod_{n}p(x_n;H_i)$ |
| $L$ | likelihood ratio, $H_1$ on top |
| $\gtrless$ with labels | "if the left side is bigger, decide the top label ($H_1$); if smaller, the bottom one" |
| $\gamma$ | the bar on the ratio. Neyman–Pearson picks it to hit a target $P_{FA}$; Bayes sets $\gamma = \frac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$ ([U18](u18-bayes-detector.md)); $\gamma=1$ is "pick the more likely story" |

**Why it is the right test.** Neyman–Pearson theorem: for a fixed $P_{FA}$, thresholding $L$ gives the largest possible $P_D$. You never have to prove it; you have to apply it.

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "construct the likelihood-ratio test for a threshold $\eta$" | write $L(x)$, simplify, take $\ln$, isolate $x$ (or $x^2$, or $\sum x_n^2$), state "decide $H_1$ when …" |
| "show that the LRT takes the form $\sum \lvert x_n\rvert \gtrless \gamma'$ and determine $\gamma'$" | same recipe for $N$ samples; $\gamma'$ will contain $N$ and $\ln\gamma$ |
| "what is the value of $x$ for which $H_1$ should be accepted" | the answer is a *range* ($x \ge$ number), not a single number |
| "derive the log-likelihood ratio test" | stop after taking $\ln$ and collecting the data term; no numbers |
| "pay special attention to the inequality" | you will divide by a negative number or the $H_1$ region is on the left |
| "discuss how the separation between $\sigma_0$ and $\sigma_1$ affects detection" | closer parameters → the two pdfs overlap more → for any threshold $P_D$ drops toward $P_{FA}$, ROC moves toward the diagonal |

## Recipe

!!! recipe key "U16 · From the ratio to the axis"
    1. **Write the ratio** $L = p(\cdot;H_1)/p(\cdot;H_0)$ with $H_1$ on top. For $N$ samples write each side as a product; the product of exponentials is an exponential of the sum ($\prod e^{a_n} = e^{\sum a_n}$) and constants come out as a power ($\prod_{n=1}^N c = c^N$).
    2. **Cancel what cancels.** Same factor top and bottom (like the $x$ in the Rayleigh pdf, or $k_1$): gone. Exponentials: $e^a/e^b = e^{a-b}$. Powers: $x^a/x^b = x^{a-b}$.
    3. **Write the test** $L \gtrless \gamma$ and **take $\ln$** of both sides. Direction unchanged.
    4. **Isolate the data term** ($x$, $x^2$, $|x|$, $\sum x_n^2$, $\sum|x_n|$): move constants to the right. Every time you multiply or divide by a negative number, flip the inequality **and swap the labels**.
    5. **Finish the inversion.** If you have $x^2 > c$ with $x > 0$, then $x > \sqrt c$. If $e^{x} > c$, then $x > \ln c$. If $-x > c$, then $x < -c$.
    6. **Say it in words**: "decide $H_1$ when $x > \gamma'$ where $\gamma' = \ldots$". Plug numbers if the question gives them.
    7. **Check with a test point**: pick an $x$ far on the $H_1$ side and verify $p_1(x) > \gamma\,p_0(x)$.

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 4b · 1 p"
    A wireless sensor detects the presence of a transmitting device by measuring the received signal envelope $X$ (in mV). Under normal operating conditions the envelope follows a Rayleigh distribution due to multipath fading. Two hypotheses are proposed:

    1. Under $H_0$ (no device present), $X \sim \text{Rayleigh}(\sigma_0)$.
    2. Under $H_1$ (device present), $X \sim \text{Rayleigh}(\sigma_1)$,

    with $\sigma_1 > \sigma_0 > 0$, both known. The Rayleigh pdf with scale parameter $\sigma$ is $p(x \mid \sigma) = \frac{x}{\sigma^2} \exp\left(-\frac{x^2}{2\sigma^2}\right)$, $x \geq 0$.

    - Construct the likelihood-ratio test for a threshold $\eta$.
    - Discuss how the separation between $\sigma_0$ and $\sigma_1$ affects detection performance.

<div class="stepper" markdown>

**Step 1 · Write the ratio.** $L(x) = \dfrac{\frac{x}{\sigma_1^2}\exp\!\left(-\frac{x^2}{2\sigma_1^2}\right)}{\frac{x}{\sigma_0^2}\exp\!\left(-\frac{x^2}{2\sigma_0^2}\right)}$.

**Now do step 2 yourself:** cancel the common factor and merge the two exponentials into one, using $e^a/e^b = e^{a-b}$.

---

**Step 2 · Cancel.** The $x$ cancels. $\frac{1/\sigma_1^2}{1/\sigma_0^2} = \frac{\sigma_0^2}{\sigma_1^2}$. Exponent: $-\frac{x^2}{2\sigma_1^2} - \left(-\frac{x^2}{2\sigma_0^2}\right) = \frac{x^2}{2}\left(\frac{1}{\sigma_0^2} - \frac{1}{\sigma_1^2}\right)$. So

$$L(x) = \frac{\sigma_0^2}{\sigma_1^2}\exp\!\left[\frac{x^2}{2}\left(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\right)\right].$$

Note the bracket is **positive** because $\sigma_1 > \sigma_0$ means $1/\sigma_0^2 > 1/\sigma_1^2$. So $L$ grows with $x$: large envelopes point to $H_1$.

**Now do step 3 yourself:** write $L(x)\gtrless\eta$ and take $\ln$ of both sides.

---

**Step 3 · Take ln.** $\ln L = \ln\frac{\sigma_0^2}{\sigma_1^2} + \frac{x^2}{2}\left(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\right) \;\underset{H_0}{\overset{H_1}{\gtrless}}\; \ln\eta$.

**Now do step 4 yourself:** isolate $x^2$. Is the number you divide by positive or negative?

---

**Step 4 · Isolate.** Move the constant: $\frac{x^2}{2}\left(\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}\right) \gtrless \ln\eta - \ln\frac{\sigma_0^2}{\sigma_1^2} = \ln\eta + \ln\frac{\sigma_1^2}{\sigma_0^2} = \ln\!\left(\eta\frac{\sigma_1^2}{\sigma_0^2}\right)$. Divide by the positive bracket (no flip) and multiply by 2:

$$x^2 \;\underset{H_0}{\overset{H_1}{\gtrless}}\; \frac{2\ln\!\left(\eta\,\sigma_1^2/\sigma_0^2\right)}{\frac{1}{\sigma_0^2}-\frac{1}{\sigma_1^2}} = \frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\!\left(\eta\frac{\sigma_1^2}{\sigma_0^2}\right).$$

(The last form: multiply top and bottom by $\sigma_0^2\sigma_1^2$.)

**Now do step 5 yourself:** $x \ge 0$, so take the square root and write the final sentence.

---

**Step 5 · Finish.** Decide $H_1$ when

$$x > \gamma' = \sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\!\left(\eta\frac{\sigma_1^2}{\sigma_0^2}\right)}.$$

**Step 6 · Separation discussion.** If $\sigma_1 \to \sigma_0$ the two Rayleigh curves become the same curve: the denominator $\sigma_1^2 - \sigma_0^2 \to 0$, $\gamma'$ blows up, and for any threshold $P_D \approx P_{FA}$ (ROC on the diagonal: the test is a coin flip). If $\sigma_1 \gg \sigma_0$ the $H_1$ curve is spread far to the right of the $H_0$ curve, a threshold between them gives $P_D$ near 1 with $P_{FA}$ near 0 (ROC hugs the top-left corner). Detection performance improves monotonically with the separation $\sigma_1/\sigma_0$.

!!! answer "Answer"
    $L(x) = \frac{\sigma_0^2}{\sigma_1^2}\exp\!\left[\frac{x^2}{2}\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)\right] \gtrless \eta$; equivalently decide $H_1$ when $x > \sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln(\eta\sigma_1^2/\sigma_0^2)}$. Larger separation → better ROC; equal scales → useless test.

</div>

## Do it cold · 1

!!! exam "April 2025 · 4a · 0.5 p"
    You are conducting a likelihood ratio test using a single datapoint $x$, $0 < x < 1$ whereby $p(x) = k_1 \theta x^{k_2 \theta - 1}$. Two hypothesis can be distinguished: $\mathcal{H}_0 : \theta = 3$, $\mathcal{H}_1 : \theta = 6$. If $\lambda = 0.2$, $k_1 = 1$, and $k_2 = 2$, what is the value for $x$ for which $\mathcal{H}_1$ should be accepted?

???+ solution "Solution"
    **Step 1.** Under $H_1$: $p = k_1\cdot6\cdot x^{2\cdot6-1} = 6k_1x^{11}$. Under $H_0$: $p = 3k_1x^{5}$. $L(x) = \dfrac{6k_1x^{11}}{3k_1x^{5}}$.

    **Step 2.** $k_1$ cancels; $6/3 = 2$; $x^{11}/x^5 = x^{6}$. $L(x) = 2x^6$.

    **Step 3.** $2x^6 \ge 0.2$.

    **Step 4.** Divide by 2: $x^6 \ge 0.1$.

    **Step 5.** Sixth root (both sides positive, direction kept): $x \ge 0.1^{1/6}$. $0.1^{1/6} = e^{\ln(0.1)/6} = e^{-2.3026/6} = e^{-0.3838} = 0.6813$.

    **Step 7 check.** $x = 0.9$: $L = 2\cdot0.9^6 = 2\cdot0.531 = 1.06 > 0.2$. Yes, $H_1$.

    !!! answer "Answer"
        Accept $H_1$ for $x \ge 0.1^{1/6} \approx 0.68$ (a range, as the official clarification says).

## Do it cold · 2

!!! exam "November 2022 · 4c · 0.5 p"
    Under the two hypotheses, a single observation $x$ admits a zero mean Laplacian distribution, but with different variances which are given as $\mathcal{H}_0 : p(x; \mathcal{H}_0) = \frac{1}{2}e^{-|x|}$ and $\mathcal{H}_1 : p(x; \mathcal{H}_1) = e^{-2|x|}$. Assume that each observation $x_n$ of the observation vector $\mathbf{x}$ is independent and identically distributed. Show that the likelihood ratio test for deciding between these two hypotheses takes the form $\sum_{n=0}^{N-1} |x_n| \underset{\mathcal{H}_1}{\overset{\mathcal{H}_0}{\gtrless}} \gamma'$. Additionally, determine the threshold $\gamma'$. **Hint:** Pay special attention to the inequality in the decision criteria.

???+ solution "Solution"
    **Step 1.** $L(\mathbf x) = \dfrac{\prod_{n=0}^{N-1}e^{-2|x_n|}}{\prod_{n=0}^{N-1}\frac12 e^{-|x_n|}}$. Products: top $= e^{-2\sum|x_n|}$; bottom $= \left(\frac12\right)^N e^{-\sum|x_n|}$.

    **Step 2.** $1/(1/2)^N = 2^N$. Exponent: $-2\sum|x_n| + \sum|x_n| = -\sum|x_n|$. $L = 2^N e^{-\sum|x_n|}$.

    **Step 3.** $\ln L = N\ln2 - \sum|x_n| \;\underset{H_0}{\overset{H_1}{\gtrless}}\; \ln\gamma$.

    **Step 4.** $-\sum|x_n| \gtrless \ln\gamma - N\ln 2$. Multiply by $-1$: **flip and swap labels**: $\sum|x_n| \;\underset{H_1}{\overset{H_0}{\gtrless}}\; N\ln2 - \ln\gamma$.

    **Step 6.** $\gamma' = N\ln 2 - \ln\gamma$. A *small* sum of magnitudes points to $H_1$ (its pdf is narrower). That is the hint.

    !!! answer "Answer"
        $\sum|x_n| \underset{H_1}{\overset{H_0}{\gtrless}} \gamma'$ with $\gamma' = N\ln2 - \ln\gamma$.

## Do it cold · 3

!!! exam "November 2019 · 4c · 1 p (also October 2021 · 4b · 1 p)"
    $\mathcal{H}_0 : x[n] \sim \mathcal{N}(0, \sigma_0^2)$, $\mathcal{H}_1 : x[n] \sim \mathcal{N}(0, \sigma_1^2)$, $\sigma_1 > \sigma_0$, $N$ i.i.d. samples. Derive the log-likelihood ratio test that uses the observed data $x[0], \ldots, x[n]$, starting from the likelihood ratio formulation $\mathcal{L}(x) = \frac{p(\mathbf{x}; \mathcal{H}_1)}{p(\mathbf{x}; \mathcal{H}_0)} > \gamma$.

???+ solution "Solution"
    **Step 1.** $p(\mathbf x;H_i) = \prod_n\frac{1}{\sqrt{2\pi\sigma_i^2}}e^{-x[n]^2/(2\sigma_i^2)} = (2\pi\sigma_i^2)^{-N/2}\exp\!\left(-\frac{\sum_n x[n]^2}{2\sigma_i^2}\right)$.

    **Step 2.** Ratio of the constants: $\left(\frac{\sigma_0^2}{\sigma_1^2}\right)^{N/2} = \left(\frac{\sigma_0}{\sigma_1}\right)^N$. Exponent: $-\frac{\sum x^2}{2\sigma_1^2} + \frac{\sum x^2}{2\sigma_0^2}$.

    **Step 3.** $\ln\mathcal L = N\ln\frac{\sigma_0}{\sigma_1} - \frac{\sum x[n]^2}{2\sigma_1^2} + \frac{\sum x[n]^2}{2\sigma_0^2} > \ln\gamma$. That is the log-likelihood ratio test the exam asks for.

    **Step 4 (one step further, for full clarity).** $\sum x[n]^2\left(\frac{1}{2\sigma_0^2}-\frac{1}{2\sigma_1^2}\right) > \ln\gamma + N\ln\frac{\sigma_1}{\sigma_0}$. The bracket is positive, so $\sum_n x[n]^2 > \dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\left(\ln\gamma + N\ln\frac{\sigma_1}{\sigma_0}\right)$: large energy → $H_1$.

    !!! answer "Answer"
        $\ln\mathcal L(\mathbf x) = N\ln\frac{\sigma_0}{\sigma_1} - \frac{\sum x[n]^2}{2\sigma_1^2} + \frac{\sum x[n]^2}{2\sigma_0^2} > \ln\gamma$.

## Do it cold · 4 (from the review deck, resit Q1 2023 4d)

!!! exam "Resit Q1 2023 · 4d (review deck)"
    $p(x;\mathcal H_0) = xe^{-x^2/2}$, $p(x;\mathcal H_1) = \frac x4 e^{-x^2/8}$, $x>0$. Show that the LRT can be written as $x \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}}\lambda'$, find $\lambda'$ and its value for $\lambda = 1$.

???+ solution "Solution"
    $L = \dfrac{\frac x4 e^{-x^2/8}}{xe^{-x^2/2}} = \frac14 e^{-x^2/8 + x^2/2} = \frac14 e^{3x^2/8}$ (since $-\frac18 + \frac12 = \frac{-1+4}{8} = \frac38$). $\frac14 e^{3x^2/8} > \lambda \Rightarrow \frac{3x^2}{8} > \ln(4\lambda) \Rightarrow x^2 > \frac83\ln(4\lambda) \Rightarrow x > \lambda' = \sqrt{\frac83\ln(4\lambda)}$. For $\lambda = 1$: $\ln 4 = 1.3863$, $\frac83\cdot1.3863 = 3.6968$, $\sqrt{3.6968} = 1.923$.

    !!! answer "Answer"
        $\lambda' = \sqrt{\tfrac83\ln(4\lambda)} \approx 1.92$ for $\lambda=1$ (valid for $\lambda > 1/4$; below that we always decide $H_1$).

## Definitions question (January 2019 · 3a · 1.25 p)

!!! exam "January 2019 · 3a"
    Formulate the likelihood ratio test, probability of false alarm and probability of detection. Represent the distributions under $\mathcal{H}_0$ and $\mathcal{H}_1$ as $p(\mathbf{x}; \mathcal{H}_0)$ and $p(\mathbf{x}; \mathcal{H}_1)$.

???+ solution "Solution"
    $\mathcal L(\mathbf x) = \dfrac{p(\mathbf x;\mathcal H_1)}{p(\mathbf x;\mathcal H_0)} \underset{\mathcal H_0}{\overset{\mathcal H_1}{\gtrless}} \gamma$. $P_{fa} = \int_{\{\mathbf x:\,\mathcal L(\mathbf x)>\gamma\}}p(\mathbf x;\mathcal H_0)\,d\mathbf x$. $P_d = \int_{\{\mathbf x:\,\mathcal L(\mathbf x)>\gamma\}}p(\mathbf x;\mathcal H_1)\,d\mathbf x$. In words: integrate the $H_0$ pdf (for $P_{fa}$) or the $H_1$ pdf (for $P_d$) over the region where you decide $H_1$.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $L = p(x;H_0)/p(x;H_1)$ | $H_1$ on top. (The 2019 key once wrote it the other way; every exam since 2021 uses $H_1$ on top.) |
    | Dividing by $-1$ and keeping $>$ | $-\sum\lvert x_n\rvert > c \Rightarrow \sum\lvert x_n\rvert < -c$: flip, and swap the $H_0/H_1$ labels. |
    | Dropping $k_1$ or the $x$ factor without saying so | Write "cancels (same factor top and bottom)". It is the step that earns the mark. |
    | Answering "$x = 0.68$" | The answer is "$x \ge 0.68$": a region. |
    | Treating $(1/\sigma_0^2 - 1/\sigma_1^2)$ as negative because $\sigma_1 > \sigma_0$ | Larger $\sigma$ means **smaller** $1/\sigma^2$; the bracket is positive. Write the sign check. |
    | Forgetting $N$ in the constant for $N$ samples | $\prod_{n=1}^N c = c^N$, so $\ln$ gives $N\ln c$. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| With the Neyman–Pearson test, for a fixed probability of false alarm, the probability of detection is maximised. | True | Nov 2022 4b (b), Apr 2024 4a option c says "minimised", which is the swapped lie. |
| The Neyman–Pearson test partitions the observation space so that $P_{FA}$ equals $P_D$. | False | Nov 2022 4b (d): that would be the useless diagonal of the ROC. |
| The matched filter can be implemented as a FIR filter with impulse response $h[n] = s[n]$. | False | Jan 2022 4a: it is the time-reversed signal, $h[n] = s[N-1-n]$. |
| The signal-to-noise ratio at the output of the matched filter is maximised. | True | Jan 2022 4a (a). |
| The matched filter can only be applied for uncorrelated noise samples. | False | Jan 2022 4a: with correlated noise, prewhiten first (generalised matched filter). |

</div>

**You can leave this page when you can:**

- [ ] write $L$ for one sample and for $N$ i.i.d. samples (products → sums in the exponent, constants → $c^N$).
- [ ] take $\ln$ of an inequality and isolate $x$, $x^2$, $|x|$ or $\sum x_n^2$, flipping when you divide by a negative.
- [ ] state the final test as a sentence with "decide $H_1$ when".
- [ ] explain in two lines what happens to detection when $\sigma_1 \to \sigma_0$.

*[likelihood ratio]: p(x;H1)/p(x;H0): how many times more likely the data is under H1 than under H0.
*[Neyman–Pearson]: the test that maximises P_D for a fixed P_FA; it is always a threshold on the likelihood ratio.
*[i.i.d.]: independent and identically distributed: each sample has the same pdf and does not depend on the others, so the joint pdf is the product.
