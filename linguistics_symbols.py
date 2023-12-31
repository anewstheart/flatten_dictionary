
PARTS_OF_SPEECH = ['noun', 'verb', 'name', 'adj', 'num', 'suffix', 'adv', 'conj', 'particle', 
                   'intj', 'pron', 'prep', 'contraction', 'symbol', 'prefix', 'phrase', 
                   'character', 'infix', 'det', 'interfix', 'proverb']

# ¯ (Macron): Indicates vowel length.
# ̌ (Caron): Represents rising or falling tone.
# ̂ (Circumflex): Marks a higher or more central vowel quality.
# ́ (Acute Accent): Denotes word stress.
# ̀ (Grave Accent): Represents a low or open vowel quality.
# ̆ (Breve): Indicates a short or reduced vowel.
# ̇ (Dot Above): Represents nasalization.
# ̏ (Double Acute): Marks a long and stressed vowel.
# ̋ (Double Grave): Denotes a low or open vowel with nasalization.
# ̑ (Inverted Breve): Indicates a short or reduced vowel with nasalization.

CROATIAN_DIACRITIC_NOTATION_CHARACTERS = [
    '\u0061\u0304',  # ā (LATIN SMALL LETTER A + COMBINING MACRON)
    '\u0061\u030c',  # ǎ (LATIN SMALL LETTER A + COMBINING CARON)
    '\u0061\u0302',  # â (LATIN SMALL LETTER A + COMBINING CIRCUMFLEX)
    '\u0061\u0301',  # á (LATIN SMALL LETTER A + COMBINING ACUTE ACCENT)
    '\u0061\u0300',  # à (LATIN SMALL LETTER A + COMBINING GRAVE ACCENT)
    '\u0061\u0306',  # ă (LATIN SMALL LETTER A + COMBINING BREVE)
    '\u0061\u0307',  # ȧ (LATIN SMALL LETTER A + COMBINING DOT ABOVE)
    '\u0061\u030f',  # ȁ (LATIN SMALL LETTER A + COMBINING DOUBLE ACUTE ACCENT)
    '\u0061\u030b',  # a̋ (LATIN SMALL LETTER A + COMBINING DOUBLE GRAVE ACCENT)
    '\u0061\u0311',  # ȃ (LATIN SMALL LETTER A + COMBINING INVERTED BREVE)

    '\u0065\u0304',  # ē (LATIN SMALL LETTER E + COMBINING MACRON)
    '\u0065\u030c',  # ě (LATIN SMALL LETTER E + COMBINING CARON)
    '\u0065\u0302',  # ê (LATIN SMALL LETTER E + COMBINING CIRCUMFLEX)
    '\u0065\u0301',  # é (LATIN SMALL LETTER E + COMBINING ACUTE ACCENT)
    '\u0065\u0300',  # è (LATIN SMALL LETTER E + COMBINING GRAVE ACCENT)
    '\u0065\u0306',  # ĕ (LATIN SMALL LETTER E + COMBINING BREVE)
    '\u0065\u0307',  # ė (LATIN SMALL LETTER E + COMBINING DOT ABOVE)
    '\u0065\u030f',  # ȅ (LATIN SMALL LETTER E + COMBINING DOUBLE ACUTE ACCENT)
    '\u0065\u030b',  # e̋ (LATIN SMALL LETTER E + COMBINING DOUBLE GRAVE ACCENT)
    '\u0065\u0311',  # ȇ (LATIN SMALL LETTER E + COMBINING INVERTED BREVE)

    '\u0069\u0304',  # ī (LATIN SMALL LETTER I + COMBINING MACRON)
    '\u0069\u030c',  # ǐ (LATIN SMALL LETTER I + COMBINING CARON)
    '\u0069\u0302',  # î (LATIN SMALL LETTER I + COMBINING CIRCUMFLEX)
    '\u0069\u0301',  # í (LATIN SMALL LETTER I + COMBINING ACUTE ACCENT)
    '\u0069\u0300',  # ì (LATIN SMALL LETTER I + COMBINING GRAVE ACCENT)
    '\u0069\u0306',  # ĭ (LATIN SMALL LETTER I + COMBINING BREVE)
    '\u0069\u0307',  # i̇ (LATIN SMALL LETTER I + COMBINING DOT ABOVE)
    '\u0069\u030f',  # ȉ (LATIN SMALL LETTER I + COMBINING DOUBLE ACUTE ACCENT)
    '\u0069\u0311',  # ȋ (LATIN SMALL LETTER I + COMBINING INVERTED BREVE)
    
    '\u006f\u0311',  # ȏ (LATIN SMALL LETTER O + COMBINING INVERTED BREVE)
    '\u006f\u0304',  # ō (LATIN SMALL LETTER O + COMBINING MACRON)
    '\u006f\u030c',  # ǒ (LATIN SMALL LETTER O + COMBINING CARON)
    '\u006f\u0302',  # ô (LATIN SMALL LETTER O + COMBINING CIRCUMFLEX)
    '\u006f\u0301',  # ó (LATIN SMALL LETTER O + COMBINING ACUTE ACCENT)
    '\u006f\u0300',  # ò (LATIN SMALL LETTER O + COMBINING GRAVE ACCENT)
    '\u006f\u0306',  # ŏ (LATIN SMALL LETTER O + COMBINING BREVE)
    '\u006f\u0307',  # ȯ (LATIN SMALL LETTER O + COMBINING DOT ABOVE)
    '\u006f\u030f',  # ȍ (LATIN SMALL LETTER O + COMBINING DOUBLE ACUTE ACCENT)
    '\u006f\u030b',  # ő (LATIN SMALL LETTER O + COMBINING DOUBLE GRAVE ACCENT)

    '\u0072\u0304',  # r̄ (LATIN SMALL LETTER R + COMBINING MACRON)
    '\u0072\u030c',  # ř (LATIN SMALL LETTER R + COMBINING CARON)
    '\u0072\u0302',  # r̂ (LATIN SMALL LETTER R + COMBINING CIRCUMFLEX)
    '\u0072\u0301',  # ŕ (LATIN SMALL LETTER R + COMBINING ACUTE ACCENT)
    '\u0072\u0300',  # r̀ (LATIN SMALL LETTER R + COMBINING GRAVE ACCENT)
    '\u0072\u0306',  # r̆ (LATIN SMALL LETTER R + COMBINING BREVE)
    '\u0072\u0307',  # ṙ (LATIN SMALL LETTER R + COMBINING DOT ABOVE)
    '\u0072\u030f',  # ȑ (LATIN SMALL LETTER R + COMBINING DOUBLE ACUTE ACCENT)
    '\u0072\u030b',  # r̋ (LATIN SMALL LETTER R + COMBINING DOUBLE GRAVE ACCENT)
    '\u0072\u0311',  # ȓ (LATIN SMALL LETTER R + COMBINING INVERTED BREVE)

    '\u0075\u0304',  # ū (LATIN SMALL LETTER U + COMBINING MACRON)
    '\u0075\u030c',  # ǔ (LATIN SMALL LETTER U + COMBINING CARON)
    '\u0075\u0302',  # û (LATIN SMALL LETTER U + COMBINING CIRCUMFLEX)
    '\u0075\u0301',  # ú (LATIN SMALL LETTER U + COMBINING ACUTE ACCENT)
    '\u0075\u0300',  # ù (LATIN SMALL LETTER U + COMBINING GRAVE ACCENT)
    '\u0075\u0306',  # ŭ (LATIN SMALL LETTER U + COMBINING BREVE)
    '\u0075\u0307',  # u̇ (LATIN SMALL LETTER U + COMBINING DOT ABOVE)
    '\u0075\u030f',  # ȕ (LATIN SMALL LETTER U + COMBINING DOUBLE ACUTE ACCENT)
    '\u0075\u030b',  # ű (LATIN SMALL LETTER U + COMBINING DOUBLE GRAVE ACCENT)
    '\u0075\u0311',  # ȗ (LATIN SMALL LETTER U + COMBINING INVERTED BREVE)

    '\u0041\u0304',  # Ā (LATIN CAPITAL LETTER A + COMBINING MACRON)
    '\u0041\u030c',  # Ǎ (LATIN CAPITAL LETTER A + COMBINING CARON)
    '\u0041\u0302',  # Â (LATIN CAPITAL LETTER A + COMBINING CIRCUMFLEX)
    '\u0041\u0301',  # Á (LATIN CAPITAL LETTER A + COMBINING ACUTE ACCENT)
    '\u0041\u0300',  # À (LATIN CAPITAL LETTER A + COMBINING GRAVE ACCENT)
    '\u0041\u0306',  # Ă (LATIN CAPITAL LETTER A + COMBINING BREVE)
    '\u0041\u0307',  # Ȧ (LATIN CAPITAL LETTER A + COMBINING DOT ABOVE)
    '\u0041\u030f',  # Ȁ (LATIN CAPITAL LETTER A + COMBINING DOUBLE ACUTE ACCENT)
    '\u0041\u030b',  # A̋ (LATIN CAPITAL LETTER A + COMBINING DOUBLE GRAVE ACCENT)
    '\u0041\u0311',  # Ȃ (LATIN CAPITAL LETTER A + COMBINING INVERTED BREVE)

    '\u0045\u0304',  # Ē (LATIN CAPITAL LETTER E + COMBINING MACRON)
    '\u0045\u030c',  # Ě (LATIN CAPITAL LETTER E + COMBINING CARON)
    '\u0045\u0302',  # Ê (LATIN CAPITAL LETTER E + COMBINING CIRCUMFLEX)
    '\u0045\u0301',  # É (LATIN CAPITAL LETTER E + COMBINING ACUTE ACCENT)
    '\u0045\u0300',  # È (LATIN CAPITAL LETTER E + COMBINING GRAVE ACCENT)
    '\u0045\u0306',  # Ĕ (LATIN CAPITAL LETTER E + COMBINING BREVE)
    '\u0045\u0307',  # Ė (LATIN CAPITAL LETTER E + COMBINING DOT ABOVE)
    '\u0045\u030f',  # Ȅ (LATIN CAPITAL LETTER E + COMBINING DOUBLE ACUTE ACCENT)
    '\u0045\u030b',  # E̋ (LATIN CAPITAL LETTER E + COMBINING DOUBLE GRAVE ACCENT)
    '\u0045\u0311',  # Ȇ (LATIN CAPITAL LETTER E + COMBINING INVERTED BREVE)
    '\u0049\u0304',  # Ī (LATIN CAPITAL LETTER I + COMBINING MACRON)
    '\u0049\u030c',  # Ǐ (LATIN CAPITAL LETTER I + COMBINING CARON)
    '\u0049\u0302',  # Î (LATIN CAPITAL LETTER I + COMBINING CIRCUMFLEX)
    '\u0049\u0301',  # Í (LATIN CAPITAL LETTER I + COMBINING ACUTE ACCENT)
    '\u0049\u0300',  # Ì (LATIN CAPITAL LETTER I + COMBINING GRAVE ACCENT)
    '\u0049\u0306',  # Ĭ (LATIN CAPITAL LETTER I + COMBINING BREVE)
    '\u0049\u0307',  # İ (LATIN CAPITAL LETTER I + COMBINING DOT ABOVE)
    '\u0049\u030f',  # Ȉ (LATIN CAPITAL LETTER I + COMBINING DOUBLE ACUTE ACCENT)
    '\u0049\u030b',  # I̋ (LATIN CAPITAL LETTER I + COMBINING DOUBLE GRAVE ACCENT)
    '\u0049\u0311',  # Ȋ (LATIN CAPITAL LETTER I + COMBINING INVERTED BREVE)

    '\u004F\u0304',  # Ō (LATIN CAPITAL LETTER O + COMBINING MACRON)
    '\u004F\u030c',  # Ǒ (LATIN CAPITAL LETTER O + COMBINING CARON)
    '\u004F\u0302',  # Ô (LATIN CAPITAL LETTER O + COMBINING CIRCUMFLEX)
    '\u004F\u0301',  # Ó (LATIN CAPITAL LETTER O + COMBINING ACUTE ACCENT)
    '\u004F\u0300',  # Ò (LATIN CAPITAL LETTER O + COMBINING GRAVE ACCENT)
    '\u004F\u0306',  # Ŏ (LATIN CAPITAL LETTER O + COMBINING BREVE)
    '\u004F\u0307',  # Ȯ (LATIN CAPITAL LETTER O + COMBINING DOT ABOVE)
    '\u004F\u030f',  # Ȍ (LATIN CAPITAL LETTER O + COMBINING DOUBLE ACUTE ACCENT)
    '\u004F\u030b',  # Ő (LATIN CAPITAL LETTER O + COMBINING DOUBLE GRAVE ACCENT)
    '\u004F\u0311',  # Ȏ (LATIN CAPITAL LETTER O + COMBINING INVERTED BREVE)

    '\u0052\u0304',  # R̄ (LATIN CAPITAL LETTER R + COMBINING MACRON)
    '\u0052\u030c',  # Ř (LATIN CAPITAL LETTER R + COMBINING CARON)
    '\u0052\u0302',  # R̂ (LATIN CAPITAL LETTER R + COMBINING CIRCUMFLEX)
    '\u0052\u0301',  # Ŕ (LATIN CAPITAL LETTER R + COMBINING ACUTE ACCENT)
    '\u0052\u0300',  # R̀ (LATIN CAPITAL LETTER R + COMBINING GRAVE ACCENT)
    '\u0052\u0306',  # R̆ (LATIN CAPITAL LETTER R + COMBINING BREVE)
    '\u0052\u0307',  # Ṙ (LATIN CAPITAL LETTER R + COMBINING DOT ABOVE)
    '\u0052\u030f',  # Ȑ (LATIN CAPITAL LETTER R + COMBINING DOUBLE ACUTE ACCENT)
    '\u0052\u030b',  # R̋ (LATIN CAPITAL LETTER R + COMBINING DOUBLE GRAVE ACCENT)
    '\u0052\u0311',  # Ȓ (LATIN CAPITAL LETTER R + COMBINING INVERTED BREVE)    

    '\u0055\u0304',  # Ū (LATIN CAPITAL LETTER U + COMBINING MACRON)
    '\u0055\u030c',  # Ǔ (LATIN CAPITAL LETTER U + COMBINING CARON)
    '\u0055\u0302',  # Û (LATIN CAPITAL LETTER U + COMBINING CIRCUMFLEX)
    '\u0055\u0301',  # Ú (LATIN CAPITAL LETTER U + COMBINING ACUTE ACCENT)
    '\u0055\u0300',  # Ù (LATIN CAPITAL LETTER U + COMBINING GRAVE ACCENT)
    '\u0055\u0306',  # Ŭ (LATIN CAPITAL LETTER U + COMBINING BREVE)
    '\u0055\u0307',  # U̇ (LATIN CAPITAL LETTER U + COMBINING DOT ABOVE)
    '\u0055\u030f',  # Ȕ (LATIN CAPITAL LETTER U + COMBINING DOUBLE ACUTE ACCENT)
    '\u0055\u030b',  # Ű (LATIN CAPITAL LETTER U + COMBINING DOUBLE GRAVE ACCENT)
    '\u0055\u0311',  # Ȗ (LATIN CAPITAL LETTER U + COMBINING INVERTED BREVE)
]


SERBIAN_DIACRITIC_NOTATION_CHARACTERS = [

    '\u0430\u0304',  # а̄ (CYRILLIC SMALL LETTER A + COMBINING MACRON)
    '\u0430\u030c',  # а̌ (CYRILLIC SMALL LETTER A + COMBINING CARON)
    '\u0430\u0302',  # а̂ (CYRILLIC SMALL LETTER A + COMBINING CIRCUMFLEX)
    '\u0430\u0301',  # а́ (CYRILLIC SMALL LETTER A + COMBINING ACUTE ACCENT)
    '\u0430\u0300',  # а̀ (CYRILLIC SMALL LETTER A + COMBINING GRAVE ACCENT)
    '\u0430\u0306',  # ӑ (CYRILLIC SMALL LETTER A + COMBINING BREVE)
    '\u0430\u0307',  # а̇ (CYRILLIC SMALL LETTER A + COMBINING DOT ABOVE)
    '\u0430\u030f',  # а̏ (CYRILLIC SMALL LETTER A + COMBINING DOUBLE ACUTE ACCENT)
    '\u0430\u030b',  # а̋ (CYRILLIC SMALL LETTER A + COMBINING DOUBLE GRAVE ACCENT)
    '\u0430\u0311',  # а̑ (CYRILLIC SMALL LETTER A + COMBINING INVERTED BREVE)

    '\u0435\u0304',  # е̄ (CYRILLIC SMALL LETTER E + COMBINING MACRON)
    '\u0435\u030c',  # е̌ (CYRILLIC SMALL LETTER E + COMBINING CARON)
    '\u0435\u0302',  # е̂ (CYRILLIC SMALL LETTER E + COMBINING CIRCUMFLEX)
    '\u0435\u0301',  # е́ (CYRILLIC SMALL LETTER E + COMBINING ACUTE ACCENT)
    '\u0435\u0300',  # ѐ (CYRILLIC SMALL LETTER E + COMBINING GRAVE ACCENT)
    '\u0435\u0306',  # ӗ (CYRILLIC SMALL LETTER E + COMBINING BREVE)
    '\u0435\u0307',  # е̇ (CYRILLIC SMALL LETTER E + COMBINING DOT ABOVE)
    '\u0435\u030f',  # е̏ (CYRILLIC SMALL LETTER E + COMBINING DOUBLE ACUTE ACCENT)
    '\u0435\u030b',  # е̋ (CYRILLIC SMALL LETTER E + COMBINING DOUBLE GRAVE ACCENT)
    '\u0435\u0311',  # е̑ (CYRILLIC SMALL LETTER E + COMBINING INVERTED BREVE)

    '\u0438\u0304',  # ӣ (CYRILLIC SMALL LETTER I + COMBINING MACRON)
    '\u0438\u030c',  # и̌ (CYRILLIC SMALL LETTER I + COMBINING CARON)
    '\u0438\u0302',  # и̂ (CYRILLIC SMALL LETTER I + COMBINING CIRCUMFLEX)
    '\u0438\u0301',  # и́ (CYRILLIC SMALL LETTER I + COMBINING ACUTE ACCENT)
    '\u0438\u0300',  # ѝ (CYRILLIC SMALL LETTER I + COMBINING GRAVE ACCENT)
    '\u0438\u0306',  # й (CYRILLIC SMALL LETTER I + COMBINING BREVE)
    '\u0438\u0307',  # и̇ (CYRILLIC SMALL LETTER I + COMBINING DOT ABOVE)
    '\u0438\u030f',  # и̏ (CYRILLIC SMALL LETTER I + COMBINING DOUBLE ACUTE ACCENT)
    '\u0438\u030b',  # и̋ (CYRILLIC SMALL LETTER I + COMBINING DOUBLE GRAVE ACCENT)
    '\u0438\u0311',  # и̑ (CYRILLIC SMALL LETTER I + COMBINING INVERTED BREVE)

    '\u043e\u0304',  # о̄ (CYRILLIC SMALL LETTER O + COMBINING MACRON)
    '\u043e\u030c',  # о̌ (CYRILLIC SMALL LETTER O + COMBINING CARON)
    '\u043e\u0302',  # о̂ (CYRILLIC SMALL LETTER O + COMBINING CIRCUMFLEX)
    '\u043e\u0301',  # о́ (CYRILLIC SMALL LETTER O + COMBINING ACUTE ACCENT)
    '\u043e\u0300',  # о̀ (CYRILLIC SMALL LETTER O + COMBINING GRAVE ACCENT)
    '\u043e\u0306',  # о̆ (CYRILLIC SMALL LETTER O + COMBINING BREVE)
    '\u043e\u0307',  # о̇ (CYRILLIC SMALL LETTER O + COMBINING DOT ABOVE)
    '\u043e\u030f',  # о̏ (CYRILLIC SMALL LETTER O + COMBINING DOUBLE ACUTE ACCENT)
    '\u043e\u030b',  # о̋ (CYRILLIC SMALL LETTER O + COMBINING DOUBLE GRAVE ACCENT)
    '\u043e\u0311',  # о̑ (CYRILLIC SMALL LETTER O + COMBINING INVERTED BREVE)

    '\u0440\u0304',  # р̄ (CYRILLIC SMALL LETTER ER + COMBINING MACRON)
    '\u0440\u030c',  # р̌ (CYRILLIC SMALL LETTER ER + COMBINING CARON)
    '\u0440\u0302',  # р̂ (CYRILLIC SMALL LETTER ER + COMBINING CIRCUMFLEX)
    '\u0440\u0301',  # р́ (CYRILLIC SMALL LETTER ER + COMBINING ACUTE ACCENT)
    '\u0440\u0300',  # р̀ (CYRILLIC SMALL LETTER ER + COMBINING GRAVE ACCENT)
    '\u0440\u0306',  # р̆ (CYRILLIC SMALL LETTER ER + COMBINING BREVE)
    '\u0440\u0307',  # р̇ (CYRILLIC SMALL LETTER ER + COMBINING DOT ABOVE)
    '\u0440\u030f',  # р̏ (CYRILLIC SMALL LETTER ER + COMBINING DOUBLE ACUTE ACCENT)
    '\u0440\u030b',  # р̋ (CYRILLIC SMALL LETTER ER + COMBINING DOUBLE GRAVE ACCENT)
    '\u0440\u0311',  # р̑ (CYRILLIC SMALL LETTER ER + COMBINING INVERTED BREVE)    

    '\u0443\u0304',  # ӯ (CYRILLIC SMALL LETTER U + COMBINING MACRON)
    '\u0443\u030c',  # у̌ (CYRILLIC SMALL LETTER U + COMBINING CARON)
    '\u0443\u0302',  # у̂ (CYRILLIC SMALL LETTER U + COMBINING CIRCUMFLEX)
    '\u0443\u0301',  # у́ (CYRILLIC SMALL LETTER U + COMBINING ACUTE ACCENT)
    '\u0443\u0300',  # у̀ (CYRILLIC SMALL LETTER U + COMBINING GRAVE ACCENT)
    '\u0443\u0306',  # ў (CYRILLIC SMALL LETTER U + COMBINING BREVE)
    '\u0443\u0307',  # у̇ (CYRILLIC SMALL LETTER U + COMBINING DOT ABOVE)
    '\u0443\u030f',  # у̏ (CYRILLIC SMALL LETTER U + COMBINING DOUBLE ACUTE ACCENT)
    '\u0443\u030b',  # ӳ (CYRILLIC SMALL LETTER U + COMBINING DOUBLE GRAVE ACCENT)
    '\u0443\u0311',  # у̑ (CYRILLIC SMALL LETTER U + COMBINING INVERTED BREVE)  

    '\u0410\u0304',  # А̄ (CYRILLIC CAPITAL LETTER A + COMBINING MACRON)
    '\u0410\u030c',  # А̌ (CYRILLIC CAPITAL LETTER A + COMBINING CARON)
    '\u0410\u0302',  # А̂ (CYRILLIC CAPITAL LETTER A + COMBINING CIRCUMFLEX)
    '\u0410\u0301',  # А́ (CYRILLIC CAPITAL LETTER A + COMBINING ACUTE ACCENT)
    '\u0410\u0300',  # А̀ (CYRILLIC CAPITAL LETTER A + COMBINING GRAVE ACCENT)
    '\u0410\u0306',  # Ӑ (CYRILLIC CAPITAL LETTER A + COMBINING BREVE)
    '\u0410\u0307',  # А̇ (CYRILLIC CAPITAL LETTER A + COMBINING DOT ABOVE)
    '\u0410\u030f',  # А̏ (CYRILLIC CAPITAL LETTER A + COMBINING DOUBLE ACUTE ACCENT)
    '\u0410\u030b',  # А̋ (CYRILLIC CAPITAL LETTER A + COMBINING DOUBLE GRAVE ACCENT)

    '\u0415\u0304',  # Е̄ (CYRILLIC CAPITAL LETTER E + COMBINING MACRON)
    '\u0415\u030c',  # Е̌ (CYRILLIC CAPITAL LETTER E + COMBINING CARON)
    '\u0415\u0302',  # Е̂ (CYRILLIC CAPITAL LETTER E + COMBINING CIRCUMFLEX)
    '\u0415\u0301',  # Е́ (CYRILLIC CAPITAL LETTER E + COMBINING ACUTE ACCENT)
    '\u0415\u0300',  # Ѐ (CYRILLIC CAPITAL LETTER E + COMBINING GRAVE ACCENT)
    '\u0415\u0306',  # Ӗ (CYRILLIC CAPITAL LETTER E + COMBINING BREVE)
    '\u0415\u0307',  # Е̇ (CYRILLIC CAPITAL LETTER E + COMBINING DOT ABOVE)
    '\u0415\u030f',  # Е̏ (CYRILLIC CAPITAL LETTER E + COMBINING DOUBLE ACUTE ACCENT)
    '\u0415\u030b',  # Е̋ (CYRILLIC CAPITAL LETTER E + COMBINING DOUBLE GRAVE ACCENT)
    '\u0415\u0311',  # Е̑ (CYRILLIC CAPITAL LETTER E + COMBINING INVERTED BREVE)    

    '\u0418\u0304',  # Ӣ (CYRILLIC CAPITAL LETTER I + COMBINING MACRON)
    '\u0418\u030c',  # И̌ (CYRILLIC CAPITAL LETTER I + COMBINING CARON)
    '\u0418\u0302',  # И̂ (CYRILLIC CAPITAL LETTER I + COMBINING CIRCUMFLEX)
    '\u0418\u0301',  # И́ (CYRILLIC CAPITAL LETTER I + COMBINING ACUTE ACCENT)
    '\u0418\u0300',  # Ѝ (CYRILLIC CAPITAL LETTER I + COMBINING GRAVE ACCENT)
    '\u0418\u0306',  # Й (CYRILLIC CAPITAL LETTER I + COMBINING BREVE)
    '\u0418\u0307',  # И̇ (CYRILLIC CAPITAL LETTER I + COMBINING DOT ABOVE)
    '\u0418\u030f',  # И̏ (CYRILLIC CAPITAL LETTER I + COMBINING DOUBLE ACUTE ACCENT)
    '\u0418\u030b',  # И̋ (CYRILLIC CAPITAL LETTER I + COMBINING DOUBLE GRAVE ACCENT)
    '\u0418\u0311',  # И̑ (CYRILLIC CAPITAL LETTER I + COMBINING INVERTED BREVE)    

    '\u041e\u0304',  # О̄ (CYRILLIC CAPITAL LETTER O + COMBINING MACRON)
    '\u041e\u030c',  # О̌ (CYRILLIC CAPITAL LETTER O + COMBINING CARON)
    '\u041e\u0302',  # О̂ (CYRILLIC CAPITAL LETTER O + COMBINING CIRCUMFLEX)
    '\u041e\u0301',  # О́ (CYRILLIC CAPITAL LETTER O + COMBINING ACUTE ACCENT)
    '\u041e\u0300',  # О̀ (CYRILLIC CAPITAL LETTER O + COMBINING GRAVE ACCENT)
    '\u041e\u0306',  # О̆ (CYRILLIC CAPITAL LETTER O + COMBINING BREVE)
    '\u041e\u0307',  # О̇ (CYRILLIC CAPITAL LETTER O + COMBINING DOT ABOVE)
    '\u041e\u030f',  # О̏ (CYRILLIC CAPITAL LETTER O + COMBINING DOUBLE ACUTE ACCENT)
    '\u041e\u030b',  # О̋ (CYRILLIC CAPITAL LETTER O + COMBINING DOUBLE GRAVE ACCENT)
    '\u041e\u0311',  # О̑ (CYRILLIC CAPITAL LETTER O + COMBINING INVERTED BREVE)

    '\u0420\u0304',  # Р̄ (CYRILLIC CAPITAL LETTER ER + COMBINING MACRON)
    '\u0420\u030c',  # Р̌ (CYRILLIC CAPITAL LETTER ER + COMBINING CARON)
    '\u0420\u0302',  # Р̂ (CYRILLIC CAPITAL LETTER ER + COMBINING CIRCUMFLEX)
    '\u0420\u0301',  # Р́ (CYRILLIC CAPITAL LETTER ER + COMBINING ACUTE ACCENT)
    '\u0420\u0300',  # Р̀ (CYRILLIC CAPITAL LETTER ER + COMBINING GRAVE ACCENT)
    '\u0420\u0306',  # Р̆ (CYRILLIC CAPITAL LETTER ER + COMBINING BREVE)
    '\u0420\u0307',  # Р̇ (CYRILLIC CAPITAL LETTER ER + COMBINING DOT ABOVE)
    '\u0420\u030f',  # Р̏ (CYRILLIC CAPITAL LETTER ER + COMBINING DOUBLE ACUTE ACCENT)
    '\u0420\u030b',  # Р̋ (CYRILLIC CAPITAL LETTER ER + COMBINING DOUBLE GRAVE ACCENT)
    '\u0420\u0311',  # Р̑ (CYRILLIC CAPITAL LETTER ER + COMBINING INVERTED BREVE)        

    '\u0423\u0304',  # Ӯ (CYRILLIC CAPITAL LETTER U + COMBINING MACRON)
    '\u0423\u030c',  # У̌ (CYRILLIC CAPITAL LETTER U + COMBINING CARON)
    '\u0423\u0302',  # У̂ (CYRILLIC CAPITAL LETTER U + COMBINING CIRCUMFLEX)
    '\u0423\u0301',  # У́ (CYRILLIC CAPITAL LETTER U + COMBINING ACUTE ACCENT)
    '\u0423\u0300',  # У̀ (CYRILLIC CAPITAL LETTER U + COMBINING GRAVE ACCENT)
    '\u0423\u0306',  # Ў (CYRILLIC CAPITAL LETTER U + COMBINING BREVE)
    '\u0423\u0307',  # У̇ (CYRILLIC CAPITAL LETTER U + COMBINING DOT ABOVE)
    '\u0423\u030f',  # У̏ (CYRILLIC CAPITAL LETTER U + COMBINING DOUBLE ACUTE ACCENT)
    '\u0423\u030b',  # Ӳ (CYRILLIC CAPITAL LETTER U + COMBINING DOUBLE GRAVE ACCENT)
    '\u0423\u0311',  # У̑ (CYRILLIC CAPITAL LETTER U + COMBINING INVERTED BREVE)    
]

DIACRITIC_NOTATION_CHARACTERS = \
    CROATIAN_DIACRITIC_NOTATION_CHARACTERS + \
    SERBIAN_DIACRITIC_NOTATION_CHARACTERS


























