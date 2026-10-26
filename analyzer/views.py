from django.shortcuts import render

from .forms import SkillAnalysisForm

from .resume_parser import extract_text_from_pdf

from .skill_engine import extract_skills

from .matching_engine import calculate_skill_match

from .models import SkillAnalysis


def home(request):

    form = SkillAnalysisForm()

    return render(
        request,
        "analyzer/home.html",
        {
            "form": form
        }
    )


def analyze_resume(request):

    if request.method != "POST":

        return render(
            request,
            "analyzer/home.html",
            {
                "form": SkillAnalysisForm()
            }
        )

    form = SkillAnalysisForm(
        request.POST,
        request.FILES
    )

    if not form.is_valid():

        return render(
            request,
            "analyzer/home.html",
            {
                "form": form
            }
        )

    candidate_name = form.cleaned_data[
        "candidate_name"
    ]

    resume_file = form.cleaned_data[
        "resume_file"
    ]

    job_description = form.cleaned_data[
        "job_description"
    ]

    try:

        resume_text = extract_text_from_pdf(
            resume_file
        )

    except Exception:

        form.add_error(
            "resume_file",
            "Unable to read this PDF. Please upload "
            "a valid, text-based PDF resume."
        )

        return render(
            request,
            "analyzer/home.html",
            {
                "form": form
            }
        )

    if not resume_text.strip():

        form.add_error(
            "resume_file",
            "No readable text was found in this PDF."
        )

        return render(
            request,
            "analyzer/home.html",
            {
                "form": form
            }
        )

    resume_skills = extract_skills(
        resume_text
    )

    required_skills = extract_skills(
        job_description
    )

    match_result = calculate_skill_match(
        resume_skills,
        required_skills
    )

    recommendations = []

    for skill in match_result["missing_skills"]:

        recommendations.append(
            f"Learn and practice {skill}."
        )

    if not required_skills:

        recommendations.append(
            "No supported technical skills were detected "
            "in the job description. Review the description "
            "or expand the skill dictionary."
        )

    elif not recommendations:

        recommendations.append(
            "All skills recognized by the current "
            "dictionary were matched. Review the full "
            "job requirements before applying."
        )

    analysis = SkillAnalysis.objects.create(

        candidate_name=candidate_name,

        resume_file=resume_file,

        job_description=job_description,

        matched_skills=match_result[
            "matched_skills"
        ],

        missing_skills=match_result[
            "missing_skills"
        ],

        resume_skills=resume_skills,

        required_skills=required_skills,

        match_score=match_result[
            "match_score"
        ],

        recommendations=recommendations,
    )

    return render(
        request,
        "analyzer/result.html",
        {
            "analysis": analysis
        }
    )