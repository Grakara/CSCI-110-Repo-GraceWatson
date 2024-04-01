import string

def remove_punctuation(s):
    """Function from book that removes punctuation"""
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct.lower()

def word_split(t):
    """Splits long strings into a list of words"""
    ss = t.split()
    return ss

def count_e(ss):
    """counts how many words have an "e" in them"""
    count1 = 0
    for l in str(ss):
        for c in(l):
            if c == "e":
                count1 += 1
    return count1


def NoPunctSplitCount(string):
    """Combines No punctuation, split, and count_e functions to make new string and
numbers"""
    NewVariableString = remove_punctuation(string).split()
    word_count = len(NewVariableString)
    countofe = count_e(NewVariableString)
    percentage = (countofe / word_count)*100
    print("""Your text contains {0} words,of which {1} ({2:.1f}%) contain an "e".""".format(word_count, countofe, percentage))
    return NewVariableString

OriginalString = """
Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing
in place of English to emphasise design elements over content. It's also called
placeholder (or filler) text. It's a convenient tool for mock-ups.
It helps to outline the visual elements of a document or presentation,
eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by
the classical author and philosopher Cicero. Its words and letters have been changed
by addition or removal, so to deliberately render its content nonsensical; it's not
genuine, correct, or comprehensible Latin anymore. While lorem ipsum's still resembles
classical Latin, it actually has no meaning whatsoever. As Cicero's text doesn't
contain the letters K, W, or Z, alien to latin, these, and others are often inserted
randomly to mimic the typographic appearence of European languages, as are digraphs not
to be found in the original."""

NoPunctSplitCount(OriginalString)
