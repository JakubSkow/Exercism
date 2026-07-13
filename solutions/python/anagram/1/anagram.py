def find_anagrams(word, candidates):
    final = []
    for candidate in candidates:
        word2 = candidate
        if len(word) != len(word2):
            continue
        if word.lower() == word2.lower():
            continue
        if sorted(word.lower()) != sorted(word2.lower()):
            continue
        final.append(word2)

    return final
