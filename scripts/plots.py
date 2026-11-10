"""Regenerate every SVG figure of the guide into docs/img/. Run: python scripts/plots.py"""
import os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "img")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
BLUE, RED, INK = "#1f5fae", "#b8321f", "#222"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), format="svg")
    plt.close(fig)


def two_pdfs(name, x, p0, p1, th, h1_right, xlabel="y", labels=("$p(y;H_0)$", "$p(y;H_1)$"), extra=None):
    """Solid p0, dashed p1, threshold line(s), shade P_FA (p0 on H1 side, blue) and P_M (p1 on H0 side, red)."""
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    ax.plot(x, p0, color=INK, lw=1.8, label=labels[0])
    ax.plot(x, p1, color=INK, lw=1.8, ls="--", label=labels[1])
    ths = th if isinstance(th, (list, tuple)) else [th]
    for t in ths:
        ax.axvline(t, color="#777", lw=1, ls=":")
    if callable(h1_right):
        h1 = h1_right(x)
    else:
        h1 = (x > ths[0]) if h1_right else (x < ths[0])
        if len(ths) == 2:
            h1 = (x > ths[1]) | (x < ths[0])
    ax.fill_between(x, 0, p0, where=h1, color=BLUE, alpha=.35, label="$P_{FA}$")
    ax.fill_between(x, 0, p1, where=~h1, color=RED, alpha=.3, label="$P_M$")
    ax.set_xlabel(xlabel); ax.set_ylabel("pdf"); ax.set_ylim(bottom=0)
    ax.legend(frameon=False, fontsize=8)
    if extra:
        extra(ax)
    save(fig, name)


# ---------------- U17 ----------------
y = np.linspace(0, 5, 600)
two_pdfs("u17_apr24_4b.svg", y, norm.pdf(y), .25 * np.exp(-y / 2), 1.5884, True,
         extra=lambda ax: ax.annotate("$y_{th}=1.59$", (1.6, .3), fontsize=8))
y = np.linspace(-5, 5, 800)
two_pdfs("u17_jan22_4b.svg", y, norm.pdf(y), .25 * np.exp(-np.abs(y) / 2), [-1.5884, 1.5884], True)
y = np.linspace(0, 5, 600)
two_pdfs("u17_nov22_4d.svg", y, np.exp(-y), 2 * np.exp(-2 * y), 1.0, False)
x = np.linspace(0, 6, 600)
two_pdfs("u17_jan20_5a.svg", x, .1 * np.exp(-.1 * x), 2 * np.exp(-2 * x), 1.5767, False, xlabel="x",
         extra=lambda ax: ax.set_ylim(0, 1.0))
x = np.linspace(-6, 6, 800)
two_pdfs("u17_nov19_4a.svg", x, norm.pdf(x, 0, 1), norm.pdf(x, 0, 3), [-3, 3], True, xlabel="x")

# ROC jan20 5c
fig, ax = plt.subplots(figsize=(4.2, 4))
pfa = np.linspace(1e-4, 1, 400)
for l1, lab in [(2.1855, "$\\lambda_1=2.19$"), (6, "larger $\\lambda_1$"), (0.5, "smaller $\\lambda_1$")]:
    xth = -np.log(1 - pfa) / .1
    ax.plot(pfa, 1 - np.exp(-l1 * xth), label=lab)
ax.plot([0, 1], [0, 1], ls=":", color="#777"); ax.plot([.1, .5, .9], [.9, 1, 1], "o", color=INK)
ax.set_xlabel("$P_{fa}$"); ax.set_ylabel("$P_d$"); ax.legend(frameon=False, fontsize=8)
save(fig, "u17_jan20_5c.svg")

# ROC oct21 4a
fig, ax = plt.subplots(figsize=(4.2, 4))
th = np.linspace(-4, 5, 400)
for mu in (1, 2):
    ax.plot(norm.sf(th), norm.sf(th - mu), label=f"$\\mu={mu}$")
    pts = [-1, 0, 1, 2, 3]
    ax.plot([norm.sf(t) for t in pts], [norm.sf(t - mu) for t in pts], "o", color=INK, ms=4)
ax.plot([0, 1], [0, 1], ls=":", color="#777")
ax.set_xlabel("$P_{fa}$"); ax.set_ylabel("$P_d$"); ax.legend(frameon=False, fontsize=8)
save(fig, "u17_oct21_roc.svg")

print("ok", len(os.listdir(OUT)), "files in", OUT)
