from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from textblob import TextBlob
from .models import Review


@login_required
def volunteer_page(request):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #saving detials of volunteer 
            review = form.save(commit=False)
            review.Volunteer = request.user
            review.Volunteer_First_Name = request.user.first_name
            review.Volunteer_Last_Name = request.user.first_name
            
            #sentiment analysis: 
            review_content = form.cleaned_data['Review_Content']
            blob = TextBlob(review_content)
            polarity = blob.sentiment.polarity
            review.Sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'

            review.save()

            #fetch the reviews for list
            user_reviews = Review.objects.filter(Volunteer=request.user)
            context = {
                'form': form,
                'user_reviews': user_reviews,
            }

            return redirect('volunteer_page') #redirect after submission
            
    else:
        form = ReviewForm()

    # For GET request (page load), fetch and pass the reviews
    reviews = Review.objects.filter(Volunteer=request.user).order_by('-Date_Submitted')
    #view page 
    return render(request, 'volunteer/volunteer_home_page.html', {'reviews': reviews})
