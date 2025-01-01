from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Review, volunteer #imported models 
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from io import BytesIO
import base64
from textblob import TextBlob
from django.utils.html import format_html
from django.utils.safestring import mark_safe


#register the classes to enable CRUD operations (create, read, update, delete)
admin.site.register(volunteer)

class ReviewAdmin(admin.ModelAdmin):
    # **Display fields as columns**
    list_display = ('Volunteer','Volunteer_First_Name','Volunteer_Last_Name', 'Rating', 'Date_Submitted','Department', 'Sentiment','Review_Content','Admin_Response')  # Columns to display
    
    # Enable filtering options
    list_filter = ('Rating', 'Sentiment', 'Department', 'Date_Submitted')  # Add filter options
    
    # Editable option for admin
    list_editable = ('Admin_Response',)  # Allow inline editing of responses

    # **Enable sorting by columns**
    ordering = ('-Date_Submitted',)  # Default sorting (newest first)
    
    # **Search box for filtering by text fields**
    search_fields = ('id', 'Volunteer', 'Rating', 'Date_Submitted','Department', 'Sentiment','Review_Content')
    # search_fields = ('Review_Content', 'Volunteer')  # Search in content and volunteer's username

    # **Enable pagination (optional)**
    list_per_page = 20  # Show 20 reviews per page

    # Enable clickable rows (detail view)
    list_display_links = ('Volunteer',)  # Clicking these fields opens the detail view
    
    # Read-only fields (for viewing)
    # readonly_fields = ('id', 'Volunteer', 'Rating', 'Date_Submitted', 'Review_Content')

     # Add a button above the table
    change_list_template = "admin/review_change_list.html"  # Custom template for adding the button

###############################################################################################
################### Graphical Display of Reviews ##############################################
###############################################################################################

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('review-stats/', self.admin_site.admin_view(self.review_stats), name="review-stats"),
        ]
        return custom_urls + urls

    #view to render the new page 
    def review_stats(self, request):
        # Get data
        reviews = Review.objects.all()
        df = pd.DataFrame(list(reviews.values('Rating', 'Department', 'Sentiment')))

        # Overall satisfaction (Gauge Chart)
        avg_rating = df['Rating'].mean()
        satisfaction_label = 'Excellent' if avg_rating >= 8 else 'Good' if avg_rating >= 6 else 'Average' if avg_rating >= 4 else 'Poor'

        # Gauge Chart
        fig1 = px.pie(
            values=[avg_rating, 10 - avg_rating],
            names=['Satisfaction', 'Remaining'],
            title=f"Overall Satisfaction: {satisfaction_label}",
            color_discrete_sequence=['green', 'lightgray']
        )
        graph1 = fig1.to_html()

        # Department Ratings
        dept_avg = df.groupby('Department')['Rating'].mean().reset_index()
        fig2 = px.bar(dept_avg, x='Department', y='Rating', title="Department-wise Ratings", color='Rating')
        graph2 = fig2.to_html()

        # # Sentiment Analysis
        # sentiment_counts = df['Sentiment'].value_counts().reset_index()
        # fig3 = px.pie(sentiment_counts, values='Sentiment', names='index', title="Sentiment Analysis")
        # graph3 = fig3.to_html()

        # Render template with graphs
        return TemplateResponse(request, "admin/review_stats.html", {
            'title': 'Review Analytics',
            'graph1': graph1,
            'graph2': graph2,
            # 'graph3': graph3,
        })
    

# Register the model with the customized admin view
admin.site.register(Review, ReviewAdmin)