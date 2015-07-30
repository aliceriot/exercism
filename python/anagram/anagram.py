from collections import Counter

def detect_anagrams(word, anagrams):
    wc = Counter(word.lower())
    agranams = filter(lambda x: x.lower() != word.lower(), anagrams)
    grams = filter(lambda x: Counter(x.lower()) == wc, agranams)
    return grams


