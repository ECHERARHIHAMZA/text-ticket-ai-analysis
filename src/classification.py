def classify(text):
    text = text.lower()

    if "erreur" in text or "bug" in text or "incident" in text:
        return "Incident IT"

    elif "accès" in text or "compte" in text or "droits" in text:
        return "Demande d'accès"

    elif "demande" in text or "question" in text:
        return "Support utilisateur"

    elif "rh" in text or "agent" in text or "congés" in text:
        return "Processus RH"

    else:
        return "Autre"