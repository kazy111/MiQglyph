#!/bin/sh
rm MiQglyph.*

python scripts/generate.py
ttx MiQglyph.otf
rm MiQglyph.otf
python scripts/fix_tsb.py
ttx MiQglyph.ttx
rm MiQglyph.ttx
