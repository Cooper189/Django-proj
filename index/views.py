from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from index.models import News
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

firstIf = True
obj = {
    'first': 'First if working',
    'double': 'Double els'
}

def someDate():
    myList = []
    testVar = News.objects.all()
    for user in testVar:
        myList.append(user.title)

    return myList

def index(request):
    return HttpResponse(json.dumps(someDate()), content_type="application/json")

@csrf_exempt
def setKo(request):
    python_obj = json.loads(request.body)
    q = News(newsId = python_obj['img'], title = python_obj['title'])
    q.save()
    return HttpResponse()
