def ability_scores():
    scores = "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"
    return scores


def ability_skills():
    skills = "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",\
        "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature",\
        "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand",\
        "Stealth", "Survival"
    return skills


def skill_to_score_map(skill):
    score_map = {
        "Strength": "Strength",
        "Dexterity": "Dexterity",
        "Constitution": "Constitution",
        "Intelligence": "Intelligence",
        "Wisdom": "Wisdom",
        "Charisma": "Charisma",

        "Acrobatics": "Dexterity",
        "Animal Handling": "Wisdom",
        "Arcana": "Intelligence",
        "Athletics": "Strength",
        "Deception": "Charisma",
        "History": "Intelligence",
        "Insight": "Wisdom",
        "Intimidation": "Charisma",
        "Investigation": "Intelligence",
        "Medicine": "Wisdom",
        "Nature": "Intelligence",
        "Perception": "Wisdom",
        "Performance": "Charisma",
        "Persuasion": "Charisma",
        "Religion": "Intelligence",
        "Sleight of Hand": "Dexterity",
        "Stealth": "Dexterity",
        "Survival": "Wisdom"
    }
    return score_map[skill]
