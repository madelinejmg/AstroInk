from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_text(text, max_length=150, min_length=30):
    # Hugging Face models sometimes expect text < 512 tokens
    if len(text.split()) > 400:  # Rough token estimate
        text = " ".join(text.split()[:400])

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
