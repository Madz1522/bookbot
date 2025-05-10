def word_count(text):
    words = text.split()
    return len(words)

def count_char(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_dict(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char":char, "num":count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list
    