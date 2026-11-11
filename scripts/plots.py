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

# ---------------- Part 3: PSD plots ----------------
th = np.linspace(-np.pi, np.pi, 721)


def psd_plot(name, curves, ylim=None, ylabel="PSD"):
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    styles = ["-", "--", ":", "-."]
    for (lab, f), st in zip(curves, styles):
        ax.plot(th, f(th), st, color=INK, lw=1.8, label=lab)
    ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
    ax.set_xticklabels([r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    ax.set_xlabel(r"$\theta$"); ax.set_ylabel(ylabel); ax.axhline(0, color="#999", lw=.6)
    if ylim: ax.set_ylim(*ylim)
    ax.legend(frameon=False, fontsize=8)
    save(fig, name)


def ar_psd(sig, a):
    return lambda t: sig / np.abs(1 + sum(ak * np.exp(-1j * (k + 1) * t) for k, ak in enumerate(a))) ** 2


psd_plot("u11_jun26_3c.svg", [("correlogram", lambda t: 3 + 4 * np.cos(t) + 2 * np.cos(2 * t))])
psd_plot("u12_jun26_3d.svg", [("correlogram", lambda t: 3 + 4 * np.cos(t) + 2 * np.cos(2 * t)), ("AR(2)", ar_psd(1.6, [-0.8, 0.2]))])
psd_plot("u12_apr25.svg", [("correlogram", lambda t: 2 - .5 * np.cos(t) - .375 * np.cos(2 * t)), ("AR(1)", ar_psd(63 / 32, [1 / 8])),
                           ("MA(1)", lambda t: 2 - .5 * np.cos(t))], ylim=(0, 3))
psd_plot("u12_apr24.svg", [("correlogram", lambda t: 25 / 16 - 1.5 * np.cos(t) + np.cos(2 * t) - np.cos(3 * t)), ("AR(2)", ar_psd(9129 / 7696, [204 / 481, -56 / 481]))])
psd_plot("u12_nov19.svg", [("correlogram", lambda t: 1 + 1.4 * np.cos(t) + np.cos(2 * t) + .6 * np.cos(3 * t)), ("AR(2)", ar_psd(0.5098, [-0.6863, -0.0196]))])
psd_plot("u13_jan20.svg", [("correlogram = MA(1)", lambda t: 1 / 21 + 4 / 105 * np.cos(t))])
psd_plot("u14_nov22.svg", [("ARMA(1,1) true PSD", lambda t: 28 * (1 - np.cos(t)) / (25 - 24 * np.cos(t))), ("AR(1) fit", ar_psd(63 / 64, [1 / 8])),
                           ("MA(1) fit", lambda t: 1 - .25 * np.cos(t))])
print("ok part3")

# ---------------- U15: FTD vs DFT with and without zero padding (Jan 2022 3a) ----------------
fs, f0, N = 50.0, 25.0, 24
fig, ax = plt.subplots(figsize=(6.4, 3.4))
fgrid = np.linspace(-fs / 2, fs / 2, 2001)
w = 2 * np.pi * fgrid / fs
n = np.arange(N)
X = np.array([np.sum(20 * np.cos(2 * np.pi * f0 / fs * n) * np.exp(-1j * wk * n)) for wk in w]) / N * 2  # FTD of windowed, scaled to peak 10
ax.plot(fgrid, np.abs(X) / 2, "--", color="#6a3d9a", lw=1.4, label="D: FTD of windowed $\\tilde x[n]$")
ax.vlines([-f0, f0], 0, 10, color="#e07b00", lw=2.5, label="B: FTD of $x[n]$ (two lines)")
for L, mk, lab, col in [(36, "o", "C: DFT, $N=24$, 12 zeros padded", "#c9a800"), (24, "s", "A: DFT, $N=24$, no padding", BLUE)]:
    k = np.arange(L); fk = (k - L // 2) * fs / L
    xp = np.concatenate([20 * np.cos(2 * np.pi * f0 / fs * n), np.zeros(L - N)])
    Xk = np.fft.fftshift(np.fft.fft(xp)) / N * 2 / 2
    ax.plot(fk, np.abs(Xk), mk, color=col, ms=5, mfc="none", label=lab)
ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("magnitude"); ax.set_xlim(-fs / 2, fs / 2); ax.set_ylim(0, 11)
ax.legend(frameon=False, fontsize=7.5)
save(fig, "u15_jan22_3a.svg")

# ---------------- U15: window shapes and spectra ----------------
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0))
M = 32; nn = np.arange(M)
wins = {"rectangular": np.ones(M), "triangular": 1 - np.abs((nn - (M - 1) / 2) / ((M - 1) / 2)), "Hanning": 0.5 - 0.5 * np.cos(2 * np.pi * nn / (M - 1))}
for (lab, wv), st in zip(wins.items(), ["-", "--", ":"]):
    a1.plot(nn, wv, st, color=INK, label=lab)
    W = np.abs(np.fft.fftshift(np.fft.fft(wv, 1024))); W = 20 * np.log10(W / W.max() + 1e-9)
    a2.plot(np.linspace(-np.pi, np.pi, 1024), W, st, color=INK, label=lab)
a1.set_xlabel("n"); a1.set_ylabel("w[n]"); a1.legend(frameon=False, fontsize=7)
a2.set_xlabel(r"$\theta$"); a2.set_ylabel("|W| (dB)"); a2.set_ylim(-80, 2); a2.set_xlim(-1.2, 1.2)
save(fig, "u15_windows.svg")
print("ok u15")
