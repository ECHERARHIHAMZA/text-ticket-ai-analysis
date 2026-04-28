def count_categories(texts, classify_function):
    results = {}

    for text in texts:
        category = classify_function(text)

        if category in results:
            results[category] += 1
        else:
            results[category] = 1

    return results