import re

def extract_keywords(text, num_keywords=5):
    """Extracts simple keywords from a text by frequency filtering."""
    common_words = set(["the", "and", "of", "in", "for", "to", "on", "with", "by", "an", "this", "is", "we", "our", "that", "as", "are", "be", "from"])
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in common_words and len(word) > 3]
    word_freq = {}
  
    for word in filtered_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    keywords = [word for word, freq in sorted_words[:num_keywords]]
    return keywords
