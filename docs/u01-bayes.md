# U1 · Total probability and Bayes: the word problems

<div class="meta"><span class="hot">Rank 10 · 4.4 points over 8 sittings</span><span>0.25 to 0.5 p every exam, 2 p in Jan 2020</span><span>35 min</span></div>

!!! need "Before this page"
    Fractions. Nothing else. For the exponential-lifetime variant: [M1](maths.md#m1-exponents-and-logarithms).

## The idea in plain words

Something is produced by several sources (machines, scanners, groups of students), each with its own share and its own defect rate. Two questions keep coming back. **Forward**: what fraction of everything is defective? Add up share × defect rate over the sources. **Backward**: given that an item is defective, which source made it? Take that source's slice of the defective pile and divide by the whole defective pile. That division is Bayes' theorem.

!!! idea "The thing that confused me"
    Which number is the "given" in "$P(A\mid B)$"? The sentence after **given** (or "if … is found to be …", "that has passed the test") is $B$: it goes on the right of the bar and is the **denominator** of Bayes. The thing you are asked about goes on the left.

## A tiny example with numbers

Two machines. $M_1$ makes 60 % of parts, 10 % of its parts are bad. $M_2$ makes 40 %, 20 % bad.
Forward: $P(\text{bad}) = 0.6\cdot0.10 + 0.4\cdot0.20 = 0.06 + 0.08 = 0.14$.
Backward: $P(M_2\mid\text{bad}) = \dfrac{0.4\cdot0.20}{0.14} = \dfrac{0.08}{0.14} = 0.5714$. Although $M_2$ makes fewer parts, it makes most of the bad ones.

!!! question "Your turn"
    Same two machines. $P(M_1\mid\text{bad})$? And do the two backward answers add to 1?

    ???+ solution "Answer"
        $\frac{0.06}{0.14} = 0.4286$; $0.4286 + 0.5714 = 1$. Yes, always: the bad part came from exactly one machine.

## The formulas, every symbol named

<div class="key" markdown>

$$P(B) = \sum_i P(B\mid A_i)\,P(A_i)\qquad\text{(total probability)}$$

$$P(A_k\mid B) = \frac{P(B\mid A_k)\,P(A_k)}{P(B)} = \frac{P(B\mid A_k)\,P(A_k)}{\sum_i P(B\mid A_i)\,P(A_i)}\qquad\text{(Bayes)}$$

</div>

| Symbol | Meaning |
|---|---|
| $A_i$ | the sources (machines, scanners, "followed the course" / "did not"); they cover every case and do not overlap |
| $P(A_i)$ | the share of source $i$ (a percentage, or a count divided by the total count) |
| $B$ | the observed event ("defective", "passes", "tests positive") |
| $P(B\mid A_i)$ | the rate of $B$ inside source $i$ |
| $P(B)$ | the overall rate of $B$: the forward answer, and the denominator of the backward one |
| complement | $P(B^c) = 1 - P(B)$; "not pass" = $1 - $ "pass" per source |

**Where Bayes comes from.** $P(A\cap B) = P(A\mid B)P(B) = P(B\mid A)P(A)$ (two ways to write the same joint probability); divide by $P(B)$.

**Independence (Jun 2026 1a).** $A$ and $B$ independent means $P(A\cap B) = P(A)P(B)$, equivalently $P(A\mid B) = P(A)$: knowing $B$ does not change $A$. Not $P(A\cap B) = 0$ (that is "disjoint", the opposite of independent for events with nonzero probability) and not $P(A\cup B) = P(A) + P(B)$ (that needs disjoint).

## What the exam asks, in its own words

| IF YOU SEE | It means |
|---|---|
| "produces 40 % of the chips", "scans 18 patients" | the share $P(A_i)$; counts must be divided by the total ($18/55$) |
| "the probability that a chip is defective is 2 % for $M_1$" | $P(B\mid M_1) = 0.02$ |
| "85 % of the images produced by CT1 have sufficient quality" and the question asks about images that do **not** pass | $P(\text{bad}\mid CT1) = 1 - 0.85 = 0.15$: take the complement per source first |
| "what is the probability that a randomly selected chip will be defective?" | forward: total probability |
| "if a randomly selected chip is found to be defective, what is the probability that it was produced by $M_2$?" | backward: Bayes with "defective" as the given |
| "a test is 99 % accurate" | $P(+\mid\text{disease}) = 0.99$ **and** $P(-\mid\text{no disease}) = 0.99$, so false-positive rate $0.01$ |
| "lifetime … $\Pr[T\ge t] = e^{-t/5}$ … breaks in the third year given it was still working after 2 years" | conditional probability with the survival function: $\frac{P(2\le T\le3)}{P(T\ge2)}$ |
| "please provide only the final answer" | still write the two lines on scrap paper; the number is all that is graded |

## Recipe

!!! recipe key "U1 · Forward then backward"
    1. **Name the sources** and write their shares $P(A_i)$ (convert counts to fractions of the total). They must add to 1.
    2. **Write the rate of the observed event in each source**, $P(B\mid A_i)$, taking complements if the text gives the opposite event.
    3. **Forward**: $P(B) = \sum_i P(B\mid A_i)P(A_i)$. Write each product on its own, then add.
    4. **Backward**: $P(A_k\mid B) = \dfrac{\text{the one product for source } k}{P(B)}$.
    5. **Check**: all backward answers add to 1; the backward answer for a source is larger than its share exactly when its rate is above average.

## Worked exam question, one step at a time

!!! exam "June 2026 resit · 1b · 0.3 p"
    A manufacturing plant has three machines, $M_1$, $M_2$, and $M_3$, that produce microchips. Machine $M_1$ produces 40 % of the chips, $M_2$ produces 35 %, and $M_3$ produces 25 %. The probability that a chip is defective is 2 % for $M_1$, 4 % for $M_2$, and 5 % for $M_3$. The chips from all machines are mixed together randomly before quality control. **Please provide only the final answer.** 1. What is the probability that a randomly selected chip will be defective? [0.15] 2. If a randomly selected chip is found to be defective, what is the probability that it was produced by machine $M_2$? [0.15]

<div class="stepper" markdown>

**Step 1 · Shares.** $P(M_1) = 0.40$, $P(M_2) = 0.35$, $P(M_3) = 0.25$. Sum $= 1.00$. ✓

**Now do step 2 yourself:** the defect rate per machine, as $P(D\mid M_i)$.

---

**Step 2 · Rates.** $P(D\mid M_1) = 0.02$, $P(D\mid M_2) = 0.04$, $P(D\mid M_3) = 0.05$ (already the event asked about, no complement needed).

**Now do step 3 yourself:** the three products and their sum.

---

**Step 3 · Forward.** $0.40\cdot0.02 = 0.0080$; $0.35\cdot0.04 = 0.0140$; $0.25\cdot0.05 = 0.0125$. $P(D) = 0.0080 + 0.0140 + 0.0125 = 0.0345$.

**Now do step 4 yourself:** Bayes for $M_2$.

---

**Step 4 · Backward.** $P(M_2\mid D) = \dfrac{0.0140}{0.0345} = 0.4058$.

**Step 5 · Check.** $M_1$: $0.0080/0.0345 = 0.232$; $M_3$: $0.0125/0.0345 = 0.362$; sum $0.232 + 0.406 + 0.362 = 1.000$. $M_2$'s rate (4 %) is above the average (3.45 %), so its backward share (0.41) exceeds its forward share (0.35). ✓

!!! answer "Answer"
    1. $P(\text{defective}) = 0.0345$. 2. $P(M_2\mid\text{defective}) = 0.406$.

</div>

## Do it cold · 1 (complements and counts)

!!! exam "April 2025 · 1a · 0.3 p"
    An hospital has three CT scanners CT1, CT2, and CT3. 85 % of the images produced by CT1 have sufficient quality, while for CT2 and CT3 the percentages are 90 % and 66 %. Each day, CT1 scans 18 patients, CT2 scans 22, and CT3 scans 15. The images are mixed at random before quality control. Assuming the same number of images per patient: 1. What is the probability that one image will NOT pass the quality test? 2. What is the probability that a bad quality image comes from CT2?

???+ solution "Solution"
    **Shares.** Total $18 + 22 + 15 = 55$: $P(CT1) = \frac{18}{55}$, $P(CT2) = \frac{22}{55}$, $P(CT3) = \frac{15}{55}$.

    **Rates of "bad"** (complements): $0.15$, $0.10$, $0.34$.

    **Forward.** $\frac{18\cdot0.15 + 22\cdot0.10 + 15\cdot0.34}{55} = \frac{2.7 + 2.2 + 5.1}{55} = \frac{10.0}{55} = 0.1818$.

    **Backward.** $P(CT2\mid\text{bad}) = \frac{2.2/55}{10/55} = \frac{2.2}{10} = 0.22$.

    !!! answer "Answer"
        1. $0.18$. 2. $0.22$.

## Do it cold · 2 (MC, forward only)

!!! exam "November 2022 · 1a · 0.25 p"
    About 65 % of students who enroll for the exam have followed the course. The probability of passing is 0.75 for students who followed the course and 0.4 for those who did not. What is the probability of passing the exam? (a) 0.53 (b) 0.52 (c) 0.63 (d) 0.65

???+ solution "Solution"
    $P(\text{pass}) = 0.75\cdot0.65 + 0.40\cdot0.35 = 0.4875 + 0.14 = 0.6275$. Closest: **(c) 0.63**.

## Do it cold · 3 (rare disease)

!!! exam "April 2024 · 1b · 0.25 p (and October 2021 · 1a · 0.5 p)"
    Apr 2024: the probability of having TB is 0.0005 and a test is 99 % accurate. What is the probability one has TB if one tests positive? Oct 2021: a virus has infected 1.8 % of a population; the test detects it 95 % of the time when present and gives a false positive 3 % of the time when absent. Probability that a positive person is infected? (a) 26 % (b) 37 % (c) 95 % (d) 92 %

???+ solution "Solution"
    **Apr 2024.** Sources: TB ($0.0005$) and no TB ($0.9995$). Rates of "+": $0.99$ and $0.01$. Forward: $0.0005\cdot0.99 + 0.9995\cdot0.01 = 0.000495 + 0.009995 = 0.01049$. Backward: $\frac{0.000495}{0.01049} = 0.0472$. A positive test means less than 5 % chance of TB: the false positives from the huge healthy group swamp the few true positives.

    **Oct 2021.** Forward: $0.018\cdot0.95 + 0.982\cdot0.03 = 0.0171 + 0.02946 = 0.04656$. Backward: $\frac{0.0171}{0.04656} = 0.367$: **(b) 37 %**.

    !!! answer "Answer"
        Apr 2024: $P(TB\mid+) = 0.047$. Oct 2021: 37 %.

## Do it cold · 4 (lifetime, conditional with a survival function)

!!! exam "April 2024 · 1a · 0.25 p"
    The lifetime $T$ (years) of a transducer satisfies $\Pr[T\ge t] = e^{-t/5}$. The transducer has worked for two years without problems. What is the probability that it breaks down in the third year, given that it was still working after 2 years? **Hint:** the third year is between $t = 2$ and $t = 3$. (a) 0.24 (b) 0.12 (c) 0.30 (d) 0.18

???+ solution "Solution"
    Given event: $T\ge2$, probability $e^{-2/5} = e^{-0.4} = 0.6703$. Asked event: $2\le T\le3$ (and it is inside the given event), probability $P(T\ge2) - P(T\ge3) = e^{-0.4} - e^{-0.6} = 0.6703 - 0.5488 = 0.1215$. Conditional: $\frac{0.1215}{0.6703} = 0.1813$. Shortcut (memoryless exponential): $1 - e^{-1/5} = 1 - 0.8187 = 0.1813$. **(d) 0.18**.

## Do it cold · 5 (Bayes as a plain MC, Jan 2022 1a · 0.3 p)

!!! exam "January 2022 resit · 1a"
    A company rates 75 % of its employees satisfactory (S) and 25 % unsatisfactory. 80 % of the satisfactory workers had previous experience (E); 15 % of the unsatisfactory workers had **no** experience. If a person with previous experience is hired, what is the probability that this person will be an unsatisfactory employee? (a) 0.24 (b) 0.25 (c) 0.26 (d) 0.28

???+ solution "Solution"
    Rates of E: $P(E\mid S) = 0.80$; $P(E\mid S^c) = 1 - 0.15 = 0.85$ (complement!). Forward: $0.80\cdot0.75 + 0.85\cdot0.25 = 0.60 + 0.2125 = 0.8125$. Backward: $\frac{0.2125}{0.8125} = 0.2615$: **(c) 0.26**.

## Do it cold · 6 (the 2-point version)

!!! exam "January 2020 retake · 2 · 2 p"
    Three painting machines: 85 % of cars painted by $M_1$ pass the quality test, 92 % for $M_2$, 60 % for $M_3$. Each day $M_1$ paints 30 cars, $M_2$ 45, $M_3$ 25. (a) Probability that a car passes? (b) Probability that a car that passed was painted by $M_3$?

???+ solution "Solution"
    Shares $\frac{30}{100}, \frac{45}{100}, \frac{25}{100}$. (a) $0.30\cdot0.85 + 0.45\cdot0.92 + 0.25\cdot0.60 = 0.255 + 0.414 + 0.150 = 0.819$. (b) $\frac{0.150}{0.819} = 0.1832$.

    !!! answer "Answer"
        (a) $0.819$. (b) $0.18$.

## Where points get lost

!!! trap key "Where points get lost"
    | Wrong line | Right line |
    |---|---|
    | $P(CT1) = 18$ | Shares are fractions: $18/55$. |
    | Using 0.85 when the question asks about images that do NOT pass | Complement per source: $1 - 0.85 = 0.15$. |
    | "15 % of unsatisfactory workers had no experience" used as $P(E\mid S^c) = 0.15$ | It is the complement: $P(E\mid S^c) = 0.85$. |
    | Backward answer $= P(B\mid A_k)$ (e.g. 0.04) | Bayes: product over the total, $0.014/0.0345$. |
    | $P(A\cap B) = 0$ as the meaning of independence | That is disjoint. Independence: $P(A\cap B) = P(A)P(B)$, i.e. $P(A\mid B) = P(A)$. |
    | Lifetime: answering $P(2\le T\le3) = 0.12$ | The "given" divides: $0.1215/0.6703 = 0.18$. |

## True or false (from real MC options)

<div class="tf" markdown>

| statement | T or F | why |
|---|---|---|
| If $A$ and $B$ are independent (nonzero probabilities), then $P(A\mid B) = P(A)$. | True | Jun 2026 1a (d). |
| If $A$ and $B$ are independent, then $P(A\cap B) = 0$. | False | Jun 2026 1a (c): that is disjointness; independent events with nonzero probability must intersect. |
| If $A$ and $B$ are independent, then $P(A\cup B) = P(A) + P(B)$. | False | Jun 2026 1a (a): the union rule needs $-P(A\cap B)$, which is $P(A)P(B)\ne0$. |
| There is a 50 % chance of rain here and 25 % on Mars, so 75 % that it rains here or on Mars. | False | Nov 2019 1b (B): $P(A\cup B) = P(A) + P(B) - P(A\cap B)$. |
| For discrete random variables the relative frequency tends to the PMF as the number of trials tends to infinity. | True | Nov 2019 1b (C). |

</div>

**You can leave this page when you can:**

- [ ] turn counts into shares and opposite rates into complements before computing anything.
- [ ] write the forward sum as separate products, then add.
- [ ] write the backward answer as one product over the sum and check all of them add to 1.
- [ ] state independence as $P(A\mid B) = P(A)$ and say why "$P(A\cap B) = 0$" is wrong.

*[total probability]: P(B) as the sum over sources of P(B | source) × P(source).
*[Bayes' theorem]: reversing a conditional probability: P(source | B) = P(B | source) P(source) / P(B).
*[complement]: the opposite event; its probability is 1 minus the original.
