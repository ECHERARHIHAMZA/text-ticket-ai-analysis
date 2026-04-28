import json
from preprocessing import clean_text, tokenize
from classification import classify
from analysis import count_categories

def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def extract_texts(data):
    return [item["text"] for item in data]


if __name__ == "__main__":
    data = load_data("data/data.json")
    texts = extract_texts(data)

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