from transformers import pipeline

with open("cleaned_text.txt", "r", encoding="utf-8") as f:
    cleaned_text_spacy = f.read()


def split_text(text, chunk_size=1024):
    
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def summarize_text_transformer(text, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")  # Use PyTorch
    input_length = len(text.split())
    max_length = min(300, input_length // 2)  
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
    return summary


chunks = split_text(cleaned_text_spacy)

summaries = [summarize_text_transformer(chunk) for chunk in chunks]
summary_transformer = ' '.join(summaries)


with open("summary_transformer.txt", "w", encoding="utf-8") as f:
    f.write(summary_transformer)

print("Summary saved to file.")
