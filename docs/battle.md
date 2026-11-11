# Battle table: every past question, solved with the sheet alone

<div class="meta"><span class="hot">10 sittings · every sub-question</span><span>Column 2 = which sheet box, what to do with it, the answer</span></div>

How to use it: take a past exam, the printed [cheat sheet](cheatsheet.md) and nothing else. Solve. Then open this table and compare. If a question needs something the sheet does not say, that is a sheet bug: fix the sheet.

<div class="battle" markdown>

## June 2026 resit

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a independence, always true? | U1 last line: independence means $P(A\mid B) = P(A)$; "$P(A\cap B) = 0$" is disjoint and "$P(A\cup B) = P(A)+P(B)$" needs disjoint. → **(d)** |
| 1b three machines | U1 steps 3–4: shares 0.4/0.35/0.25, rates 0.02/0.04/0.05; forward sum 0.0345; backward $0.014/0.0345$. → **0.0345; 0.41** |
| 1c $6x^2y$ on the square | U2 steps 3, 5: square → number limits; $\int_0^1 6x^2y\,dy = 3x^2$ on $0\le x\le1$; rectangle and factors → independent. → **$3x^2$, $0\le x\le1$; independent** |
| 1d WSS condition | U3 bullet "WSS": constant mean and lag-only autocorrelation. → **(b)** |
| 1e innovation filter condition | U4 MC line: minimum phase, poles and zeros inside. → **(a)** |
| 2a Bayesian estimation TRUE | U10 swap test: "always" (a) and "regardless" (b) are swaps; MAP needs a prior. → **(c)** |
| 2b Gamma MLE | U5 steps 1–6 with the Gamma line: $\ln L = (k-1)\sum\ln x_i - \frac{\sum x_i}{\theta} - nk\ln\theta - n\ln\Gamma(k)$; derivative $\frac{S}{\theta^2} - \frac{nk}{\theta} = 0$. → **$\hat\theta = \sum x_i/(nk) = \bar x/k$**; it matches the model mean $k\theta$ to the observed average |
| 2c NegBin + Beta | U6 steps 1–3 and the NegBin line: $L = 360\,\theta^{10}(1-\theta)^{12}$; posterior Beta(12,15); MAP $\frac{a-1}{a+b-2} = 11/25$. → **0.44** |
| 2d Poisson + Gamma | U6 Poisson line: posterior Gamma(23, 8); MAP $22/8$; MLE $20/6$; prior pulls down, fades with $n$. → **2.75 vs 3.33** |
| 3a periodogram TRUE | U15 table and window bullets: not consistent (b); length ≠ leakage; Hamming widens the lobe; Bartlett averages. → **(b)** |
| 3b Welch $K$ | U15 "Welch segments": $(1000-200)/100 + 1 = 9$; ratio $1/K$. → **9; 1/9** |
| 3c correlogram 3,2,1 | U11 formula: $3 + 4\cos\theta + 2\cos2\theta$. → **that** |
| 3d AR(2) | U12 steps 1–3 and the Jun26 line: $3a_1+2a_2 = -2$, $2a_1+3a_2 = -1$; $\sigma_i^2 = 3 - 1.6 + 0.2$; AR(2) denominator formula. → **$a_1 = -0.8$, $a_2 = 0.2$, $\sigma_i^2 = 1.6$, $P = 1.6/(1.68 - 1.92\cos\theta + 0.4\cos2\theta)$** |
| 3e AR order | U15 "AR order" bullet: residual variance always falls → overfitting; AIC/MDL/FPE penalty grows with $p$; any spectrum needs a sufficiently high $p$. → **three sentences from the bullet** |
| 4a priors FALSE | U18 last sentence of the box: larger $P_1$ → smaller $\eta$. → **(c)** |
| 4b Rayleigh LRT | U16 steps 1–6 and the Rayleigh line. → **decide $H_1$ when $x > \sqrt{\frac{2\sigma_0^2\sigma_1^2}{\sigma_1^2-\sigma_0^2}\ln(\eta\sigma_1^2/\sigma_0^2)}$; closer $\sigma$'s → ROC toward the diagonal** |
| 4c priors 0.9/0.1 | U18: $\eta = P_0/P_1 = 9$, plug into the 4b threshold with $\ln(9\sigma_1^2/\sigma_0^2)$. → **accept $H_1$ above that larger threshold** |

## April 2025

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a three CT scanners | U1: shares $18/55$ etc., rates = complements 0.15/0.10/0.34; forward $10/55$; backward $2.2/10$. → **0.18; 0.22** |
| 1b expected value | U3 first bullet: weighted average of the outcomes. → **(d)** |
| 1c find $c$ on the triangle | U2 step 2 and its Apr25 line: $\frac c6 + \frac12 = 1$. → **$c = 3$** |
| 1d dice ergodic | U3 ergodic bullet: i.i.d. rolls → ergodic in mean and variance. → **(b)** |
| 1e factorise $1/(61+60\cos\theta)$ | U4 steps 1–4 and its Apr25 line. → **$\sigma_i^2 = 1/36$, $L = 1/(1+\frac56z^{-1})$** |
| 2a FALSE statement | U10: "always different" is the swap. → **(c)** |
| 2b LS line | U9 box and its Apr25 line: $26a+10b = 34$, $10a+6b = 20$. → **$y = \frac1{14}x + \frac{45}{14}$** |
| 2c sigmoid MLE | U5 step 4 (chain rule) and the sigmoid line. → **$\hat\theta = -\ln(\frac{4x}{7}-1)$, $x>7/4$** |
| 2d MAP of $\theta^A(1-\theta)^B$ | U6 step 3 Beta shortcut, Apr25 line. → **$\frac{\beta_1-1+k_1N_1}{\beta_1-1+k_1N_1+\beta_0-1+k_0N_0}$** |
| 3a energy or power | U15 energy bullet: $A\sin\omega t$ periodic → power $A^2/2$; $e^{-n}$ → energy $1/(1-e^{-2}) = 1.157$, $P = 0$. → **that** |
| 3b spectral TRUE | U15: bias from windowing affects any signal (a); padding, same-estimator and window-variance options are swaps. → **(a)** |
| 3c estimator table | U15 table rows: Bartlett, periodogram, ARMA, Blackman–Tukey, WOSA. → **that** |
| 3d correlogram | U11 Apr25 line. → **$2 - \frac12\cos\theta - \frac38\cos2\theta$** |
| 3e AR(1) | U12 Apr25 line. → **$a_1 = \frac18$, $\sigma_i^2 = \frac{63}{32}$, $P = 126/(65+16\cos\theta)$** |
| 3f MA(1) | U13 steps 1–3 and the Apr25 line. → **$b_1 = -0.13$, $\sigma_i^2 = 1.97$, $P = 2 - 0.5\cos\theta$** |
| 3g which plot | U15 "which plot": values at 0 and $\pi$ (1.125/2.125, 1.56/2.57, 1.5/2.5), AR and MA overlap. → **plot D, option (a)** |
| 4a LRT power pdf | U16 Apr25 line: $2x^6\ge0.2$. → **$x\ge0.1^{1/6} = 0.68$** |
| 4b FALSE statement | U19: all three sentences are true facts (NP maximises $P_D$; Bayes minimises risk; scaled costs still minimise $P_e$). → **no false option as printed; say so and justify (b)** |
| 4c genAI, $C_{01} = 100C_{10}$ | U18 posterior form: threshold 0.01; ratio 5 ≥ 0.01. → **$H_1$: the student fails** |

## April 2024

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a transducer third year | U1 lifetime line. → **(d) 0.18** |
| 1b TB test | U1 Apr24 line. → **0.047** |
| 1c $p_Y$ and $p_{X\mid Y}$ on $0\le y\le x\le1$ | U2 steps 3–4 and the Apr24 lines. → **$2(1-y)$, $0\le y\le1$; $1/(1-y)$, $y\le x\le1$** |
| 1d WSS / ergodic of $\cos(t+U)$, $A\cos t$ | U3 recipe bullet. → **1: yes, yes; 2: no, no** |
| 1e factorise $7/(25-24\cos\theta)$ | U4 Apr24 line. → **$\sigma_i^2 = 7/16$, $L = 1/(1-\frac34z^{-1})$** |
| 2a Fisher TRUE | U8 MC line: $N i(\theta)$. → **(c)** |
| 2b MMSE TRUE | U7 last line: MMSE = posterior mean. → **(a)** |
| 2c MLE of $\frac{x}{2\theta}e^{-x^2/2\theta}$ | U5 example line. → **$\hat\theta = \frac1{2N}\sum x_n^2$** |
| 2d MAP with sigmoid | U6 sigmoid-posterior line. → **$\hat\theta = -\ln(\frac x2 - 1)$, $x>2$** |
| 3a methods table | U15 bullets "Consistent / FT of autocorrelation / averages / overlap / variance ∝ $P^2$ / linear model". → **parametric; Welch; Bartlett+Welch+BT; correlogram+BT; periodogram; Bartlett+Welch** |
| 3b model type | U14 "Name": only kicks, oldest $i[n-3]$. → **MA(3)** |
| 3c autocorrelation | U14 "MA lags" and its Apr24 line. → **$\frac{25}{16}, -\frac34, \frac12, -\frac12$** |
| 3d correlogram | U11 Apr24 line. → **$\frac{25}{16} - \frac32\cos\theta + \cos2\theta - \cos3\theta$** |
| 3e AR(2) | U12 steps with $r = \frac{25}{16}, -\frac34, \frac12$ and the Apr24 numbers. → **$a_1 = \frac{204}{481}$, $a_2 = -\frac{56}{481}$, $\sigma_i^2 = 1.19$, $P = \sigma_i^2/|1+a_1e^{-j\theta}+a_2e^{-j2\theta}|^2$** |
| 3f which plot | U15 "which plot": 0.06/5.06 and 0.69/5.6. → **plot B, option (c)** |
| 4a hypothesis testing TRUE | U19: "maximised" and "minimised" are swaps. → **(b)** |
| 4b Gaussian vs $\frac14e^{-y/2}$ | U17 steps 1–6 and its Apr24 line. → **$y_{th} = 1.588$, $H_1$ above; $P_{FA} = Q(1.59)$, $P_D = \frac12e^{-0.794}$ (folded: 0.112, 0.452)** |

## November 2022

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a P(pass) | U1 step 3: $0.75(0.65)+0.4(0.35) = 0.6275$. → **(c)** |
| 1b marginal PMF | U2 step 6: add the rows. → **(b) $\frac{13}{24}, \frac{11}{24}$** |
| 1c uniform in $[-A,A]$ | U3 ergodic bullet: mean 0, ergodic in the mean. → **(d)** |
| 1d factorise $1/(\frac53-\cos\theta)$ | U4 Nov22 line. → **$\sigma_i^2 = \frac23$, $L = 1/(1-\frac13z^{-1})$** |
| 2a/2b/2c MC | U8 MC line ($Ni$); U8 "asymptotically unbiased"; U10 "Bayes risk minimised". → **(a); (c); (b)** |
| 2d MLE of the angle | U5 angle line. → **$\tan^{-1}(x_2/x_1)$, right quadrant** |
| 2e Fisher information | U8 Nov22 line. → **$A^2/\sigma^2$** |
| 2f MMSE | U7 Nov22 line. → **$2/(x+a)$** |
| 2g MAP | U6 Nov22 line. → **$1/(x+a)$** |
| 3a Bartlett/WOSA | U15 table: variance $/K$, bias increases. → **(a)** |
| 3b windows | U15 window bullet: main lobe → resolution, side lobes → leakage. → **(b)** |
| 3c type | U14 "Name". → **ARMA(1,1)** |
| 3d PSD | U14 "PSD" line. → **$28\frac{1-\cos\theta}{25-24\cos\theta}$** |
| 3e autocorrelation | U14 ARMA bullet and its Nov22 line. → **$r_0 = 1$, $r[\tau] = -\frac18(\frac34)^{|\tau|-1}$** |
| 3f AR(1) | U12 Nov22 line. → **$\frac18$, $\frac{63}{64}$, $63/(65+16\cos\theta)$** |
| 3g MA(1) | U13 line "Apr25 3f and Nov22 3g". → **$b_1 = -0.13$, $\sigma_i^2 = 0.98$, $1 - 0.25\cos\theta$** |
| 4a table names | U19 first two sentences. → **(a)** |
| 4b Neyman–Pearson | U19. → **(b)** |
| 4c Laplacian LRT | U16 Laplacian line. → **$\sum|x_n|\underset{H_1}{\overset{H_0}{\gtrless}} N\ln2 - \ln\gamma$** |
| 4d indicate $P_{FA}$, $P_M$ | U17 "curve = truth, side = said"; $H_1$ side is $y<1$. → **$P_{FA}$ = $e^{-y}$ left of 1; $P_M$ = $2e^{-2y}$ right of 1** |
| 4e threshold for $P_{FA} = 0.1$ | U17 Nov22 line. → **$\gamma' = 0.105$, $P_D = 0.19$** |
| 4f Bayesian threshold | U18 Nov22 line. → **$\ln 3$** |
| 4g $P_M$, $P_{FA}$ | U18 Nov22 line. → **$\frac23$, $\frac19$** |

## January 2022 resit

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a unsatisfactory given experience | U1: complement $0.85$ for $P(E\mid S^c)$; $0.2125/0.8125$. → **(c) 0.26** |
| 1b pictures | U3 "A picture is a realisation …". → **(b)** |
| 1c dice | U3 ergodic bullet. → **(b)** |
| 1d printed factorisation | U4 MC line: $L(z)$ = the $z^{-1}$ half, constant = $\sigma_i^2 = 2$. → **(c)** |
| 2a–2d MC | U8 MC line (CRLB falls as $1/N$; "efficient" = equals); U8/U10 (invariance; MLE Gaussian); U9 (transform/separate; error orthogonal; NR works); U7 (mean). → **(b); (c); (a); (b)** |
| 2e CRLB for $0\le x\le\theta$ | U8 step 0. → **not possible, regularity violated** |
| 2f posteriors of $X = \pm1$ | U6 discrete line. → **the two fractions** |
| 2g MMSE | U7 Jan22 line. → **$\tanh(y/\sigma^2)$** |
| 2h MAP threshold | U6 discrete line: ratio $e^{2y/\sigma^2}\gtrless1$. → **$y_{th} = 0$** |
| 3a FTD/DFT plots | U15 Jan22 3a bullet. → **(b) 1B 2D 3C 4A** |
| 3b MA(2) $a$, $b$ | U13 MA(2) line. → **$a = -\frac34$, $b = \frac14$** |
| 3c correlogram | U11 Jan22 line ($r_0 = \frac{13}8$ from U13). → **$\frac{13}8 - \frac{15}8\cos\theta + \frac12\cos2\theta$** |
| 3d AR(1) | U12 Jan22 line; PSD via the AR(1) denominator. → **$\frac{15}{26}$, $\frac{451}{416}$, $5863/(7208+6240\cos\theta)$** |
| 4a matched filter | U19 matched-filter sentence. → **(a)** |
| 4b sketch and shade | U17 Apr24/Jan22 line: crossing at $\pm1.588$, $H_1$ outside. → **shade bell tails ($P_{FA}$) and tent centre ($P_M$)** |
| 4c $P_D$, $P_{FA}$ | same line: $2Q(1.59)$, $e^{-0.794}$. → **0.112; 0.452** |

## October 2021 practice

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a virus test | U1 steps: $0.0171/0.04656$. → **(b) 37 %** |
| 1b covariance | U3 covariance bullet. → **(d)** |
| 1c expected value | U3 first bullet. → **(b)** |
| 1d binomial | U3 binomial line. → **(d) 0.2936** |
| 1e ROC below diagonal, cannot be | U19 ROC sentence. → **(a)** |
| 1f t-statistic not correct | not on the sheet (dropped, asked once): larger $|t|$ = more evidence against $H_0$. → **(c)** |
| 2a MVUE → pdf | not on the sheet (asked once): efficiency condition $\partial\ln p/\partial\theta = \mathcal I(\hat\theta-\theta)$ integrated gives the Gaussian. → **i.i.d. Gaussian, variance $A^2$** |
| 2b MLE | U5 example line ($\frac x\theta$ front factor changes nothing). → **$\frac{1}{2N}\sum x^2$** |
| 3a autocorrelation from $H(z)$ | U14 ARMA bullet with $b_1 = -\frac23$, $a_1 = -\frac12$, $\sigma_i^2 = 1$: $r_0 = \frac{13}9 + \frac14r_0 - \frac23$. → **$\frac{28}{27}$, $-\frac4{27}$, $(\frac12)^{|\tau|-1}r_1$** |
| 3b AR(1) | U12 steps: $a_1 = \frac17$, $\sigma_i^2 = \frac{64}{63}$. → **$224/(225+63\cos\theta)$** |
| 3c correlogram as MA(1) | U11 formula with lags 0, ±1. → **$\frac{28}{27} - \frac8{27}\cos\theta$** |
| 4a erf table | U17 Gaussian-means line. → **the 10 pairs (e.g. $y_{th}=1,\mu=1$: 0.5 / 0.1585)** |
| 4b LLRT Gaussian variances | U16 Gaussian-variances line. → **that** |

## January 2020 retake

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a legitimate autocorrelation | U3 legitimate-autocorrelation line (symmetry, max at 0). → **A (only $r_B$)** |
| 1b WOSA | U15 table Welch row: overlap, not exactly $1/K$. → **option 2** |
| 1c windows | U15 window bullet: wider main lobe → worse resolution. → **option 3** |
| 1d expected value | U3 first bullet. → **option 2 (mean over infinite observations)** |
| 2 painting machines | U1 steps. → **0.819; 0.18** |
| 3a correlogram | U11 Jan20 line. → **$\frac1{21} + \frac4{105}\cos\theta$** |
| 3b MA(1) and relation | U13 steps: $\rho = \frac25$, $b_1 = \frac12$, $\sigma_i^2 = \frac4{105}$; "truly MA(1) → equals the correlogram". → **same curve, because all nonzero lags are reproduced** |
| 4a–4d $Ae^{\phi n}$ | U9 last paragraph: LS; $\hat A = \sum xe^{\phi n}/\sum e^{2\phi n}$; non-linear cost; Gauss–Newton (write the update from U9 of the guide). → **as U9** |
| 5a–5c exponentials | U17 exponential line and steps 1–6: $x_{th} = \ln20/1.9 = 1.58$, $H_1$ left; $P_{fa} = 0.1\Rightarrow x_{th} = 1.054$, $\lambda_1 = 2.19$; $P_{fa} = 0.5, 0.9 \Rightarrow P_d\approx1$; ROC toward the corner for larger $\lambda_1$. → **that** |

## November 2019

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a cross-correlation | not on the sheet (flawed key): time average $\frac14\sum x[n]y[n-\tau]$ gives $\frac54, 2, \frac{11}4, \frac74, 1, \frac14$ for $\tau = -3..2$. → **B's numbers shifted by 3** |
| 1b five T/F | U1 (union rule), U3 (relative frequency, CDF limits), U13 MC line (linear prediction gives AR). → **F F T T F** |
| 1c methods table | U15 table. → **copy the five rows** |
| 2a correlogram | U11 formula. → **$1+1.4\cos\theta+\cos2\theta+0.6\cos3\theta$** |
| 2b AR(2) | U12 steps: $a_1+0.7a_2 = -0.7$, $0.7a_1+a_2 = -0.5$. → **$-0.686$, $-0.020$, $\sigma_i^2 = 0.51$** |
| 3a MLE Rayleigh | U5 Rayleigh line. → **$\sqrt{\frac1{2N}\sum x^2}$** |
| 3b CRLB | U8 Rayleigh line. → **$\theta^2/(4N)$** |
| 3c MAP with exponential prior | U6 "no closed form" line: write the derivative $= 0$. → **$-\frac{2N}\theta + \frac{\sum x^2}{\theta^3} - \lambda = 0$** |
| 4a sketch, equations | U17 steps 4–5: two bells, $H_1$ in both tails, $P_d = 2\int_{x_{th}}^\infty p_1$, $P_{fa} = 2\int_{x_{th}}^\infty p_0$. → **that** |
| 4b numbers | U17 Nov19 line. → **0.318; 0.004** |
| 4c LLRT | U16 Gaussian-variances line. → **that** |

## January 2019 retake

| Question | Sheet box → how to solve it with the sheet only → answer |
|---|---|
| 1a discrete RVs | U3 "Discrete = countable". → **B, C** |
| 1b MLE expression | U10 true sentences. → **D** |
| 1c non-parametric | U15 table (Bartlett bias up with shorter segments; BT consistent; Welch not exactly $1/K$; padding no resolution). → **A, C** |
| 1d linear models | U13 MC line (MA fit non-linear) and U14 (compression; ARMA matrix not diagonal; MA($Q$) has $Q+1$ distinct lags). → **C, D** |
| 2a MLE exponential | U5 example line. → **$N/\sum x_i$** |
| 2b MMSE uniform prior | U7 steps 1–2 with the handed-out integrals; both limits 0 and 2. → **$\frac{2-(4x^2+4x+2)e^{-2x}}{x[1-(2x+1)e^{-2x}]}$** |
| 2c MAP uniform prior | U6 step 4: flat prior → MLE, capped at 2. → **$N/\sum x_i$** |
| 3a definitions | U16 step 1 and U17 "curve = truth, side = said". → **$L\gtrless\gamma$; $P_{fa} = \int_{L>\gamma}p_0$; $P_d = \int_{L>\gamma}p_1$** |
| 3b erf table | U17 Gaussian-means line with $\sigma_1$: standardise $(X-\mu_1)/\sigma_1$. → **$P_d$: 0.5, 0.977, 0.8415, 0.8415; $P_{fa}$: 0.1585, 0.1585, 0.1585, 0.023** |
| 4 Wiener filter | out of scope (dropped from the course). → **$\mathbf w = [1, 2]$, $J = 0$ per the key** |

</div>

Rows marked "not on the sheet" are deliberate: Wiener filtering, the t-statistic, the MVUE-to-pdf derivation and the flawed cross-correlation item were each asked once, before 2022, and the space went to the question types that recur.
