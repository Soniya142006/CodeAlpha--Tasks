import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Collect FAQs (Questions and their Answers)
faq_data = {
    "What is your return policy?": "You can return any item within 30 days of purchase.",
    "How do I track my order?": "Use the tracking link sent to your email after shipment.",
    "Do you ship internationally?": "Yes, we ship to over 50 countries worldwide.",
    "How can I contact customer support?": "You can email us at support@example.com or call 1-800-123-4567.",
    "What payment methods do you accept?": "We accept Credit Cards, PayPal, and Apple Pay."
}

faq_questions = list(faq_data.keys())

def chatbot_response(user_input):
    # 2. Preprocess and 3. Match questions using Cosine Similarity
    # We combine the user input with the FAQ list for vectorization
    vectorizer = TfidfVectorizer().fit_transform(faq_questions + [user_input])
    vectors = vectorizer.toarray()

    # Compare user vector (last one) against all FAQ vectors
    user_vector = vectors[-1].reshape(1, -1)
    faq_vectors = vectors[:-1]
    
    similarities = cosine_similarity(user_vector, faq_vectors).flatten()
    
    # Find the index of the highest similarity score
    closest_index = np.argmax(similarities)
    confidence = similarities[closest_index]

    # 4. Display the best matching answer
    # A threshold (e.g., 0.3) ensures the bot doesn't give a wrong answer to random text
    if confidence > 0.3:
        return faq_data[faq_questions[closest_index]]
    else:
        return "I'm sorry, I don't have an answer for that. Please contact support."

# 5. Simple Chat UI (Command Line)
print("--- FAQ Chatbot ---")
print("Type 'quit' to exit.")

while True:
    user_query = input("\nYou: ")
    if user_query.lower() in ['quit', 'exit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot_response(user_query)
    print(f"Chatbot: {response}")
