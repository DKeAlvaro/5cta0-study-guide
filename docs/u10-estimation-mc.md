# U10 · Estimation theory: the multiple-choice facts

<div class="meta"><span class="hot">Rank 8 · 4.45 points over 7 sittings</span><span>0.5 to 1 p every exam, pure lookup</span><span>40 min</span></div>

!!! need "Before this page"
    [U5](u05-mle.md), [U6](u06-map.md), [U7](u07-mmse.md), [U8](u08-crlb.md), [U9](u09-ls.md) for the ideas behind each sentence. This page is the drill.

## How these questions are built

Every estimation MC in this course is one true sentence from the reader plus one or two **swapped** versions: a word replaced by its opposite (*mean ↔ maximum*, *lower bounded by $\mathcal I$ ↔ by $1/\mathcal I$*, *positive ↔ negative*, *always ↔ sometimes*, *$x$ ↔ $\theta$*). The method, for every option: find the one word that could be swapped and check it.

!!! idea "The swap test"
    Read the option. Underline the strongest word: *always, regardless, only, strictly, never, cannot*. If the sentence is still true with that word removed but false with it, the option is a lie built around that word. Jun 2026 2a (b): "converges to the MLE **regardless** of the prior" is false only because of *regardless*.

## The facts, grouped (memorise these 18 sentences)

**Maximum likelihood**

1. The MLE is the value of **$\theta$** (not $x$) that maximises the likelihood $p(\mathbf x;\theta)$.
2. The MLE is **asymptotically** unbiased and asymptotically efficient (reaches the CRLB as $N\to\infty$); it does **not** always attain the CRLB.
3. For large $N$ the MLE is **Gaussian** distributed, $\hat\theta_{ML}\sim\mathcal N(\theta,\mathcal I^{-1}(\theta))$ (not uniform).
4. Invariance: for a one-to-one $\alpha = \psi(\theta)$, $\hat\theta_{ML} = \psi^{-1}(\hat\alpha_{ML})$.
5. The MLE can be found for general models, not only linear ones (the maximum may need numerical search).

**Fisher information and CRLB**

6. $\operatorname{Var}(\hat\theta)\ \ge\ 1/\mathcal I(\theta)$ for any unbiased estimator (bounded by the **inverse** of the information).
7. $\mathcal I(\theta)\ge0$; it is an expected squared derivative. "Strictly negative" is always the lie.
8. $N$ i.i.d. samples: $\mathcal I = N\,i(\theta)$, so the CRLB decreases as $1/N$.
9. The CRLB exists only if the regularity condition holds (support of $x$ not depending on $\theta$). "Can always be derived" is the lie.
10. **Efficient** = unbiased and variance **equal** to the CRLB. Nothing goes below.

**Bayesian estimation**

11. Bayesian estimators **do** use prior knowledge (a prior pdf on $\theta$); classical ones do not.
12. The Bayesian estimate minimises the Bayes risk $\iint C(e)\,p(\theta\mid\mathbf x)\,d\theta\,p(\mathbf x)\,d\mathbf x$.
13. Quadratic cost → MMSE = **mean** of the posterior. Uniform (hit-or-miss) cost → MAP = **maximum** of the posterior.
14. MMSE and MAP coincide for symmetric (e.g. Gaussian) posteriors; "always different" is the lie.
15. The MAP needs a prior; it depends on likelihood **and** prior.
16. With more data the MAP tends to the MLE for well-behaved priors; "regardless of the prior" is the lie.

**Least squares**

17. LS needs no noise pdf; it minimises $\sum(x[n] - s[n;\theta])^2$. The error vector is orthogonal to the columns of $\mathbf H$.
18. Non-linear LS: Gauss–Newton **or** Newton–Raphson; some problems become linear by transformation or separation.

## Every past MC, with each option judged

!!! exam "June 2026 resit · 2a · 0.5 p"
    Which of the following statements about Bayesian estimation is TRUE?

    - (a) The MAP estimate always equals the posterior mean.
    - (b) As the number of observations increases, the MAP estimate converges to the MLE regardless of the choice of prior.
    - (c) The MAP estimate depends on both the likelihood and the prior, and therefore cannot be computed without specifying a prior distribution.

???+ solution "Solution"
    (a) False: *always*; the posterior mean is the MMSE, equal to the MAP only for symmetric posteriors (fact 13, 14). (b) False: *regardless*; a prior that is zero on part of the range can block convergence (fact 16). (c) **True** (fact 15).

!!! exam "April 2025 · 2a · 0.5 p"
    Which of the following statements is FALSE?

    - a) The MLE is the argument maximising the likelihood.
    - b) The MMSE estimate results from minimising the square error.
    - c) In Bayesian estimation, the minimum mean square error estimator and the maximum posterior estimator will always result in a different estimate.

???+ solution "Solution"
    a) True (fact 1). b) True (fact 13). c) **False** (fact 14): *always*. Answer: c.

!!! exam "April 2024 · 2a · 0.5 p"
    Which of the following statements is TRUE?

    - a) The variance of any unbiased estimator is lower bounded by the Fisher information, i.e., $Var(\hat{\theta}) \geq \mathcal{I}(\theta)$.
    - b) The Fisher information is strictly negative.
    - c) The Fisher information for $N$ i.i.d. observations is $N i(\theta)$.

???+ solution "Solution"
    a) False: bounded by $1/\mathcal I$ (fact 6). b) False (fact 7). c) **True** (fact 8).

!!! exam "April 2024 · 2b · 0.5 p"
    Which of the following statements is TRUE?

    - (a) In Bayesian estimation, the minimum mean square error is the mean of the posterior PDF.
    - (b) In Bayesian estimation, the minimum mean square error is the maximum of the posterior PDF.
    - (c) In Bayesian estimation, the MMSE estimator and the MAP estimator will always result in a different estimate.

???+ solution "Solution"
    (a) **True** (fact 13). (b) False: that is the MAP. (c) False: *always* (fact 14).

!!! exam "November 2022 · 2a, 2b, 2c · 0.25 p each"
    **2a** TRUE about Fisher information: (a) for $N$ i.i.d. observations it is $Ni(\theta)$; (b) $Var(\hat\theta)\ge\mathcal I(\theta)$; (c) $\mathcal I(\theta)$ is strictly negative.

    **2b** TRUE about the MLE: (a) always achieves the CRLB; (b) can only be found for special problems such as linear models; (c) is asymptotically unbiased.

    **2c** TRUE about Bayesian estimation: (a) Bayesian estimators do not incorporate prior knowledge; (b) the Bayesian estimate minimises the Bayes risk $\hat\theta = \arg\min\iint C(e)p(\theta\mid\mathbf x)d\theta\,p(\mathbf x)d\mathbf x$; (c) minimising the Bayes risk for the uniform cost gives the MMSE.

???+ solution "Solution"
    2a: **(a)** (fact 8); (b) inverse (fact 6); (c) never negative (fact 7). 2b: (a) *always* (fact 2); (b) *only* (fact 5); **(c)** (fact 2). 2c: (a) reversed (fact 11); **(b)** (fact 12); (c) uniform cost gives the MAP (fact 13).

!!! exam "January 2022 resit · 2a to 2d · 0.3 p each"
    **2a** CRLB: (a) can always be derived; (b) for i.i.d. observations the CRLB decreases linearly with the number of observations; (c) an estimator whose variance is lower than the CRLB is called efficient.

    **2b** MLE: (a) the ML estimate is the value of $x$ that maximises the likelihood; (b) for large $N$ it is uniformly distributed; (c) invariance $\hat\theta_{ML} = \psi^{-1}(\hat\alpha_{ML})$.

    **2c** LS: (a) some non-linear LS problems can be solved analytically by separation or transformation; (b) the solution vector is orthogonal to the span of the columns of $\mathbf H$; (c) only Gauss–Newton applies.

    **2d** Bayesian: (a) the MMSE is the maximum of the posterior; (b) the MMSE is the mean of the posterior; (c) MMSE and MAP always differ.

???+ solution "Solution"
    2a: (a) *always* (fact 9); **(b)** (fact 8); (c) *lower than* (fact 10). 2b: (a) $x$ for $\theta$ (fact 1); (b) Gaussian (fact 3); **(c)** (fact 4). 2c: **(a)** (fact 18); (b) error, not solution (fact 17); (c) *only* (fact 18). 2d: (a) maximum is MAP; **(b)** (fact 13); (c) *always* (fact 14).

!!! exam "January 2019 · 1b · 0.5 p"
    Which expression describes the maximum likelihood estimator? A. $\arg\min_\theta\sum(x[n]-s[n;\theta])^2$. B. $\arg\min_{\hat\theta}\int(\hat\theta-\theta)^2p(x\mid\theta)dx$. C. $\arg\max_\theta p(\theta\mid x)$. D. $\arg\max_\theta p(x\mid\theta)$.

???+ solution "Solution"
    A is least squares. B is a mean-square-error minimisation (MMSE flavour). C is the MAP (posterior). **D** is the MLE (likelihood).

## Paraphrase drill (fresh wording, never printed in an exam)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| Doubling the number of independent samples halves the Cramér–Rao bound. | True | $\mathcal I = Ni(\theta)$, bound $= 1/(Ni)$ (fact 8). |
| An unbiased estimator can have a variance smaller than $1/\mathcal I(\theta)$ if it is cleverly designed. | False | The bound is a bound (fact 6, 10). |
| If the posterior is a Gaussian, the MAP and the MMSE give the same number. | True | Symmetric posterior (fact 14). |
| The MAP can be computed from the likelihood alone when the data set is large. | False | A prior is always needed to define a posterior (fact 15). |
| The likelihood ratio of the data is maximised by the ML estimator. | False | The MLE maximises the likelihood, not a ratio; ratios belong to detection ([U16](u16-lrt.md)). |
| Least squares can be used when the noise distribution is unknown. | True | Fact 17. |
| The ML estimate of $\theta^2$ is the square of the ML estimate of $\theta$. | True | Invariance (fact 4). |
| For a pdf whose support is $[0,\theta]$ the Fisher information is $N/\theta^2$. | False | The regularity condition fails; no CRLB (fact 9). |
| The Fisher information can be computed as the expected square of the score $\partial\ln p/\partial\theta$. | True | Second form of the definition ([U8](u08-crlb.md)). |
| Minimising the hit-or-miss Bayes risk gives the posterior mean. | False | Hit-or-miss gives the MAP; quadratic gives the mean (fact 13). |

</div>

**You can leave this page when you can:**

- [ ] recite facts 1 to 18 from the headings alone.
- [ ] apply the swap test to any option and name the swapped word.
- [ ] tell apart the four $\arg$ expressions of Jan 2019 1b at a glance.

*[swap test]: a false MC option is usually a true sentence with one word replaced by its opposite.
*[Bayes risk]: the expected cost of the estimation error, averaged over the posterior and the data.
