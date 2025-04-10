from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

def main():
    sentence = input("Enter a sentence: ")

    reversed_str = reverse_string(sentence)
    capitalized_str = capitalize_words(sentence)
    cleaned_str = remove_punctuation(sentence)

    print("\n--- String Analysis ---")
    print("Reversed:", reversed_str)
    print("Capitalized:", capitalized_str)

    print("\nAfter removing punctuation:")
    print("Character count (no spaces):", count_characters(cleaned_str))
    print("Word count:", count_words(cleaned_str))
    print("Average word length:", round(average_word_length(cleaned_str), 2))

if __name__ == "__main__":
    main()
