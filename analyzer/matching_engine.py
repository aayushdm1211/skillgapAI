def calculate_skill_match(
    resume_skills,
    required_skills
):

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    required_set = {
        skill.lower()
        for skill in required_skills
    }

    matched = sorted(
        resume_set.intersection(required_set)
    )

    missing = sorted(
        required_set - resume_set
    )

    if not required_set:

        score = 0.0

    else:

        score = (
            len(matched)
            / len(required_set)
        ) * 100

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": round(score, 2),
    }