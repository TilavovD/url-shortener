from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from django.conf import settings
from .forms import LinkForm
from .models import Link
import random


# Create your views here.
@require_http_methods(['GET', 'POST'])
def shortify(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
            random.shuffle(bank)
            random_combination = "".join(bank[:6])
            while Link.objects.filter(title=random_combination):
                random.shuffle(bank)
                random_combination = "".join(bank[:6])

            Link.objects.create(title=random_combination, link=form.cleaned_data['link'])
            link = f'{settings.HOST}/{random_combination}'
            return render(request, 'shortener/result.html', {'result': link})
    else:
        form = LinkForm()
    return render(request, "shortener/home.html", {'form': form})

@require_GET
def link_match(request, link):
    try:
        obj = Link.objects.get(title=link)
        return redirect(obj.link)
    except Link.DoesNotExist:
        return HttpResponse("404 Not Found")

