del MiQglyph.*

ffpython scripts/generate.py
ttx MiQglyph.otf
del MiQglyph.otf
node scripts/fix_tsb.js
ttx MiQglyph.ttx
del MiQglyph.ttx
