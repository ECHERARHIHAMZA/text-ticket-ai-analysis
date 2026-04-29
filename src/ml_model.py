from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def train_model(texts, labels):
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2)
    )
    cleaned_texts = [text.lower() for text in texts]
    X = vectorizer.fit_transform(cleaned_texts)

    model = LogisticRegression(max_iter=200)
    model.fit(X, labels)

    return model, vectorizer


def predict_category(text, model, vectorizer):
    X = vectorizer.transform([text])
    prediction = model.predict(X)

    return prediction[0]


def evaluate_model(texts, labels):
    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.3,
        random_state=42
    )

    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train_vectorized, y_train)

    predictions = model.predict(X_test_vectorized)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, zero_division=0)

    return accuracy, report