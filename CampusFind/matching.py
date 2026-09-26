import re


STOP_WORDS = {
    "the", "a", "an", "and", "of", "with", "near", "at", "in",
    "item", "found", "lost", "black", "white"
}


def words(text):
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return {token for token in tokens if token not in STOP_WORDS}


def similarity(left, right):
    a, b = words(left), words(right)
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def calculate_match(lost, found):
    score = 0
    reasons = []

    if lost.category.lower() == found.category.lower():
        score += 30
        reasons.append("same category")

    if lost.color.lower() == found.color.lower():
        score += 15
        reasons.append("same color")

    location_score = similarity(lost.location, found.location)
    if location_score > 0:
        score += 20
        reasons.append("similar location")

    description_score = similarity(
        f"{lost.name} {lost.description}",
        f"{found.name} {found.description}"
    )
    score += round(description_score * 25)
    if description_score >= 0.2:
        reasons.append("similar description")

    if lost.date == found.date:
        score += 10
        reasons.append("same date")

    return min(score, 100), reasons
