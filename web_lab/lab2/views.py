from django.shortcuts import render
from datetime import datetime
from django.apps import apps
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.debug("Calling index view from lab2 app")
    year = datetime.now().year
    bookmarks = []
    for app in apps.get_app_configs():
       bookmarks.append(app.verbose_name)
    i = bookmarks.index("Lab1")
    return render(
        request,
        './lab2.html',
        context={'year': year, 
        'bookmarks': bookmarks[i:],
        'active': 'Lab2'}
    )
