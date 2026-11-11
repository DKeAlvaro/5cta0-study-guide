# U19 · Detection theory: the multiple-choice facts

<div class="meta"><span class="hot">0.5 p in each of the last three exams</span><span>pure lookup</span><span>30 min</span></div>

!!! need "Before this page"
    [U16](u16-lrt.md), [U17](u17-pfa-pd.md), [U18](u18-bayes-detector.md). This page is the drill.

## The facts (memorise these 12 sentences)

**Errors and names**

1. Decide $H_1$ when $H_0$ is true: **false alarm**, false positive, type I error, probability $P_{FA}$.
2. Decide $H_0$ when $H_1$ is true: **miss**, false negative, type II error, probability $P_M = 1 - P_D$.
3. Decide $H_1$ when $H_1$ is true: **detection**, true positive, $P_D$. Decide $H_0$ when $H_0$ is true: true negative, $1 - P_{FA}$.

**Neyman–Pearson**

4. For a **fixed $P_{FA}$**, the NP test **maximises $P_D$**. (Swaps to watch: "minimises $P_D$", "fixed $P_D$ minimises $P_{FA}$", "$P_{FA} = P_D$".)
5. It is always a threshold on the likelihood ratio $p(\mathbf x;H_1)/p(\mathbf x;H_0)$.
6. The ROC plots $P_D$ (vertical) against $P_{FA}$ (horizontal); it lies above the diagonal; it passes through $(0,0)$ and $(1,1)$; more separation between the hypotheses pushes it toward the top-left corner.

**Bayesian**

7. The Bayesian detector minimises the **Bayes risk** (never "maximises").
8. Threshold $\eta = \frac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$. Equal costs → $\eta = P_0/P_1$ → minimises $P_e$. Equal costs and priors → $\eta = 1$ → ML rule.
9. Larger $P_0$ or larger false-alarm cost → larger $\eta$ (harder to say $H_1$). Larger $P_1$ or larger miss cost → smaller $\eta$.
10. Multiplying all costs by the same factor changes nothing.

**Matched filter and t-statistic**

11. The matched filter maximises the output **SNR**; its impulse response is the **time-reversed** signal $h[n] = s[N-1-n]$; with correlated noise, prewhiten first (generalised matched filter). It is not restricted to uncorrelated noise.
12. $t = \frac{\hat\mu - \mu}{\hat\sigma/\sqrt N}$: more samples make a deviation more significant; a larger $\hat\sigma$ makes it less significant; a **larger** $|t|$ means stronger evidence against $H_0$ (so "smaller $t$ → greater chance the samples are not from $H_0$" is the wrong one); $t$ is itself a random variable.

## Every past MC, with each option judged

!!! exam "June 2026 resit · 4a · 0.5 p"
    Which statement about prior probabilities in Bayesian hypothesis testing is FALSE? (a) When priors are equal and costs are equal, the Bayesian rule reduces to the ML rule. (b) A higher $P(H_0)$ raises $\eta$, requiring stronger evidence before $H_1$ is selected. (c) Increasing $P(H_1)$ raises $\eta$, making it harder to decide in favour of $H_1$.

???+ solution "Solution"
    (a) true (fact 8). (b) true (fact 9). **(c) false**: $P_1$ sits in the denominator; raising it lowers $\eta$.

!!! exam "April 2025 · 4b · 0.5 p"
    Which statement is FALSE? (a) In Bayesian detection the decision region is partitioned so that the Bayes risk is minimised. (b) The cost assignment $C_{01} = C_{10} = 10$, $C_{11} = C_{00} = 0$ minimises the total probability of error. (c) With the Neyman–Pearson test, for a fixed $P_{FA}$, $P_D$ is maximised.

???+ solution "Solution"
    (a) true (fact 7). (b) true: risk $= 10P_e$, same minimiser (fact 10). (c) true (fact 4). The official clarification: **as printed all three are true, there is no correct answer**. If this happens again, write "all true" and justify (b) with the scaling argument.

!!! exam "April 2024 · 4a · 0.5 p"
    Which statement is TRUE? (a) In Bayesian detection the decision region is partitioned so that the Bayes risk is **maximised**. (b) The cost assignment $C_{01} = C_{10} = 1$, $C_{11} = C_{00} = 0$ minimises the total probability of error. (c) With the NP test, for a fixed $P_{FA}$, $P_D$ is **minimised**.

???+ solution "Solution"
    **(b)**. (a) and (c) each have one swapped verb.

!!! exam "November 2022 · 4a · 0.25 p"
    Table with cells 1 = (decide $H_0$, true $H_0$), 2 = (decide $H_0$, true $H_1$), 3 = (decide $H_1$, true $H_0$), 4 = (decide $H_1$, true $H_1$). (a) 1 true negative, 2 miss/type II, 3 false alarm/type I, 4 detection. (b) 1 detection, 2 miss, 3 false alarm, 4 true negative. (c) 1 true negative, 2 false alarm/type I, 3 miss/type II, 4 detection. (d) 1 miss, 2 true negative, 3 detection, 4 false alarm.

???+ solution "Solution"
    **(a)** (facts 1 to 3). (c) swaps type I and II; (b) and (d) put detection in the $H_0$ column.

!!! exam "November 2022 · 4b · 0.25 p"
    The Neyman–Pearson test partitions the observation space such that (a) for a fixed $P_{FA}$, $P_D$ is minimised; (b) for a fixed $P_{FA}$, $P_D$ is maximised; (c) for a fixed $P_D$, $P_{FA}$ is minimised; (d) $P_{FA} = P_D$.

???+ solution "Solution"
    **(b)**. (c) is the dual statement, not the course's definition; (d) is the useless diagonal.

!!! exam "January 2022 resit · 4a · 0.3 p"
    Matched filter: (a) the SNR at the output is maximised; (b) it can be implemented as an FIR filter with $h[n] = s[n]$; (c) it can only be applied for uncorrelated noise samples.

???+ solution "Solution"
    **(a)**. (b) time-reversed, $h[n] = s[N-1-n]$. (c) prewhitening handles correlated noise.

!!! exam "October 2021 · 1e · 0.5 p"
    ROC curves appear in the lower triangle. Which **cannot** be the reason? (a) The variance of $H_0$ is set too high. (b) $H_0$ and $H_1$ are switched in the likelihood ratio. (c) The CDF is used to compute $P_d$. (d) $P_d$ and $P_{fa}$ are switched.

???+ solution "Solution"
    **(a)**: a large $H_0$ variance makes a poor detector, whose ROC approaches the diagonal from **above**, never below. (b), (c), (d) each flip the curve below the diagonal.

!!! exam "October 2021 · 1f · 0.5 p"
    $t = \frac{\hat\mu-\mu}{\hat\sigma/\sqrt N}$. Which is **not** correct? (a) The deviation becomes more significant with more samples. (b) A large $\hat\sigma$ makes the deviation less significant. (c) As $t$ gets smaller, there is a greater chance the samples do not belong to $H_0$. (d) The t-statistic is itself a random variable.

???+ solution "Solution"
    **(c)** is wrong: a **larger** $|t|$ is stronger evidence against $H_0$.

## Paraphrase drill (fresh wording)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| A type II error is a miss. | True | Fact 2. |
| The NP detector needs the prior probabilities of the hypotheses. | False | NP uses only the likelihoods and a target $P_{FA}$; priors belong to the Bayesian detector. |
| Doubling every cost in a Bayesian detector moves the threshold. | False | Fact 10. |
| A detector whose ROC is the diagonal is as good as flipping a coin. | True | $P_D = P_{FA}$ for every threshold. |
| With a very large cost for a miss, the Bayesian threshold becomes very small and the detector says $H_1$ almost always. | True | Fact 9; Apr 2025 4c. |
| The matched filter output SNR depends on the signal shape, not only on its energy. | False | The maximum output SNR equals signal energy over noise PSD level; the shape does not matter for white noise. |
| For Gaussian noise with equal variances, the likelihood ratio test reduces to comparing the sample mean with a threshold. | True | Oct 2021 4a: $\mathcal N(0,\sigma^2)$ vs $\mathcal N(\mu,\sigma^2)$ gives a linear statistic. |

</div>

**You can leave this page when you can:**

- [ ] fill the $2\times2$ decision/truth table with all four names and error types.
- [ ] state NP and Bayes in one sentence each, and the two swaps that make them false.
- [ ] say which way $\eta$ moves with each prior and each cost.

*[type I error]: false alarm.
*[type II error]: miss.
*[matched filter]: the linear filter maximising output SNR for a known signal in noise; impulse response = time-reversed signal.
