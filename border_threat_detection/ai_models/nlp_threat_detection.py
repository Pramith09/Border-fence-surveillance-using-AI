# ai_models/nlp_threat_detection.py
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Disable TensorFlow use

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_text_threat(text):
    candidate_labels = ["terrorism", "violence", "protest", "smuggling", "benign"]
    result = classifier(text, candidate_labels)
    return {"labels": result["labels"], "scores": result["scores"]}

