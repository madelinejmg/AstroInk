import re

def summarize_text(text, num_sentences=3):
    # Split abstract into sentences
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    # Take the first few sentences
    summary = sentences[:num_sentences]
    return " ".join(summary)
