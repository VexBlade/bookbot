def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    character_count = {}
    for char in text:
        processed_char = char.lower()
        character_count[processed_char] = character_count.get(processed_char, 0) + 1

    return character_count

def count_characters_sorted(text):
    character_count = count_characters(text)
    filtered_count = {char: count for char, count in character_count.items() if char.isalpha()}
    sorted_characters = sorted(filtered_count.items(), key=lambda item: item[1], reverse=True)
    
    # Transforming the sorted list into a dictionary
    result = {char: count for char, count in sorted_characters}
    return result
