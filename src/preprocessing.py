import string


def clean_text(text):
    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text


def tokenize(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    return words