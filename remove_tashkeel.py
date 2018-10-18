def get_normal_text(aya):
    # Remove honorific sign
    aya = aya.replace("\u0610", "")  # ARABIC SIGN SALLALLAHOU ALAYHE WA SALLAM
    aya = aya.replace("\u0611", "")  # ARABIC SIGN ALAYHE ASSALLAM
    aya = aya.replace("\u0612", "")  # ARABIC SIGN RAHMATULLAH ALAYHE
    aya = aya.replace("\u0613", "")  # ARABIC SIGN RADI ALLAHOU ANHU
    aya = aya.replace("\u0614", "")  # ARABIC SIGN TAKHALLUS

    # Remove koranic anotation
    aya = aya.replace("\u0615", "")  # ARABIC SMALL HIGH TAH
    aya = aya.replace("\u0616", "")  # ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH
    aya = aya.replace("\u0617", "")  # ARABIC SMALL HIGH ZAIN
    aya = aya.replace("\u0618", "")  # ARABIC SMALL FATHA
    aya = aya.replace("\u0619", "")  # ARABIC SMALL DAMMA
    aya = aya.replace("\u061A", "")  # ARABIC SMALL KASRA
    aya = aya.replace("\u06D6", "")  # ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA
    aya = aya.replace("\u06D7", "")  # ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA
    aya = aya.replace("\u06D8", "")  # ARABIC SMALL HIGH MEEM INITIAL FORM
    aya = aya.replace("\u06D9", "")  # ARABIC SMALL HIGH LAM ALEF
    aya = aya.replace("\u06DA", "")  # ARABIC SMALL HIGH JEEM
    aya = aya.replace("\u06DB", "")  # ARABIC SMALL HIGH THREE DOTS
    aya = aya.replace("\u06DC", "")  # ARABIC SMALL HIGH SEEN
    aya = aya.replace("\u06DD", "")  # ARABIC END OF AYAH
    aya = aya.replace("\u06DE", "")  # ARABIC START OF RUB EL HIZB
    aya = aya.replace("\u06DF", "")  # ARABIC SMALL HIGH ROUNDED ZERO
    aya = aya.replace("\u06E0", "")  # ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO
    aya = aya.replace("\u06E1", "")  # ARABICC SMALL HIGH DOTLESS HEAD OF KHAH
    aya = aya.replace("\u06E2", "")  # ARABIC SMALL HIGH MEEM ISOLATED FORM
    aya = aya.replace("\u06E3", "")  # ARABIC SMALL LOW SEEN
    aya = aya.replace("\u06E4", "")  # ARABIC SMALL HIGH MADDA
    aya = aya.replace("\u06E5", "")  # ARABIC SMALL WAW
    aya = aya.replace("\u06E6", "")  # ARABIC SMALL YEH
    aya = aya.replace("\u06E7", "")  # ARABIC SMALL HIGH YEH
    aya = aya.replace("\u06E8", "")  # ARABIC SMALL HIGH NOON
    aya = aya.replace("\u06E9", "")  # ARABIC PLACE OF SAJDAH
    aya = aya.replace("\u06EA", "")  # ARABIC EMPTY CENTRE LOW STOP
    aya = aya.replace("\u06EB", "")  # ARABIC EMPTY CENTRE HIGH STOP
    aya = aya.replace("\u06EC", "")  # ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE
    aya = aya.replace("\u06ED", "")  # ARABIC SMALL LOW MEEM
    aya = aya.replace("\u0671", "\u0627")
    aya = aya.replace("\u0640", "") 

    #  Remove tashkeel
    aya = aya.replace("\u064B", "")  # ARABIC FATHATAN
    aya = aya.replace("\u064C", "")  # ARABIC DAMMATAN
    aya = aya.replace("\u064D", "")  # ARABIC KASRATAN
    aya = aya.replace("\u064E", "")  # ARABIC FATHA
    aya = aya.replace("\u064F", "")  # ARABIC DAMMA
    aya = aya.replace("\u0650", "")  # ARABIC KASRA
    aya = aya.replace("\u0651", "")  # ARABIC SHADDA
    aya = aya.replace("\u0652", "")  # ARABIC SUKUN
    aya = aya.replace("\u0653", "")  # ARABIC MADDAH ABOVE
    aya = aya.replace("\u0654", "")  # ARABIC HAMZA ABOVE
    aya = aya.replace("\u0655", "")  # ARABIC HAMZA BELOW
    aya = aya.replace("\u0656", "")  # ARABIC SUBSCRIPT ALEF
    aya = aya.replace("\u0657", "")  # ARABIC INVERTED DAMMA
    aya = aya.replace("\u0658", "")  # ARABIC MARK NOON GHUNNA
    aya = aya.replace("\u0659", "")  # ARABIC ZWARAKAY
    aya = aya.replace("\u065A", "")  # ARABIC VOWEL SIGN SMALL V ABOVE
    aya = aya.replace("\u065B", "")  # ARABIC VOWEL SIGN INVERTED SMALL V ABOVE
    aya = aya.replace("\u065C", "")  # ARABIC VOWEL SIGN DOT BELOW
    aya = aya.replace("\u065D", "")  # ARABIC REVERSED DAMMA
    aya = aya.replace("\u065E", "")  # ARABIC FATHA WITH TWO DOTS
    aya = aya.replace("\u065F", "")  # ARABIC WAVY HAMZA BELOW
    aya = aya.replace("\u0670", "")  # ARABIC LETTER SUPERSCRIPT ALEF

    return aya
