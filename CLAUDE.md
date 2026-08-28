# Claude workflow — MATH 13 Syllabus (Fall 2026)

PreTeXt article, published automatically on every push to `main`:

- Website: https://mahmadi-ops.github.io/MATH13-Syllabus-Fall2026/
- PDF: https://mahmadi-ops.github.io/MATH13-Syllabus-Fall2026/math13-syllabus-fall2026.pdf

Do **not** reorganize the sections, rename files, or restructure the article.
Routine work in this repo is limited to the one job below unless the
instructor asks for something else.

## The "Posted Notes and Assignments" table

`source/updates.ptx` holds the last section of the syllabus: a table that
logs every piece of course material as it is posted. It is the companion of
the course-notes repo `mahmadi-ops/M13-Mehdi` (published at
https://mahmadi-ops.github.io/M13-Mehdi/), whose `CLAUDE.md` defines the
posting workflow (`/post-notes`, `/post-assignment`, `/release-solutions`)
and the click-to-post Posting Desk panel (see "The Posting Desk" in that
`CLAUDE.md`). Whenever material is posted there, add a row **here**. For
panel-initiated postings the instructor has authorized committing directly
to `main`; everything else follows the session's normal branch rules.

Rules for adding a row:

1. Insert the new `<row>` directly below the `NEW ROWS GO DIRECTLY BELOW`
   comment in `source/updates.ptx`, so the table stays newest-first. Never
   delete or reorder existing rows. Row templates are inside that comment.
2. **Date posted**: today's date, formatted like `Sep 25, 2026`.
3. **Item**: a `<url>` link to the exact page of the notes site
   (`https://mahmadi-ops.github.io/M13-Mehdi/<xml-id-of-section>.html` —
   verify the filename against a build of that repo, or link to the site
   root if unsure). Label it `Notes: <topic>`, `Assignment <n>`, or
   `Solutions: Assignment <n>`.
4. **Due date**: required for assignments (e.g. `Fri Oct 2, 11:59 PM` —
   assignments are due Fridays, but Wednesday in exam weeks 3, 6, 9; see
   `source/assignments.ptx`). For notes use `<mdash/>`; for solutions use
   `was due <date>`.
5. Keep the first row of the tabular marked `header="yes"` and keep every
   `<url>` label meaningful (no "click here").
6. Check well-formedness (`xmllint --noout source/updates.ptx`), then commit
   with a message like `Log Assignment 3 in the posted-materials table` and
   push to the branch designated for the session. Publishing happens when
   the change reaches `main`.
