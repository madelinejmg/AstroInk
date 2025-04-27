from transformers import pipeline

# Load a smaller summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=150, min_length=30):
    if len(text.split()) > 400:
        text = " ".join(text.split()[:400])
    
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
