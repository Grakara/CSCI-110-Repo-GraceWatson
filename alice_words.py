punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}’‘“”~"

def remove_punctuation(s):
    """Function from book that removes punctuation"""
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct.lower()

def word_split(t):
    """Splits long strings into a list of words"""
    ss = t.split()
    return ss

def count_word(listofwords):
    """counts how many times a word occurs"""
    known = {}      
    for word in listofwords:
        if str(word) not in known:
            newmemo = 1
            known[word] = newmemo
        else:
            known[word] = newmemo + 1
    return known




def AliceDictionary(string):
    """counts and sorts words in string"""
    t =remove_punctuation(str(string))
    splice = word_split(t)
    splice.sort()
    countwords = count_word(splice)     #returns dictionary
    return countwords

f = open("alice_words.txt", "r")
content = f.readlines()
f.close()

c = list(AliceDictionary(content).items())
layout = "{0:<15}{1:>8}"
layout2 = "{0:^23}"
n1 = "Word"
n2 = "Count"
print(layout.format(n1,n2))
print(layout2.format("======================="))
for (word, count) in c:
    print(layout.format(word, count))






