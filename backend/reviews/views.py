# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from .models import Review


# #Volunteer View for Displaying Reviews
# @login_required
# def volunteer_reviews(request):
#     reviews = Review.objects.filter(volunteer=request.user)  # Get reviews by the logged-in user
#     return render(request, 'reviews/volunteer_reviews.html', {'reviews': reviews})



# #admin analytics
# from django.db.models import Count

# @login_required
# @user_passes_test(lambda user: user.is_superuser)  # Ensure only admins can access
# def admin_analytics(request):
#     # Count the number of reviews submitted by each volunteer
#     volunteer_review_counts = Review.objects.values('volunteer').annotate(review_count=Count('id'))
    
#     return render(request, 'reviews/admin_views.html', {'volunteer_review_counts': volunteer_review_counts})
