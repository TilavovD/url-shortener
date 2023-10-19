from django.shortcuts import render


# Create your views here.
def shortify(request):
    return render(request, "shortener/home.html")
