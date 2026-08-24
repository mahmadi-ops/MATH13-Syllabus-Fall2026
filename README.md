# MATH 13 Syllabus — Fall 2026

Syllabus for MATH 13 (Fall 2026, Santa Clara University), authored in
[PreTeXt](https://pretextbook.org) and published automatically to GitHub Pages
in two formats:

- **Accessible website:** https://mahmadi-ops.github.io/MATH13-Syllabus-Fall2026/
- **Printable PDF:** https://mahmadi-ops.github.io/MATH13-Syllabus-Fall2026/math13-syllabus-fall2026.pdf

## How it works

Every push to `main` triggers the GitHub Actions workflow in
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), which builds
both the HTML and PDF versions with the PreTeXt CLI and deploys them to
GitHub Pages. Nothing needs to be built or committed by hand.

**One-time setup:** in the repository settings on GitHub, go to
*Settings → Pages* and set **Source** to **GitHub Actions** before (or right
after) the first push.

## Editing the syllabus

All content lives in `source/`:

| File | Section |
| --- | --- |
| `source/main.ptx` | Title, subtitle, and overall structure |
| `source/frontmatter.ptx` | Instructor info and the abstract (with PDF link) |
| `source/course-info.ptx` | Meeting times, office hours, prerequisites |
| `source/learning-objectives.ptx` | Learning objectives |
| `source/materials.ptx` | Textbook and materials |
| `source/grading.ptx` | Grade breakdown and grading policies |
| `source/schedule.ptx` | Tentative weekly schedule |
| `source/policies.ptx` | Attendance, late work, academic integrity |
| `source/resources.ptx` | Accommodations and campus resources |

Placeholders are marked with `TODO` comments and `[bracketed]` text.
Styling and output options (theme, chunking, PDF options) are in
`publication/publication.ptx`; build targets are in `project.ptx`.

## Building locally (optional)

Install the CLI once with `pip install -r requirements.txt`, then:

- `pretext build web` — build the HTML version
- `pretext view web` — preview it in a browser
- `pretext build print` — build the PDF (requires a LaTeX installation,
  e.g. [MacTeX](https://www.tug.org/mactex/); otherwise just let the GitHub
  Action build it)

## Accessibility

PreTeXt's HTML output is designed for accessibility: semantic structure,
keyboard navigation, and math rendered by MathJax with screen-reader support.
To keep the document accessible as you edit:

- Give every `<image>` a `<description>` (alt text).
- Keep the first row of each `<tabular>` marked with `header="yes"`.
- Use meaningful link text (avoid "click here").
