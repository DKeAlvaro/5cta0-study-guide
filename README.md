# Study guide template

MkDocs Material template for a "pass the exam" guide: lesson pages with exam/solution/trap/recipe boxes, KaTeX maths, step-by-step reveals, true/false cards, progress bar, collapsible nav, dark mode, and an optional AI tutor panel (reader's own API key).

Derived from [5cta0-exam-guide](https://github.com/DKeAlvaro/5cta0-exam-guide), with all course content removed.

## Use it

```bash
pip install mkdocs==1.6.1 mkdocs-material==9.7.7 pymdown-extensions==12.3
mkdocs serve        # http://127.0.0.1:8000
```

1. Edit `mkdocs.yml`: `site_name`, `site_url`, `repo_url`, `repo_name`, and `nav` (one entry per `.md` in `docs/`).
2. Put your `.md` files in `docs/`. `docs/example-lesson.md` shows every box and widget; `STYLE.md` is the writing checklist.
3. Set the course name in `docs/javascripts/ask.js` (`SUBJECT`) for the AI tutor.
4. Push to `master`; `.github/workflows/deploy.yml` publishes to GitHub Pages (enable Pages from the `gh-pages` branch).

Custom figures: add `W.name = (root, preset) => {...}` in `docs/javascripts/widgets.js`, use with `<div class="widget" data-w="name"></div>`.
