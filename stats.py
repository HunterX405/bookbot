def get_num_words(text) -> int:
    return len(text.split())

def get_char_frequency(text) -> dict:
    text = text.lower()
    frequency: dict = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

def sort_dictionary(dictionary: dict):
    return [{"char":key, "num": value} for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True)]

# def main():
#     text_freq = get_char_frequency('aaabbb ssdasmd adfbawod bawdn')
#     print(sort_dictionary(text_freq))

# main()