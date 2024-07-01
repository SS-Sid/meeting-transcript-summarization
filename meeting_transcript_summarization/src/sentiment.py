from transformers import pipeline

class SentimentAnalyser:
    def __init__(self, model_dir):
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=model_dir, tokenizer=model_dir)

    def predict(self, text):
        return self.sentiment_pipeline(text)