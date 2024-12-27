#form to handle review submission

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_content']  # Allow users to submit content for their review
