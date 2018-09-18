from django.shortcuts import render
from django.apps import apps
from datetime import datetime


def index(request):
    year = datetime.now().year
    bookmarks = []
    for app in apps.get_app_configs():
       bookmarks.append(app.verbose_name)
    i = bookmarks.index("Lab1")
    return render(
        request,
        'index.html',
        context={'year': year, 
        'bookmarks': bookmarks[i:],
        'active': 'Lab1'}
    )