def count_words(text_to_count):
    words_number = text_to_count.split()
    return len(words_number)

def get_unique_characters(text):
    dictionary_word_appearances = {}
    for char in text.lower():
        if char in dictionary_word_appearances:
            dictionary_word_appearances[char] += 1
        else:
            dictionary_word_appearances[char] = 1        
    return dictionary_word_appearances
