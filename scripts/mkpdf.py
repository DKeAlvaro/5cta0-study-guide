"""Build the site and print docs/cheatsheet.md to cheatsheet.pdf with headless Chrome.
Usage: python scripts/mkpdf.py [--scale 0.95] [--no-build] [--out path]
The sheet is extracted from site/cheatsheet.html into a standalone page (site/cheatsheet-print.html) with only
KaTeX and the print stylesheet, served over HTTP (KaTeX does not render from file://), and printed.
Prints the page count and, per page, how full each of the three columns is."""
import argparse, functools, http.server, os, re, shutil, subprocess, sys, threading
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site")
CHROME = next((p for p in [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    shutil.which("google-chrome") or "", shutil.which("chromium") or ""] if p and os.path.exists(p)), None)

KATEX = "https://unpkg.com/katex@0.16.11/dist/"
PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>5CTA0 cheat sheet</title>
<link rel="stylesheet" href="{katex}katex.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="stylesheets/cheat-print.css">
<style>
body {{ margin: 0; font-family: "Source Serif 4", Georgia, serif; }}
.md-typeset {{ font-size: 8pt; line-height: 1.15; }}
.md-typeset p, .md-typeset ul, .md-typeset ol {{ margin: .1em 0; }}
.md-typeset h1, .md-typeset h2, .md-typeset h3 {{ font-family: "Source Serif 4", Georgia, serif; font-weight: 700; }}
.md-typeset table {{ border-collapse: collapse; }}
.md-typeset code {{ font-family: Consolas, monospace; font-size: .9em; }}
</style>
<script defer src="{katex}katex.min.js"></script>
<script defer src="{katex}contrib/auto-render.min.js"></script>
<script>window.addEventListener("DOMContentLoaded", function () {{
  function go() {{ if (!window.renderMathInElement) return setTimeout(go, 50);
    renderMathInElement(document.body, {{ delimiters: [
      {{ left: "$$", right: "$$", display: true }}, {{ left: "$", right: "$", display: false }},
      {{ left: "\\\\(", right: "\\\\)", display: false }}, {{ left: "\\\\[", right: "\\\\]", display: true }} ], throwOnError: false }});
    document.body.dataset.ready = "1"; }}
  go(); }});</script>
</head><body><div class="md-typeset">{body}</div></body></html>"""


def build():
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "-q"], cwd=ROOT, check=True)


def extract_sheet():
    html = open(os.path.join(SITE, "cheatsheet.html"), encoding="utf-8").read()
    start = html.index('<div class="cheat"')
    # walk to the matching closing div
    depth, i = 0, start
    while True:
        m = re.compile(r"<div\b|</div>").search(html, i)
        if m.group(0).startswith("<div"):
            depth += 1
        else:
            depth -= 1
        i = m.end()
        if depth == 0:
            break
    body = html[start:i]
    out = os.path.join(SITE, "cheatsheet-print.html")
    open(out, "w", encoding="utf-8").write(PAGE.format(katex=KATEX, body=body))
    return out


def print_pdf(out):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=SITE)
    handler.log_message = lambda *a, **k: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{port}/cheatsheet-print.html"
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=30000", f"--print-to-pdf={out}", url]
    subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True, timeout=180)
    srv.shutdown()


def set_scale(scale):
    css = os.path.join(ROOT, "docs", "stylesheets", "cheat-print.css")
    s = open(css, encoding="utf-8").read()
    s = re.sub(r"--cheat-scale:\s*[\d.]+", f"--cheat-scale: {scale}", s)
    open(css, "w", encoding="utf-8").write(s)


def measure(pdf, cols=3):
    import fitz
    doc = fitz.open(pdf)
    print(f"pages: {len(doc)}")
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=50, colorspace=fitz.csGRAY)
        a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
        ink = a < 200
        w = pix.width // cols
        fills = []
        for c in range(cols):
            r = np.where(ink[:, c * w + 4:(c + 1) * w - 4].any(axis=1))[0]
            fills.append((r.max() - r.min()) / pix.height if len(r) else 0)
        print(f"page {i + 1}: column fill " + ", ".join(f"{f:.0%}" for f in fills))
    return len(doc)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", type=float, default=None, help="CSS zoom for the printed sheet (stored in cheat-print.css)")
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--out", default=os.path.join(ROOT, "cheatsheet.pdf"))
    a = ap.parse_args()
    if not CHROME:
        sys.exit("Chrome not found")
    if a.scale:
        set_scale(a.scale)
    if not a.no_build:
        build()
    extract_sheet()
    print_pdf(a.out)
    measure(a.out)
    print("wrote", a.out)
