#form to handle review submission

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Review_Content','Rating', 'Department']  # Allow users to submit content for their review
        
        #defining area of the review box 
        widgets = {
            'Review_Content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }