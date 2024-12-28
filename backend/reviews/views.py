from django.shortcuts import render

def volunteer_page(request):
    # Your view logic here (e.g., fetching data related to volunteer)
    return render(request, 'volunteer/volunteer_home_page.html')
