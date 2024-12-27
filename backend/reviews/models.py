from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class volunteer(models.Model):
    #volunteer attributes
    vol_fname = models.CharField(max_length =50, help_text = "First Name") 
    vol_lname = models.CharField(max_length =50, help_text = "Last Name") 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 255, unique = True)
    is_active = models.BooleanField(default=True)  # write a mechanism to check if active based on posts

    #returns string representing model object
    def __str__(self):
        return f'{self.vol_lname}, {self.vol_fname}' 
    
    #returns url for particular volunteer instance
    def get_absolute_url(self):
        return reverse('volunteer-detail', args=[str(self.id)])



class Review(models.Model):
    #attribute notes: if volunteer gets deleted, cascade deletes all reviews
    rating = models.IntegerField(help_text = "Rating")
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # one to many relationship: one user can make many reviews
    department = models.CharField(max_length = 50, help_text = 'Department')
    review_content = models.TextField(help_text="Your Review")  # Store the review content (text)
    date_submitted = models.DateTimeField(auto_now_add=True)  # Automatically set the current date/time when the review is created


    #return url to particular review 
    def get_absolute_url(self):
        return reverse('review-details', args=[str(self.id)])
    
    #returns string representing review object
    def __str__(self):
        return f'{self.department}, {self.rating}, {self.date_submitted}' 
    
    class Meta:
        ordering = ['date_submitted','-rating']

        #these permissions can be later defined in admin
        permissions = [('can_create_review','Can create a review'),
                       ('can_edit_review,','Can edit a review'),
                        ('can_view_review','Can view reviews')]

   



