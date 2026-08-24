#!/usr/bin/env bash
# Render a PDF twin of every SVG in assets/.
#
# PreTeXt resolves an <image> whose @source has no file extension to the .svg
# for HTML output and to the .pdf for LaTeX/print output, so each figure needs
# both files.  rsvg-convert ships in the pretextbook/pretext image used by the
# dev container and by CI, so this runs the same way in both places.
set -euo pipefail

cd "$(dirname "$0")/.."
shopt -s nullglob

for svg in assets/*.svg; do
  pdf="${svg%.svg}.pdf"
  rsvg-convert --format=pdf --output="$pdf" "$svg"
  echo "rendered $pdf"
done
