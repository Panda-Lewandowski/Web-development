from django.shortcuts import render
from django.apps import apps
from datetime import datetime
from django.http import JsonResponse, HttpResponse, QueryDict
from .models import Todo
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime
from urllib.parse import parse_qs
import requests 
import json

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
        content = r.content.decode("utf-8").replace("<", "&lt")
        content.replace(">", "&gt")
        
        return JsonResponse({"status": "ok", "headers": headers, "content": content})
    else: 
        return JsonResponse({"error": "invalid method"})


@csrf_exempt
def api(request):
    if request.method == "POST":
        data = request.POST 
        try:
            date = data['date']
            text = data['task']
        except MultiValueDictKeyError:
            return JsonResponse({'status': 'error', 'text': 'The query must contain data of the form date = & task ='})
        else:
            new_task = Todo(task=text, deadline=datetime.strptime(date, "%d.%m.%Y"))
            new_task.save()
            return HttpResponse(status=201)
    elif request.method == "GET":
        params = request.GET
        if len(params) == 0:
            data = Todo.objects.all()
        else:
            data = Todo.objects.filter(id__exact=params['id'])
        return JsonResponse({'todo': list(data.values())})
    elif request.method == "DELETE":
        if request.META['QUERY_STRING'] == '':
            return JsonResponse({'status': 'error', 'text': 'Please, send id via query string!'})
        else:
            obj_id = parse_qs(request.META['QUERY_STRING'])['id'][0]
            obj = Todo.objects.filter(id__exact=obj_id)
            if len(obj) == 0:
                return JsonResponse({'status': 'error', 'text': 'Invalid id'})
            else:
                obj.delete()
                return HttpResponse(status=200)
    elif request.method == "PUT":
        if request.META['CONTENT_TYPE'] != 'application/x-www-form-urlencoded':
            return JsonResponse({'status': 'error', 'text': 'Please, send body request as urlencoded!'})
        else:
            data = request.body.decode() 
            data = parse_qs(data)
            try:
                obj_id = data['id'][0]
                field = data['field'][0]
                value = data['value'][0]
            except MultiValueDictKeyError:
                return JsonResponse({'status': 'error', 'text': 'The query must contain data of the form id = & filed = & value= '})
            else:
                obj = Todo.objects.filter(id__exact=obj_id)
                if len(obj) == 0:
                    return JsonResponse({'status': 'error', 'text': 'Invalid id'})
                else:
                    if field == 'task':
                        obj.task = value
                    elif field == 'date':
                        obj.date = datetime.strptime(date, "%d.%m.%Y")
                    else: 
                        return JsonResponse({'status': 'error', 'text': 'Invalid field'})
                    obj.save()
            return HttpResponse()
    elif request.method == "OPTIONS":
        response = HttpResponse()
        response['Allow'] = 'POST, GET, DELETE, PUT, OPTIONS, HEAD'
        return response
    elif request.method == "HEAD":
        return HttpResponse()