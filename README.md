# 🚀 SkillGap AI — Intelligent Career Skill Gap Analyzer

SkillGap AI is a Django-based web application that analyzes a candidate's resume against a job description, identifies matching and missing technical skills, calculates a skill-match score, and provides learning recommendations.

## ✨ Features

* 📄 **Resume Parsing:** Extracts text from PDF resumes using PyMuPDF.
* 🔍 **Skill Extraction:** Identifies technical skills using a predefined skill dictionary.
* 🎯 **Skill Matching:** Compares resume skills with skills detected in job descriptions.
* 📊 **Match Score:** Calculates a percentage based on detected required skills.
* 💡 **Learning Recommendations:** Suggests areas to improve based on missing skills.
* 🗄️ **Database Storage:** Stores analysis results using Django's ORM and SQLite.
* 🛡️ **Input Validation:** Checks PDF file extensions and upload size.

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python, Django
* **Database:** SQLite
* **PDF Processing:** PyMuPDF
* **Skill Analysis:** Python regular expressions and set operations
* **Version Control:** Git and GitHub

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aayushdm1211/skillgapAI.git
cd skillgapAI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## 📊 How It Works

1. Upload a text-based PDF resume.
2. Paste the target job description.
3. Extract supported technical skills from both inputs.
4. Compare the detected skills.
5. View matching skills, missing skills, the match score, and recommendations.

## 🧮 Matching Algorithm

The application calculates skill coverage using:

**Match Score = (Number of Matching Required Skills / Total Detected Required Skills) × 100**

The score represents coverage of supported skills detected by the current dictionary. It does not represent a candidate's actual proficiency or probability of getting hired.

## 🔮 Future Improvements

* Expand technical skill detection.
* Add charts and a more interactive dashboard.
* Provide learning resources for missing skills.
* Improve handling of scanned PDF resumes.
* Add secure user authentication and analysis history.

## 👨‍💻 Author

**Aayush Mali**

GitHub: [@aayushdm1211](https://github.com/aayushdm1211)

---

⭐ If you find this project interesting, consider giving the repository a star!
