import re

def summarize_text(text, num_sentences = 3):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    summary = setnences[:num_sentences)
    return " ".join(summary)
