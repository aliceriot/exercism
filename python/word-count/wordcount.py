def word_count(input_string):
    words = {}

    for word in input_string.split():
        if (word in words):
            words[word] += 1
        else:
            words[word] = 1

    return words

    
