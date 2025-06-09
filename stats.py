def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def get_num_char(text):
    char_dict = {}
    for c in text:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict