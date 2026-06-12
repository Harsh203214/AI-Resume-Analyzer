def extract_skills(text):

    with open("skills.txt", "r") as file:
        skills_db = file.read().splitlines()

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills