def calculate_score(skills):

    score = 0

    score += len(skills) * 5

    if score > 100:
        score = 100

    return score