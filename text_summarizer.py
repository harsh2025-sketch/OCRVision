from transformers import pipeline

def summarize_text(text, max_length=150, min_length=50):
    summarizer = pipeline("summarization")
    # Split text into chunks if it's too long
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return " ".join(summaries)

if __name__ == "__main__":
    # Test the summarization
    test_text = "Long text for testing..." * 50  # Repeat to make it longer
    summary = summarize_text(test_text)
    print("Summary:", summary)
