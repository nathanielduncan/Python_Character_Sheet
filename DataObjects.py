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


def score_to_skill_dict(ability):
    score_map = {
        "Strength": {"Athletics", },
        "Dexterity": {"Acrobatics", "Sleight of Hand", "Stealth"},
        "Constitution": {},
        "Intelligence": {"Arcana", "History", "Investigation", "Nature", "Religion"},
        "Wisdom": {"Animal Handling", "Insight", "Medicine", "Perception", "Survival"},
        "Charisma": {"Deception", "Intimidation", "Performance", "Persuasion"}
    }
    return score_map[ability]


def proficiency_bonus_map(level):
    if level < 5:
        key = "A"
    if 5 <= level < 9:
        key = "B"
    if 9 <= level < 13:
        key = "C"
    if 13 <= level < 17:
        key = "D"
    if 17 <= level:
        key = "E"

    prof_bonus_map = {
        "A": "2",
        "B": "3",
        "C": "4",
        "D": "5",
        "E": "6"
    }
    return prof_bonus_map[key]
