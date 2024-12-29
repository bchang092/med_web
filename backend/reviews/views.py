from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from textblob import TextBlob


@login_required
def volunteer_page(request):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #if a logged in user is attached to the review
            review = form.save(commit=False)
            review.Volunteer = request.user
            #save the name of volunteer
            review.Volunteer_First_Name = request.user.first_name
            review.Volunteer_Last_Name = request.user.first_name
            
            #sentiment analysis: 
            review_content = form.cleaned_data['Review_Content']
            blob = TextBlob(review_content)
            polarity = blob.sentiment.polarity
            if polarity > 0:
                review.Sentiment = 'Positive'
            elif polarity < 0:
                review.Sentiment = 'Negative'
            else:
                review.Sentiment = 'Neutral'

            review.save()
            return redirect('volunteer_page') #redirect after submission
    else:
        form = ReviewForm()

    #view page 
    return render(request, 'volunteer/volunteer_home_page.html', {'form': form})
