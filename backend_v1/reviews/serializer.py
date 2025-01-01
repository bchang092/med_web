from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class meta: 
        model = Review #specifies the model in model.py to serialize
        fields = ['id', 'Rating', 'Volunteer', 'Department', 'Review_Content', 'Date_Submitted', 'Sentiment', 
                  'Volunteer_First_Name', 'Volunteer_Last_Name', 'Admin_Response']
        #fields that aren't manually inputted in review
        read_only_fields = ['Date_Submitted', 'Volunteer_First_Name', 'Volunteer_Last_Name', 'Sentiment']
