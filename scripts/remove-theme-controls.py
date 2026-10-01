#!/usr/bin/env python3
"""Remove SmartGen's optional theme controls from the generated site.

The API Playground theme ships reusable theme-control markup even when the
configuration disables style switching. This post-build step removes the
interactive controls while leaving the configured API Playground theme intact.
"""
from pathlib import Path
import re
import sys

site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
patterns = [
    re.compile(r'\s*<div class="theme-switcher" id="theme-switcher">.*?</div>\s*</div>', re.S),
    re.compile(r'\s*<div class="style-switcher" id="style-switcher">.*?</div>\s*</div>', re.S),
]

for html in site.rglob("*.html"):
    text = html.read_text(encoding="utf-8")
    updated = text
    for pattern in patterns:
        updated = pattern.sub("", updated)
    if updated != text:
        html.write_text(updated, encoding="utf-8")
