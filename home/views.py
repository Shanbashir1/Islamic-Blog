from django.shortcuts import render


def index(request):
    """A View to return the Index Page"""

    return render(request, 'home/index.html')
