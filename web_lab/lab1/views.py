from django.shortcuts import render
from django.apps import apps
from datetime import datetime
from django.http import JsonResponse
import requests 


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


def http_response(response):
    return 'HTTP/1.1 {} {}\r\n{}\r\n\r\n'.format(
        response.status_code, response.reason , 
        '\r\n'.join(k + ': ' + v for k, v in response.headers.items())
    )


def send(request):
    if request.method == "POST":
        data = request.POST
        url = data['url']
        method = data['method']

        if method == '1': # GET
            r = requests.get(url)
        elif method == '2': # POST
            r = requests.post(url) 
        elif method == '3': # DELETE
            r = requests.delete(url)
        elif method == '4': # PUT
            r = requests.put(url)
        elif method == '5': # OPTIONS
            r = requests.options(url)
        elif method == '6': # HEAD 
            r = requests.head(url)

        headers = http_response(r).replace("\n", "<br >")
        content = r.content
        
        return JsonResponse({"status": "ok", "headers": headers, "content": content})
    else: 
        return JsonResponse({"error": "invalid method"})
