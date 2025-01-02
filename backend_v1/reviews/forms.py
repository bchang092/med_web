from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Review_Content', 'Rating', 'Department']  # Allow users to submit content for their review
        
        # Defining area of the review box
        widgets = {
            'Review_Content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
    
    # Add validation for the 'Rating' field
    Rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 10})
    )
