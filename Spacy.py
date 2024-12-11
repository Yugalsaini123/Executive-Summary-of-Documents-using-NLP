import spacy
from collections import defaultdict
import heapq
nlp = spacy.load("en_core_web_sm")
def preprocess_text_spacy(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    cleaned_text = ' '.join(sentences)
    return cleaned_text
def extract_summary_spacy(text, n=5):
    doc = nlp(text)
    freq_table = defaultdict(int)
    for token in doc:
        if not token.is_stop and not token.is_punct:
            freq_table[token.lemma_.lower()] += 1

    sentence_scores = defaultdict(int)
    for sent in doc.sents:
        for token in sent:
            if token.lemma_.lower() in freq_table:
                sentence_scores[sent.text] += freq_table[token.lemma_.lower()]

    summary_sentences = heapq.nlargest(n, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    return summary
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    document_text = f.read()
cleaned_text_spacy = preprocess_text_spacy(document_text)
summary_spacy = extract_summary_spacy(cleaned_text_spacy, n=10)

with open("cleaned_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text_spacy)
with open("summary_spacy.txt", "w", encoding="utf-8") as f:
    f.write(summary_spacy)
print("Cleaned text and summary saved to files.")