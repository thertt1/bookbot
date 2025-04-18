def word_count(text):
    num_words = text.split()
    num_words = len(num_words)
    print(f'Found {num_words} total words')
    return num_words

def char_count(text):
    text = text.lower()
    char_count = {}
    for i in text:
        char_count[i] = char_count.get(i, 0) + 1
    return char_count

def remove_others(a):
    keys_to_remove = [key for key in a if not str(key).isalpha()]
    for key in keys_to_remove:
        del a[key]
    return a

def formatting(x): 
    char_count = x
    ## remove non alphas from dict
    char_count = remove_others(char_count)
    ##sort dict
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    ## final printing
    for i in char_count:
        if str(char_count.get(i)):
            print(f'{i}: {char_count[i]}')