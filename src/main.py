import json
from preprocessing import clean_text, tokenize


def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def extract_texts(data):
    return [item["text"] for item in data]


if __name__ == "__main__":
    data = load_data("data/data.json")
    texts = extract_texts(data)

    print("=== Prétraitement des tickets ===")
    for text in texts:
        print("Texte original :", text)
        print("Texte nettoyé :", clean_text(text))
        print("Mots :", tokenize(text))
        print()