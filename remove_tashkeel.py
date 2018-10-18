
/**
 * Remove diacritics (tashkeel) from Arabic text
 * @author @Ahmed Salama
 * @param  string $text arabic text with diacritics (tashkeel)
 * @return string arabic text without the diacritics (tashkeel)
 */
def remove_tashkeel(text):
    # Remove honorific sign
    text = text.replace("\u0610", "")  # ARABIC SIGN SALLALLAHOU ALAYHE WA SALLAM
    text = text.replace("\u0611", "")  # ARABIC SIGN ALAYHE ASSALLAM
    text = text.replace("\u0612", "")  # ARABIC SIGN RAHMATULLAH ALAYHE
    text = text.replace("\u0613", "")  # ARABIC SIGN RADI ALLAHOU ANHU
    text = text.replace("\u0614", "")  # ARABIC SIGN TAKHALLUS

    # Remove koranic anotation
    text = text.replace("\u0615", "")  # ARABIC SMALL HIGH TAH
    text = text.replace("\u0616", "")  # ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH
    text = text.replace("\u0617", "")  # ARABIC SMALL HIGH ZAIN
    text = text.replace("\u0618", "")  # ARABIC SMALL FATHA
    text = text.replace("\u0619", "")  # ARABIC SMALL DAMMA
    text = text.replace("\u061A", "")  # ARABIC SMALL KASRA
    text = text.replace("\u06D6", "")  # ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA
    text = text.replace("\u06D7", "")  # ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA
    text = text.replace("\u06D8", "")  # ARABIC SMALL HIGH MEEM INITIAL FORM
    text = text.replace("\u06D9", "")  # ARABIC SMALL HIGH LAM ALEF
    text = text.replace("\u06DA", "")  # ARABIC SMALL HIGH JEEM
    text = text.replace("\u06DB", "")  # ARABIC SMALL HIGH THREE DOTS
    text = text.replace("\u06DC", "")  # ARABIC SMALL HIGH SEEN
    text = text.replace("\u06DD", "")  # ARABIC END OF textH
    text = text.replace("\u06DE", "")  # ARABIC START OF RUB EL HIZB
    text = text.replace("\u06DF", "")  # ARABIC SMALL HIGH ROUNDED ZERO
    text = text.replace("\u06E0", "")  # ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO
    text = text.replace("\u06E1", "")  # ARABICC SMALL HIGH DOTLESS HEAD OF KHAH
    text = text.replace("\u06E2", "")  # ARABIC SMALL HIGH MEEM ISOLATED FORM
    text = text.replace("\u06E3", "")  # ARABIC SMALL LOW SEEN
    text = text.replace("\u06E4", "")  # ARABIC SMALL HIGH MADDA
    text = text.replace("\u06E5", "")  # ARABIC SMALL WAW
    text = text.replace("\u06E6", "")  # ARABIC SMALL YEH
    text = text.replace("\u06E7", "")  # ARABIC SMALL HIGH YEH
    text = text.replace("\u06E8", "")  # ARABIC SMALL HIGH NOON
    text = text.replace("\u06E9", "")  # ARABIC PLACE OF SAJDAH
    text = text.replace("\u06EA", "")  # ARABIC EMPTY CENTRE LOW STOP
    text = text.replace("\u06EB", "")  # ARABIC EMPTY CENTRE HIGH STOP
    text = text.replace("\u06EC", "")  # ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE
    text = text.replace("\u06ED", "")  # ARABIC SMALL LOW MEEM
    text = text.replace("\u0671", "\u0627")
    text = text.replace("\u0640", "") 

    #  Remove tashkeel
    text = text.replace("\u064B", "")  # ARABIC FATHATAN
    text = text.replace("\u064C", "")  # ARABIC DAMMATAN
    text = text.replace("\u064D", "")  # ARABIC KASRATAN
    text = text.replace("\u064E", "")  # ARABIC FATHA
    text = text.replace("\u064F", "")  # ARABIC DAMMA
    text = text.replace("\u0650", "")  # ARABIC KASRA
    text = text.replace("\u0651", "")  # ARABIC SHADDA
    text = text.replace("\u0652", "")  # ARABIC SUKUN
    text = text.replace("\u0653", "")  # ARABIC MADDAH ABOVE
    text = text.replace("\u0654", "")  # ARABIC HAMZA ABOVE
    text = text.replace("\u0655", "")  # ARABIC HAMZA BELOW
    text = text.replace("\u0656", "")  # ARABIC SUBSCRIPT ALEF
    text = text.replace("\u0657", "")  # ARABIC INVERTED DAMMA
    text = text.replace("\u0658", "")  # ARABIC MARK NOON GHUNNA
    text = text.replace("\u0659", "")  # ARABIC ZWARAKAY
    text = text.replace("\u065A", "")  # ARABIC VOWEL SIGN SMALL V ABOVE
    text = text.replace("\u065B", "")  # ARABIC VOWEL SIGN INVERTED SMALL V ABOVE
    text = text.replace("\u065C", "")  # ARABIC VOWEL SIGN DOT BELOW
    text = text.replace("\u065D", "")  # ARABIC REVERSED DAMMA
    text = text.replace("\u065E", "")  # ARABIC FATHA WITH TWO DOTS
    text = text.replace("\u065F", "")  # ARABIC WAVY HAMZA BELOW
    text = text.replace("\u0670", "")  # ARABIC LETTER SUPERSCRIPT ALEF

    return text


if __name__ == "__main__":
    text = "وَمِنَ النَّاسِ مَنْ يَقُولُ آمَنَّا بِاللَّهِ وَبِالْيَوْمِ الآخِرِ وَمَا هُمْ بِمُؤْمِنِينَ "
    plain_text = remove_tashkeel(text)
    print(plain_text)
