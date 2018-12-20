# -*- coding: utf-8 -*-
import math
import sys
import os
import re
import psMat
import fontforge
#import config

#fontforge.setPrefs('CoverageFormatsAllowed', 1)
# config
font_file_name = 'MiQglyph.otf'
font_name_en = 'MiQglyph'
font_name_ja = 'みQ文字'
font_version = '0.2'
font_style_en = 'Regular'
font_style_ja = '標準'
font_copyright = 'kazy111 <kazy@kazy111.info>'
font_license = 'MIT License'
font_designer = 'MiQ from WEAR'
font_sample_text = 'みＱてんばぶ！'

f = fontforge.font()
# set font names
f.em = 1000
f.fontname = font_name_en
f.familyname = font_name_en
f.fullname = font_name_en + '-' + font_style_en
f.weight = font_style_en
f.copyright = font_copyright
f.version = font_version

font_names = [
    ('English (US)', 'Copyright', f.copyright),
    ('English (US)', 'Family', font_name_en),
    ('Japanese', 'Family', font_name_ja),
    ('English (US)', 'SubFamily', font_style_en),
    ('Japanese', 'SubFamily', font_style_ja),
    ('English (US)', 'Fullname', font_name_en),
    ('Japanese', 'Fullname', font_name_ja),
    ('English (US)', 'Version', 'Version %s' % font_version),
    ('Japanese', 'Preferred Family', font_name_ja),
    ('English (US)', 'Preferred Family', font_name_en),
    ('Japanese', 'Preferred Styles', font_style_ja),
    ('English (US)', 'Preferred Styles', font_style_en),
    ('English (US)', 'License', font_license),
    ('Japanese', 'License', font_license),
    ('English (US)', 'Designer', font_designer),
    ('Japanese', 'Designer', font_designer),
    ('Japanese', 'Sample Text', font_sample_text),
]
f.sfnt_names = tuple(font_names)
f.hasvmetrics = 1

f.addLookup('gsubvert', 'gsub_single', (), (
	        ("vert", (("DFLT", ("dflt",)), ("latn", ("dflt",)), 
	                  ("kana", ("dflt",)), ("hani", ("dflt",))),),))
f.addLookupSubtable('gsubvert', "j-vert")

f.addLookup('gsubvrt2', 'gsub_single', (), (
	        ("vrt2", (("DFLT", ("dflt",)), ("latn", ("dflt",)), 
	                  ("kana", ("dflt",)), ("hani", ("dflt",))),),))
f.addLookupSubtable('gsubvrt2', "j-vrt2")

uni_glyph_pattern = re.compile(r'^u([0-9A-F]{4,5})$')
def get_glyph(name):
    if len(name) == 1 and ord(name) in f:
        return f[ord(name)]
    match = uni_glyph_pattern.match(name)
    if match:
        ucode = int(match.group(1), 16)
        if ucode in f:
            g = f[ucode]
        else:
            g = f.createChar(ucode)
    else:
        if name in f:
            g = f[name]
        else:
            g = f.createChar(-1, name)
    return g


def add_vert_substitute(codepoint):
    g = get_glyph(codepoint)
    g.addPosSub("j-vert", '%s.vert' % codepoint)
    g.addPosSub("j-vrt2", '%s.vert' % codepoint)

def import_svgs(target_path):
    if os.path.exists(target_path):
        files = os.listdir(target_path)
        for name in files:
            file_path = os.path.join(target_path, name)
            if not os.path.isfile(file_path):
                break
            splitted = name.split('.')
            if len(splitted) == 3:
                # tagged glyph
                g = get_glyph('%s.%s' % (splitted[0], splitted[1]))
                g.glyphname = '%s.%s' % (splitted[0], splitted[1])
                # add mapping
                if splitted[1] == 'vert':
                    add_vert_substitute(splitted[0])
            else:
                g = get_glyph(splitted[0])
            
            g.importOutlines(file_path)
            g.right_side_bearing = 60
            g.vwidth = 1000
            # fix outline direction
            g.correctDirection()
            # disable auto hinting
            g.manualHints = 1
            # round control point position to int
            g.round()

# import fonts
f.encoding = 'unicode'
g = get_glyph('u0000')
g.glyphname = '.notdef'
g.importOutlines("glyphs/.notdef.svg")
g.right_side_bearing = 60
g.vwidth = 1000

import_svgs('glyphs/digits')
import_svgs('glyphs/alphabets')
import_svgs('glyphs/symbols')
import_svgs('glyphs/hiraganas')
import_svgs('glyphs/katakanas')
import_svgs('glyphs/kanjis')


# * individual setting
#/ space
get_glyph('u0020').right_side_bearing = 425
# space (full-width)
get_glyph('u3000').right_side_bearing = 850
# 、
get_glyph('u3001').right_side_bearing = 400
# 。
get_glyph('u3002').right_side_bearing = 400
# 「(full-width)
get_glyph('u300c').right_side_bearing = 0
# ！(full-width)
get_glyph('uff01').right_side_bearing = 100
# ) (full-width)
get_glyph('uff09').right_side_bearing = 400
# A
get_glyph('u0041').right_side_bearing = 0
# I
get_glyph('u0049').right_side_bearing = 60
# a
get_glyph('u0061').right_side_bearing = 5
# c
get_glyph('u0063').right_side_bearing = 0
# i
get_glyph('u0069').right_side_bearing = 150
# l
get_glyph('u006c').right_side_bearing = 140
# w
get_glyph('u0077').right_side_bearing = 0
# ォ
get_glyph('u30a9').right_side_bearing = 100
# ル
get_glyph('u30eb').right_side_bearing = 0



# * save
f.save(os.path.splitext(font_file_name)[0] + '.sfd')
f.generate(font_file_name)

f.close()
