import json
from preprocessing import clean_text, tokenize
from classification import classify
from analysis import count_categories
from ml_model import train_model, predict_category


def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def extract_texts(data):
    return [item["text"] for item in data]


if __name__ == "__main__":
    data = load_data("data/data.json")
    texts = extract_texts(data)

    # Labels pour le ML
    labels = [classify(text) for text in texts]

    # Entraînement du modèle
    model, vectorizer = train_model(texts, labels)

    print("=== Classification des tickets ===")
    for text in texts:
        category = classify(text)
        print("Texte :", text)
        print("Catégorie :", category)
        print()

    print("=== Analyse des catégories ===")
    stats = count_categories(texts, classify)

    for category, count in stats.items():
        print(f"{category} : {count}")

    print("\n=== Prédictions Machine Learning ===")
    for text in texts:
        prediction = predict_category(text, model, vectorizer)
        print("Texte :", text)
        print("Prédiction ML :", prediction)
        print()