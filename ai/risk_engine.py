def calculate_risk(category):
    risk_map = {
        "medical_record": 9,
        "biometric": 10,
        "insurance": 8,
        "appointment": 5
    }
    return risk_map.get(category, 3)


def explain_risk(category):
    explanations = {
        "medical_record": "Medical data leaks can lead to insurance denial and long-term profiling.",
        "biometric": "Biometric health data is irreversible and highly sensitive.",
        "insurance": "Insurance data exposure may affect premiums or coverage.",
        "appointment": "Metadata leaks can reveal personal behavior patterns."
    }

    return explanations.get(category, "Low sensitivity exposure detected.")
