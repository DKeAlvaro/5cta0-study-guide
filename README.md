# 5CTA0 · pass the exam

Active, from-zero study guide and cheat sheet for **5CTA0 Statistical Signal Processing (TU/e)**, built from every past exam in the course folder (January 2019 to June 2026). Published at https://dkealvaro.github.io/5cta0-study-guide/ (GitHub Pages from `gh-pages`, deployed by `.github/workflows/deploy.yml` on every push to `master`).

- `docs/inventory.md`: every exam question, grouped into 19 question types, ranked by points × frequency × difficulty.
- `docs/maths.md`: the maths the course assumes, taught from zero.
- `docs/u01-*.md` … `docs/u19-*.md`: one page per question type. Order inside a page: idea in plain words → tiny numeric example → formula with every symbol named → "IF YOU SEE" exam wording → recipe → one exam question in a stepper (do each step before revealing) → "Do it cold" questions → traps → true/false cards → exit checklist.
- `docs/cheatsheet.md`: the two A4 sides allowed in the exam, same U1–U19 numbering. `scripts/mkpdf.py` prints it to `cheatsheet.pdf` (headless Chrome; the sheet is extracted into a standalone page because KaTeX does not render from `file://`) and reports the page count and column fill. Print the PDF at 100 %.
- `docs/battle.md`: every past question → which sheet box → how → answer.
- `scripts/verify.py`: recomputes every number in the guide (numpy / sympy / scipy) and prints PASS/FAIL per question.
- `scripts/plots.py`: regenerates every figure (`docs/img/*.svg`).

```bash
pip install mkdocs==1.6.1 mkdocs-material==9.7.7 pymdown-extensions==12.3 numpy scipy sympy matplotlib pymupdf
python scripts/plots.py && python scripts/verify.py && mkdocs build   # zero warnings expected
python scripts/mkpdf.py            # cheatsheet.pdf, 2 pages
mkdocs serve                       # http://127.0.0.1:8000
```

Template: [DKeAlvaro/study-guide-template](https://github.com/DKeAlvaro/study-guide-template). Writing rules in `STYLE.md`.
