#!/usr/bin/env python3
"""Posting Desk row maintenance for the posted-materials table.

Usage: desk_row.py add    <label> <url> [due]
       desk_row.py remove <label>

`add` inserts a new row (today's date, Pacific time) directly below the
NEW ROWS GO DIRECTLY BELOW comment in source/updates.ptx; a row whose
link already carries the same label is left alone. `remove` deletes the
one row whose link label matches exactly. Exit 0 always means the table
is now in the requested state.
"""
import re
import sys
from datetime import datetime
from xml.etree import ElementTree as ET

try:
    from zoneinfo import ZoneInfo
    NOW = datetime.now(ZoneInfo("America/Los_Angeles"))
except Exception:
    NOW = datetime.now()

PATH = "source/updates.ptx"
MARKER = "NEW ROWS GO DIRECTLY BELOW"


def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    op, label = sys.argv[1], sys.argv[2]
    with open(PATH, encoding="utf-8") as f:
        text = f.read()

    if op == "add":
        if len(sys.argv) < 4:
            sys.exit("add needs a url")
        url, due = sys.argv[3], (sys.argv[4] if len(sys.argv) > 4 else "")
        if ">%s</url>" % xml_escape(label) in text:
            print("row for %r already present" % label)
            return
        idx = text.find(MARKER)
        if idx < 0:
            sys.exit("marker comment not found in %s" % PATH)
        insert_at = text.find("-->", idx)
        if insert_at < 0:
            sys.exit("malformed marker comment")
        insert_at = text.index("\n", insert_at) + 1
        due_cell = "<cell>%s</cell>" % xml_escape(due) if due else "<cell><mdash/></cell>"
        row = (
            "      <row>\n"
            "        <cell>%s</cell>\n"
            '        <cell><url href="%s">%s</url></cell>\n'
            "        %s\n"
            "      </row>\n"
        ) % (NOW.strftime("%b %-d, %Y"), xml_escape(url), xml_escape(label), due_cell)
        text = text[:insert_at] + row + text[insert_at:]
        print("added row for %r" % label)
    elif op == "remove":
        pat = re.compile(
            r"\n[ \t]*<row>\s*<cell>[^<]*</cell>\s*<cell><url href=\"[^\"]*\">"
            + re.escape(xml_escape(label))
            + r"</url></cell>\s*<cell>.*?</cell>\s*</row>",
            re.S,
        )
        if not pat.search(text):
            print("no row for %r; nothing to remove" % label)
            return
        text = pat.sub("", text, count=1)
        print("removed row for %r" % label)
    else:
        sys.exit("unknown op %r" % op)

    ET.fromstring(text)  # refuse to write anything that no longer parses
    with open(PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
