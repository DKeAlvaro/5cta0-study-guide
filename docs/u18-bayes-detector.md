# U18 · Bayesian detector: priors and costs set the threshold

<div class="meta"><span class="hot">Rank 16 by points, but 1 p in each of the last two exams</span><span>Jun 2026 4c, Apr 2025 4c, Nov 2022 4f+4g</span><span>50 min</span></div>

!!! need "Before this page"
    [U16](u16-lrt.md) (the LRT and how to move from the ratio to the axis), [U17](u17-pfa-pd.md) (computing $P_{FA}$, $P_M$). [M1](maths.md#m1-exponents-and-logarithms) for one $\ln$.

## The idea in plain words

Neyman–Pearson fixes $P_{FA}$ and does not care how often $H_1$ actually happens. The **Bayesian** detector does: it knows the **prior** probabilities $P_0 = P(H_0)$, $P_1 = P(H_1)$ and the **cost** of each kind of mistake, and it picks the decision rule with the smallest expected cost (the **Bayes risk**). The result is still a threshold on the likelihood ratio; only the threshold value changes. Rare $H_1$ or expensive false alarms push the threshold up; expensive misses pull it down.

!!! idea "The thing that confused me"
    $C_{ij}$ is "the cost of deciding $H_i$ when $H_j$ is true". So $C_{10}$ is a false alarm (decided 1, truth 0) and $C_{01}$ is a miss (decided 0, truth 1). Read the subscripts as (decision, truth), always in that order; the April 2025 clarification spells it out.

## A tiny example with numbers

$H_0$: $p_0(y) = e^{-y}$, $H_1$: $p_1(y) = 2e^{-2y}$, priors $P_0 = 0.4$, $P_1 = 0.6$, equal costs ($C_{10} = C_{01} = 1$, $C_{00} = C_{11} = 0$).
Threshold: $\eta = \frac{P_0(C_{10} - C_{00})}{P_1(C_{01} - C_{11})} = \frac{0.4\cdot1}{0.6\cdot1} = \frac23$.
Test: $L(y) = 2e^{-y} \gtrless \frac23 \Leftrightarrow e^{-y}\gtrless\frac13 \Leftrightarrow y \lessgtr \ln3 = 1.0986$. Decide $H_1$ when $y < \ln 3$.
Compare the $\gamma = 1$ test of U16: $y < \ln2 = 0.693$. Because $H_1$ is a priori more likely (0.6), the Bayesian rule gives it more room.

!!! question "Your turn"
    Same pdfs, but $P_0 = 0.9$, $P_1 = 0.1$, equal costs. Threshold $\eta$ and the rule on $y$?

    ???+ solution "Answer"
        $\eta = 0.9/0.1 = 9$. $2e^{-y} > 9 \Leftrightarrow e^{-y} > 4.5 \Leftrightarrow y < -\ln4.5 = -1.504$: impossible for $y\ge0$. With $H_1$ so rare, the detector never decides $H_1$ (and is right 90 % of the time).

## The formulas, every symbol named

<div class="key" markdown>

$$L(\mathbf x) = \frac{p(\mathbf x\mid H_1)}{p(\mathbf x\mid H_0)}\;\underset{H_0}{\overset{H_1}{\gtrless}}\;\eta = \frac{P_0\,(C_{10} - C_{00})}{P_1\,(C_{01} - C_{11})}\qquad\Longleftrightarrow\qquad \frac{p(H_1\mid\mathbf x)}{p(H_0\mid\mathbf x)}\;\underset{H_0}{\overset{H_1}{\gtrless}}\;\frac{C_{10} - C_{00}}{C_{01} - C_{11}}$$

</div>

| Symbol | Meaning |
|---|---|
| $P_0, P_1$ | prior probabilities of the hypotheses, $P_0 + P_1 = 1$ |
| $C_{ij}$ | cost of **deciding $H_i$ when $H_j$ is true**; $C_{10}$ false alarm, $C_{01}$ miss, $C_{00}, C_{11}$ correct decisions (usually 0) |
| $\eta$ | the Bayesian threshold on the likelihood ratio |
| $p(H_i\mid\mathbf x)$ | posterior probability of $H_i$: $p(\mathbf x\mid H_i)P_i/p(\mathbf x)$. The posterior ratio is $L(\mathbf x)P_1/P_0$ |
| Bayes risk | $R = \sum_{i,j}C_{ij}\,P(\text{decide }H_i\mid H_j)\,P_j$; with equal unit costs $R = P_0P_{FA} + P_1P_M = P_e$, the total probability of error |

**Where the threshold comes from.** Write the risk as an integral over the $H_1$ region; the integrand is $(C_{10}-C_{00})P_0p_0(\mathbf x) - (C_{01}-C_{11})P_1p_1(\mathbf x)$; put $\mathbf x$ in the $H_1$ region exactly when that integrand is negative, i.e. when $P_1(C_{01}-C_{11})p_1 > P_0(C_{10}-C_{00})p_0$. Rearranging gives the threshold.

**Special cases.** Equal costs: $\eta = P_0/P_1$ (the MAP detector, minimises $P_e$). Equal costs and equal priors: $\eta = 1$ (maximum likelihood detector). Scaling all costs by the same factor does not change $\eta$ (Apr 2025 4b).

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "assume prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$ … equal costs … when should the sensor accept $H_1$?" | $\eta = P_0/P_1 = 9$; plug into the LRT you built in the previous sub-question and solve for $x$ |
| "$C_{0,1} = 100\,C_{1,0}$, $C_{1,1} = C_{0,0} = 0$ … the posterior of $H_0$ is 5 times smaller than the posterior of $H_1$" | use the posterior form: compare $p(H_1\mid x)/p(H_0\mid x) = 5$ with $(C_{10}-C_{00})/(C_{01}-C_{11}) = 1/100$ |
| "find the threshold $\gamma''$, i.e. the value of $y$ for which $p(y\mid H_1)P_1 = p(y\mid H_0)P_0$" | set the two weighted pdfs equal and solve for $y$ (take $\ln$) |
| "determine $P_M$ and $P_{FA}$ for the Bayesian test" | [U17](u17-pfa-pd.md) with the Bayesian threshold; then optionally $P_e = P_0P_{FA} + P_1P_M$ |
| "which statement about prior probabilities … is FALSE" | check the direction: larger $P_0$ raises $\eta$, larger $P_1$ lowers it |

## Recipe

!!! recipe key "U18 · Threshold from priors and costs"
    1. **Write the four costs** and the two priors from the text. Missing costs for correct decisions are 0.
    2. **Threshold** $\eta = \dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$. If the question gives posteriors instead of likelihoods, use $\dfrac{p(H_1\mid x)}{p(H_0\mid x)} \gtrless \dfrac{C_{10}-C_{00}}{C_{01}-C_{11}}$ (the priors are already inside the posteriors).
    3. **Apply** it to the LRT of [U16](u16-lrt.md): $L(x)\gtrless\eta$ → solve for $x$. If the exam phrases it as $p_1(y)P_1 = p_0(y)P_0$, that is the same equation with $\eta$ moved across.
    4. **State the rule** in words ("accept $H_1$ when $x > \ldots$"), or "yes/no" if the question is a decision for given numbers.
    5. If asked, **errors**: $P_{FA}$, $P_M$ by U17 with this threshold; $P_e = P_0P_{FA} + P_1P_M$ (equal costs); risk $= \sum C_{ij}P(\cdot)P_j$ otherwise.

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 4c · 1 p"
    (After 4b: Rayleigh$(\sigma_0)$ under $H_0$, Rayleigh$(\sigma_1)$ under $H_1$, $\sigma_1 > \sigma_0$.) Now assume prior probabilities $P(H_0) = 0.9$, $P(H_1) = 0.1$, reflecting the fact that a transmitting device is present only 10 % of the time. Assume equal costs for false alarms and miss-detections. When should the sensor accept $H_1$?

<div class="stepper" markdown>

**Step 1 · Costs and priors.** $C_{10} = C_{01} = c$ (equal), $C_{00} = C_{11} = 0$. $P_0 = 0.9$, $P_1 = 0.1$.

**Now do step 2 yourself:** compute $\eta$.

---

**Step 2 · Threshold.** $\eta = \dfrac{0.9\cdot c}{0.1\cdot c} = 9$. The sensor needs the observation to be nine times more likely under $H_1$ than under $H_0$ before it says "device present".

**Now do step 3 yourself:** take the U16 result $L(x) = \frac{\sigma_0^2}{\sigma_1^2}\exp\!\left[\frac{x^2}{2}\left(\frac1{\sigma_0^2} - \frac1{\sigma_1^2}\right)\right]$ with $\eta = 9$ and solve for $x$.

---

**Step 3 · Apply.** $\frac{\sigma_0^2}{\sigma_1^2}\exp\!\left[\frac{x^2}{2}\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)\right] \ge 9$. Take $\ln$: $\frac{x^2}{2}\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)\ge\ln 9 + \ln\frac{\sigma_1^2}{\sigma_0^2} = \ln\!\left(\frac{9\sigma_1^2}{\sigma_0^2}\right)$. The bracket is positive, so

$$x^2 \ge \frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2 - \sigma_0^2}\ln\!\left(\frac{9\sigma_1^2}{\sigma_0^2}\right),\qquad x\ge\sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\frac{9\sigma_1^2}{\sigma_0^2}}.$$

**Step 4 · Rule.** Accept $H_1$ when the envelope exceeds that value. Compared with $\eta = 1$ the threshold grew (the $\ln$ gained a $\ln 9 = 2.197$): a rare device needs a stronger signal to be believed.

!!! answer "Answer"
    $\eta = P_0/P_1 = 9$; accept $H_1$ when $x \ge \sqrt{\dfrac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln\dfrac{9\sigma_1^2}{\sigma_0^2}}$.

</div>

## Do it cold · 1

!!! exam "April 2025 · 4c · 1 p"
    The teaching team in a MSc course uses an AI agent to detect whether assignments have been generated using genAI which is considered fraudulent. $\mathcal{H}_0$: the assignment has been generated by a student; $\mathcal{H}_1$: by genAI. The system uses Bayesian hypothesis testing and the student fails the course if the agent accepts $\mathcal{H}_1$. Assume $C_{0,1} = 100C_{1,0}$, $C_{1,1} = C_{0,0} = 0$. In addition, assume that the posterior of $\mathcal{H}_0$ is 5 times smaller than the posterior of $\mathcal{H}_1$. Should the student fail the course?

???+ solution "Solution"
    **Step 1.** $C_{01} = 100C_{10}$ (a miss, letting genAI through, costs 100 times a false accusation), $C_{00} = C_{11} = 0$.

    **Step 2 (posterior form).** Threshold on the posterior ratio: $\dfrac{C_{10}-C_{00}}{C_{01}-C_{11}} = \dfrac{C_{10}}{100C_{10}} = 0.01$.

    **Step 3.** $\dfrac{p(H_1\mid x)}{p(H_0\mid x)} = 5 \ge 0.01$. Decide $H_1$.

    **Step 4.** Yes, the student fails. (Even a posterior ratio as low as $0.01$ would do: with misses this expensive the detector is extremely trigger-happy.)

    !!! answer "Answer"
        Threshold $0.01$ on the posterior ratio; $5\ge0.01$, accept $H_1$: the student fails.

## Do it cold · 2

!!! exam "November 2022 · 4f + 4g · 0.5 + 0.5 p"
    Priors $P_0 = 0.4$, $P_1 = 0.6$; costs $C_{11} = C_{00} = 0$, $C_{01} = C_{10} = 1$; $Y = |X|$ with $p(y;H_0) = e^{-y}$, $p(y;H_1) = 2e^{-2y}$. The Bayesian test is $p(\mathbf x\mid H_1)P_1 \gtrless p(\mathbf x\mid H_0)P_0$.

    **4f** Find the threshold $\gamma''$, i.e. the value of $y$ for which $p(\mathbf{x}|\mathcal{H}_1)P_1 = p(\mathbf{x}|\mathcal{H}_0)P_0$.

    **4g** Determine the probability of miss $P_M$ and the probability of false alarm $P_{FA}$ for the Bayesian hypothesis test.

???+ solution "Solution"
    **4f.** $2e^{-2y}\cdot0.6 = e^{-y}\cdot0.4 \Rightarrow 1.2e^{-2y} = 0.4e^{-y}$. Divide by $0.4e^{-2y}$: $3 = e^{y} \Rightarrow \gamma'' = \ln 3 = 1.0986$. Side: at $y = 0$, $1.2 > 0.4$, so $H_1$ wins near zero: decide $H_1$ when $y < \ln3$.

    **4g.** $P_{FA} = \int_0^{\ln3}e^{-y}dy = [-e^{-y}]_0^{\ln3} = 1 - e^{-\ln3} = 1 - \frac13 = \frac23$. $P_M = \int_{\ln3}^\infty 2e^{-2y}dy = [-e^{-2y}]_{\ln3}^\infty = e^{-2\ln3} = 3^{-2} = \frac19$. Total error: $P_e = P_0P_{FA} + P_1P_M = 0.4\cdot\frac23 + 0.6\cdot\frac19 = \frac{4}{15} + \frac{1}{15} = \frac13$; this is what the Bayesian test minimises.

    !!! answer "Answer"
        $\gamma'' = \ln3$, decide $H_1$ for $y < \ln 3$; $P_{FA} = \frac23$, $P_M = \frac19$ ($P_e = \frac13$).

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $\eta = P_1/P_0$ | $\eta = \dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$: the **$H_0$** prior is on top. Rare $H_1$ → big $\eta$. |
    | $C_{01}$ read as "false alarm" | $C_{ij}$ = decide $i$, truth $j$: $C_{01}$ is a **miss**. |
    | Applying $\eta$ to the posterior ratio | The posterior ratio already contains $P_1/P_0$; compare it with $(C_{10}-C_{00})/(C_{01}-C_{11})$ only. |
    | Dividing $1.2e^{-2y} = 0.4e^{-y}$ wrongly | Divide both sides by $0.4e^{-2y}$: $3 = e^{y}$; or take $\ln$: $\ln1.2 - 2y = \ln0.4 - y$. |
    | $P_{FA}$ for $y > \ln3$ | The $H_1$ side here is $y < \ln 3$ (U17: test a point). |
    | "Scaling all costs by 10 changes the decision" | The ratio of cost differences is unchanged (Apr 2025 4b (b) is true). |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| When priors are equal and costs are equal, the Bayesian decision rule reduces to the maximum likelihood rule. | True | Jun 2026 4a (a): $\eta = 1$. |
| A higher prior probability $P(H_0)$ raises the Bayesian threshold $\eta$, requiring stronger evidence before $H_1$ is selected. | True | Jun 2026 4a (b): $P_0$ is in the numerator. |
| Increasing the prior probability $P(H_1)$ raises the Bayesian decision threshold $\eta$, making it harder to decide for $H_1$. | False | Jun 2026 4a (c), the FALSE option: $P_1$ is in the denominator, so $\eta$ falls. |
| In Bayesian detection the decision regions are chosen so that the Bayes risk is minimised. | True | Apr 2025 4b (a); Apr 2024 4a (a) says "maximised" and is the lie. |
| The cost assignment $C_{01} = C_{10} = 1$, $C_{11} = C_{00} = 0$ minimises the total probability of error. | True | Apr 2024 4a (b), the correct option; with $10$ instead of $1$ (Apr 2025 4b (b)) still true: risk $= 10P_e$. |

</div>

**You can leave this page when you can:**

- [ ] write $\eta$ from priors and costs and say which way it moves when $P_0$ or $C_{01}$ grows.
- [ ] read $C_{ij}$ as (decision, truth) without hesitating.
- [ ] plug $\eta$ into an LRT from U16 and solve.
- [ ] solve $p_1(y)P_1 = p_0(y)P_0$ for $y$ and then compute $P_{FA}$, $P_M$, $P_e$.

*[Bayes risk]: expected cost of the decisions, averaged over both hypotheses with their priors.
*[prior]: P(H0), P(H1): how likely each hypothesis is before any data.
*[MAP detector]: the Bayesian detector with equal costs; it minimises the probability of error.
