def count_characters(s):
    return len(s.replace(" ", ""))

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test
if __name__ == "_main_":
    test = "Hello world from Python"
    print("Characters:", count_characters(test))
    print("Words:", count_words(test))
    print("Average word length:", average_word_length(test))
