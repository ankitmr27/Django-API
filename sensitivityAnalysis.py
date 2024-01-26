from transformers import pipeline

# Load a sentiment analysis model
nlp = pipeline("sentiment-analysis")

def getSentiment(text):
    # Run the model
    result = nlp(text)
    # Display the result
    return result[0]['label']