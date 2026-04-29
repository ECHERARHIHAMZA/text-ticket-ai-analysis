def classify(text):
    text = text.lower()

    # Incident IT
    if (
        "erreur" in text
        or "bug" in text
        or "incident" in text
        or "problème" in text
        or "performance" in text
        or "lent" in text
        or "lente" in text
    ):
        return "Incident IT"

    # Documentation / Procédure
    elif (
        "documentation" in text
        or "procédure" in text
        or "wiki" in text
        or "guide" in text
    ):
        return "Documentation"

    # Processus RH (à mettre AVANT support pour éviter conflits)
    elif (
        "rh" in text
        or "agent" in text
        or "congés" in text
        or "arrivée" in text
        or "départ" in text
    ):
        return "Processus RH"

    # Demande d'accès
    elif (
        "accès" in text
        or "compte" in text
        or "droits" in text
    ):
        return "Demande d'accès"

    # Support utilisateur
    elif (
        "demande" in text
        or "question" in text
        or "besoin" in text
    ):
        return "Support utilisateur"

    # Autre
    else:
        return "Autre"