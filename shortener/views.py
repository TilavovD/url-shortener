from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
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
            return HttpResponse("%s" % random_combination)
    else:
        form = LinkForm()
    return render(request, "shortener/home.html", {'form': form})
