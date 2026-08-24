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
| `source/main.ptx` | Title, subtitle, and the order of the sections |
| `source/frontmatter.ptx` | Author block and the abstract (with the PDF link) |
| `source/course-info.ptx` | Course details, the two sections, office hours |
| `source/materials.ptx` | Textbook and lecture notes |
| `source/grading.ptx` | Course components and letter grades |
| `source/assignments.ptx` | Assignments and Gradescope submission |
| `source/schedule.ptx` | Fall 2026 calendar and important dates |
| `source/learning-objectives.ptx` | Overall goals and the 12 specific topics |
| `source/resources.ptx` | Mathematics Learning Center |
| `source/policies.ptx` | Preserving the course's integrity |
| `source/faq.ptx` | Frequently asked questions |
| `source/university-policies.ptx` | University policy statements |

Anything still to be filled in is marked with a `TODO` comment in the
source and shows up as "To be added" in the output.

Styling and output options (theme, chunking, PDF options) are in
`publication/publication.ptx`; build targets are in `project.ptx`.

## Figures

Illustrations live in `assets/`. PreTeXt resolves an `<image>` whose `@source`
has no file extension to the `.svg` for the website and to the `.pdf` for the
printable version, so each figure needs **both** files. `scripts/build-figures.sh`
renders the PDF twin of every SVG with `rsvg-convert`; the deploy workflow runs
it before each build, so the two never drift apart.

To swap in a picture of your own, either

- replace `assets/<name>.svg` and re-run `./scripts/build-figures.sh`, or
- drop in a `.png`/`.jpg` and give the `@source` the full filename, e.g.
  `<image source="my-picture.png">`.

Every `<image>` carries a `<shortdescription>` (the alt text) and a longer
`<description>`. Please keep both accurate when you change a figure.

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
