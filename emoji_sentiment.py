positive_emojis = ['😊', '😁', '👍', '🎉', '😍', '😎', '💖']
negative_emojis = ['😢', '😡', '👎', '💔', '😭', '😞', '🤬']

def analyze_emoji_sentiment(text):
    pos_count = sum(text.count(emoji) for emoji in positive_emojis)
    neg_count = sum(text.count(emoji) for emoji in negative_emojis)

    sentiment = "Neutral"
    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"

    return {
        "positive": pos_count,
        "negative": neg_count,
        "overall": sentiment
    }

if __name__ == "__main__":
    test_text = "This product is amazing 😊😊 but also a bit expensive 😞"
    result = analyze_emoji_sentiment(test_text)

    print("📝 Text:", test_text)
    print("📊 Positive emojis:", result["positive"])
    print("📉 Negative emojis:", result["negative"])
    print("🔎 Sentiment:", result["overall"])
