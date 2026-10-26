from django.db import models


class SkillAnalysis(models.Model):

    candidate_name = models.CharField(
        max_length=100,
        blank=True
    )

    resume_file = models.FileField(
        upload_to="resumes/"
    )

    job_description = models.TextField()

    matched_skills = models.JSONField(
        default=list
    )

    missing_skills = models.JSONField(
        default=list
    )

    resume_skills = models.JSONField(
        default=list
    )

    required_skills = models.JSONField(
        default=list
    )

    match_score = models.FloatField(
        default=0
    )

    recommendations = models.JSONField(
        default=list
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"Analysis {self.id} - "
            f"{self.candidate_name or 'Candidate'}"
        )