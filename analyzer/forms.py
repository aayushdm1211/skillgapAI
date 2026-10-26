from django import forms


class SkillAnalysisForm(forms.Form):

    candidate_name = forms.CharField(
        max_length=100,
        required=False,
        label="Your Name"
    )

    resume_file = forms.FileField(
        label="Upload Resume (PDF)"
    )

    job_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "placeholder": (
                    "Paste the complete job description here..."
                ),
            }
        ),
        label="Job Description"
    )

    def clean_resume_file(self):

        resume = self.cleaned_data["resume_file"]

        if not resume.name.lower().endswith(".pdf"):

            raise forms.ValidationError(
                "Please upload a PDF resume."
            )

        if resume.size > 5 * 1024 * 1024:

            raise forms.ValidationError(
                "Resume size must not exceed 5 MB."
            )

        return resume