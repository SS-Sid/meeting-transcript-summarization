from transformers import pipeline

class SentimentAnalyser:
    def __init__(self, model_dir):
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis", 
            model=model_dir, 
            tokenizer=model_dir
        )


    def predict(self, text):
        sentiments = self.sentiment_pipeline(text)
        
        for sentiment, line in zip(sentiments, text):
            sentiment['line'] = line
        
        return sentiments
    

    def get_separated_sentiments(self, text, threshold):
        sentiments = self.predict(text)
        
        positive = []
        negative = []
        for sentiment in sentiments:
            if sentiment['label'] == 'POSITIVE' \
                and sentiment['score'] > threshold:
                positive.append(sentiment)
            else:
                negative.append(sentiment)
        
        return positive, negative
    

    def get_sentiment_summary(self, text, threshold, summarizer):
        positive_sentiments, negative_sentiments = self.get_separated_sentiments(text, threshold)
        
        positive_transcript = '\n'.join([
            sentiment['line'] for sentiment in positive_sentiments
        ])
        negative_transcript = '\n'.join([
            sentiment['line'] for sentiment in negative_sentiments
        ])
        
        positive_summary = summarizer.summarize(positive_transcript)
        negative_summary = summarizer.summarize(negative_transcript)

        return positive_summary, negative_summary