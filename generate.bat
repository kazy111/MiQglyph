SET FF_EXE="C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe"

%FF_EXE% -script scripts/generate.pe
del MiQglyph.ttx
ttx MiQglyph.otf
del MiQglyph.otf
node scripts/fix_tsb.js
ttx MiQglyph.ttx
