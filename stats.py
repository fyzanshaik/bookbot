def countWords(content):
    word_array = content.split()
    count_of_words = len(word_array)
    return count_of_words


def count_each_character(content):
    char_freq = {}
    for char in content:
        charLower = char.lower()
        if charLower in char_freq:
            char_freq[charLower] += 1
        else:
            char_freq[charLower] = 1
    return char_freq


def get_sorted_dict_arr(char_dict):
    sorted_arr = []
    for item in char_dict:
        eachObject = {"char":f"{item}"}
