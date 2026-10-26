import re


SKILL_DICTIONARY = {

    "Python": [
        "python"
    ],

    "Django": [
        "django"
    ],

    "Flask": [
        "flask"
    ],

    "FastAPI": [
        "fastapi"
    ],

    "SQL": [
        "sql",
        "structured query language"
    ],

    "MySQL": [
        "mysql"
    ],

    "PostgreSQL": [
        "postgresql",
        "postgres"
    ],

    "MongoDB": [
        "mongodb",
        "mongo db"
    ],

    "REST API": [
        "rest api",
        "restful api",
        "rest apis",
        "restful apis"
    ],

    "Git": [
        "git",
        "github",
        "gitlab"
    ],

    "Docker": [
        "docker",
        "containerization"
    ],

    "Machine Learning": [
        "machine learning",
        "machine-learning"
    ],

    "Deep Learning": [
        "deep learning",
        "deep-learning"
    ],

    "TensorFlow": [
        "tensorflow"
    ],

    "PyTorch": [
        "pytorch"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy"
    ],

    "HTML": [
        "html"
    ],

    "CSS": [
        "css",
        "cascading style sheets"
    ],

    "JavaScript": [
        "javascript",
        "java script"
    ],

    "React": [
        "react",
        "react.js",
        "reactjs"
    ],

    "React Native": [
        "react native"
    ],

    "AWS": [
        "aws",
        "amazon web services"
    ],

    "Linux": [
        "linux"
    ],

    "Data Structures": [
        "data structures",
        "data structure"
    ],

    "Algorithms": [
        "algorithms",
        "algorithm"
    ],
}


def extract_skills(text):

    found_skills = []

    normalized_text = text.lower()

    for skill, aliases in SKILL_DICTIONARY.items():

        for alias in aliases:

            pattern = (
                r"(?<!\w)"
                + re.escape(alias.lower())
                + r"(?!\w)"
            )

            if re.search(pattern, normalized_text):

                found_skills.append(skill)

                break

    return sorted(found_skills)