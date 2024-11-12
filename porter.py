import re

vovels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def replace_suffix(word, suffix, replacement):
    if word.endswith(suffix):
        return word[:-len(suffix)] + replacement
    return word

def contains_vowel(word):
    for vovel in vovels:
        if vovel in word:
            return True
    return False

def ends_with_double_consonant(word):
    n = len(word)
    if word[n-1] in consonants and word[n-1] == word[n-2]:
        return True
    else: 
        return False

def ends_with_char(word, char):
    if word[len(word)-1] == char:
        return True
    else: return False

def ends_with_cvc(word):
    suffix = word[len(word)-3:]
    pattern = r"[bcdfghjklmnpqrstvwz][aeiou][b-df-hj-np-tv-z]$"
    return bool(re.search(pattern, word))

def measure_of_word(word):
    sequence = ''
    for char in word:
        if char in vovels:
            sequence += 'V'
        else:
            sequence += 'C'
    sequence = ''.join([sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i-1]])
    return sequence.count('VC')

def restore_case(word, stem):
    stem_chars = list(stem)

    for i in range(min(len(word), len(stem_chars))):
        if word[i].isupper():
            stem_chars[i] = stem_chars[i].upper()
        else:
            stem_chars[i] = stem_chars[i].lower()

    return ''.join(stem_chars)

def step1a(word):
    if word.endswith('sses'):
        word = replace_suffix(word, 'sses', 'ss')
    elif word.endswith('ies'):
        word = replace_suffix(word, 'ies', 'i')
    elif word.endswith('ss'):
        word = word
    elif word.endswith('s'):
        word = replace_suffix(word, 's', '')
    return word

def step1b_prim(word):
    if word.endswith('at'):
        word = replace_suffix(word, 'at', 'ate')
    elif word.endswith('bl'):
        word = replace_suffix(word, 'bl', 'ble')
    elif word.endswith('iz'):
        word = replace_suffix(word, 'iz', 'ize')
    elif ends_with_double_consonant(word):
        if not(ends_with_char('l') and ends_with_char('s') and ends_with_char('z')):
            word = word[:-1]
    elif measure_of_word(word) == 1 and ends_with_cvc(word):
        word = word[:-1] + 'e'
    return word
    
def step1b(word):
    if word.endswith('eed') and measure_of_word(word[:-3]) > 0:
        word = replace_suffix(word, 'eed', 'ee')
    elif word.endswith('ed') and contains_vowel(word):
        word = replace_suffix(word, 'ed', '')
        word = step1b_prim(word)
    elif word.endswith('ing') and contains_vowel(word):
        word = replace_suffix(word, 'ing', '')
        word = step1b_prim(word)
    return word

def step1c(word):
    if word.endswith('y') and contains_vowel(word[:-1]):
        replace_suffix(word, 'y', 'i')
    return word

def step2(word):
    if measure_of_word(word) == 0:
        return word
    else:
        if word.endswith('ational'):
            replace_suffix(word, 'ational', 'ate')
        elif word.endswith('tional'):
            replace_suffix(word,'tional','tion')
        elif word.endswith('enci'):
            replace_suffix(word,'enci','ence')
        elif word.endswith('anci'):
            word = replace_suffix(word, 'anci', 'ance')
        elif word.endswith('izer'):
            word = replace_suffix(word, 'izer', 'ize')
        elif word.endswith('abli'):
            word = replace_suffix(word, 'abli', 'able')
        elif word.endswith('alli'):
            word = replace_suffix(word, 'alli', 'al')
        elif word.endswith('entli'):
            word = replace_suffix(word, 'entli', 'ent')
        elif word.endswith('eli'):
            word = replace_suffix(word, 'eli', 'e')
        elif word.endswith('ousli'):
            word = replace_suffix(word, 'ousli', 'ous')
        elif word.endswith('ization'):
            word = replace_suffix(word, 'ization', 'ize')
        elif word.endswith('ation'):
            word = replace_suffix(word, 'ation', 'ate')
        elif word.endswith('ator'):
            word = replace_suffix(word, 'ator', 'ate')
        elif word.endswith('alism'):
            word = replace_suffix(word, 'alism', 'al')
        elif word.endswith('iveness'):
            word = replace_suffix(word, 'iveness', 'ive')
        elif word.endswith('fulness'):
            word = replace_suffix(word, 'fulness', 'ful')
        elif word.endswith('ousness'):
            word = replace_suffix(word, 'ousness', 'ous')
        elif word.endswith('aliti'):
            word = replace_suffix(word, 'aliti', 'al')
        elif word.endswith('iviti'):
            word = replace_suffix(word, 'iviti', 'ive')
        elif word.endswith('biliti'):
            word = replace_suffix(word, 'biliti', 'ble')
    return word

def step3(word):
    if measure_of_word == 0:
        return word
    else:
        if word.endswith('icate'):
            word = replace_suffix(word, 'icate', 'ic')
        elif word.endswith('ative'):
            word = replace_suffix(word, 'ative', '')
        elif word.endswith('alize'):
            word = replace_suffix(word, 'alize', 'al')
        elif word.endswith('iciti'):
            word = replace_suffix(word, 'iciti', 'ic')
        elif word.endswith('ical'):
            word = replace_suffix(word, 'ical', 'ic')
        elif word.endswith('ful'):
            word = replace_suffix(word, 'ful', '')
        elif word.endswith('ness'):
            word = replace_suffix(word, 'ness', '')
    return word

def step4(word):
    if measure_of_word(word) <= 1:
        return word
    
    if word.endswith('al'):
        word = replace_suffix(word, 'al', '')
    elif word.endswith('ance'):
        word = replace_suffix(word, 'ance', '')
    elif word.endswith('ence'):
        word = replace_suffix(word, 'ence', '')
    elif word.endswith('er'):
        word = replace_suffix(word, 'er', '')
    elif word.endswith('ic'):
        word = replace_suffix(word, 'ic', '')
    elif word.endswith('able'):
        word = replace_suffix(word, 'able', '')
    elif word.endswith('ible'):
        word = replace_suffix(word, 'ible', '')
    elif word.endswith('ant'):
        word = replace_suffix(word, 'ant', '')
    elif word.endswith('ement'):
        word = replace_suffix(word, 'ement', '')
    elif word.endswith('ment'):
        word = replace_suffix(word, 'ment', '')
    elif word.endswith('ent'):
        word = replace_suffix(word, 'ent', '')
    elif word.endswith('ion') and (ends_with_char(word[:-3],'s') or ends_with_char(word[:-3],'t')):
        word = replace_suffix(word, 'ion', '')
    elif word.endswith('ou'):
        word = replace_suffix(word, 'ou', '')
    elif word.endswith('ism'):
        word = replace_suffix(word, 'ism', '')
    elif word.endswith('ate'):
        word = replace_suffix(word, 'ate', '')
    elif word.endswith('iti'):
        word = replace_suffix(word, 'iti', '')
    elif word.endswith('ous'):
        word = replace_suffix(word, 'ous', '')
    elif word.endswith('ive'):
        word = replace_suffix(word, 'ive', '')
    elif word.endswith('ize'):
        word = replace_suffix(word, 'ize', '')
    return word

def step5a(word):
    if measure_of_word(word[:-1]) > 1 and word.endswith('e'):
        word = replace_suffix(word, 'e','')
    elif measure_of_word(word[:-1]) == 1 and not(ends_with_cvc(word)) and word.endswith('e'):
        word = replace_suffix(word, 'e', '')
    return word

def step5b(word):
    if word.endswith('ll') and measure_of_word(word[:-2])>1:
        replace_suffix(word, 'l', '')
    return word

def stem_word(word):
    stem = word.lower()
    stem = step1a(stem)
    stem = step1b(stem)
    stem = step1c(stem)
    stem = step2(stem)
    stem = step3(stem)
    stem = step4(stem)
    stem = step5a(stem)
    stem = step5b(stem)
    return restore_case(word, stem)

if __name__ == '__main__':
    print(f"Słowo: enlightening\nPo wykonaniu algorytmu Portera: {stem_word('enlightening')}\n")    #'pouczający'
    print(f"Słowo: nearness\nPo wykonaniu algorytmu Portera: {stem_word('nearness')}\n")            #'bliskość'
    print(f"Słowo: imperturbable\nPo wykonaniu algorytmu Portera: {stem_word('imperturbable')}\n")  #'niezwruszony'
    print(f"Słowo: badly\nPo wykonaniu algorytmu Portera: {stem_word('badly')}\n")                  #'źle'