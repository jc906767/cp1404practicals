"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""

def main():
    """Count how many times each word appears in a string."""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        # Increment the count if word exists, otherwise start at 1
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Sort words alphabetically
    sorted_words = sorted(word_to_count.keys())

    # Find the length of the longest word for alignment
    max_length = max(len(word) for word in sorted_words)

    # Display aligned word counts
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")

main()
