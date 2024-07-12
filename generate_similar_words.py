from metaphone import doublemetaphone

def generate_similar_words(input_word, max_distance=1):
    primary_code, _ = doublemetaphone(input_word)
    similar_words = set()

    # Same length variations (original logic)
    for i in range(len(input_word)):
        for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if char != input_word[i]:
                variation = input_word[:i] + char + input_word[i+1:]
                variation_code, _ = doublemetaphone(variation)
                if variation_code == primary_code:
                    similar_words.add(variation)

    # One character longer variations
    for i in range(len(input_word) + 1):
        for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            variation = input_word[:i] + char + input_word[i:]
            variation_code, _ = doublemetaphone(variation)
            if variation_code == primary_code:
                similar_words.add(variation)

    # One character shorter variations
    for i in range(len(input_word)):
        variation = input_word[:i] + input_word[i+1:]
        variation_code, _ = doublemetaphone(variation)
        if variation_code == primary_code:
            similar_words.add(variation)

    similar_words.discard(input_word)
    return similar_words

input_word = input("Please input a Name: ")
similar_words = generate_similar_words(input_word)
print(f"Similar words for '{input_word}': {', '.join(similar_words)}")
