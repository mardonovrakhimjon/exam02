def count_words(text: str) -> dict:
    words = text.lower().split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    return word_count

print(count_words("salom salom dunyo"))
print(count_words("Python python PYTHON"))
