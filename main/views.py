from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import MainInfo
import json

@csrf_exempt
def mainREST(request):
    if request.method == 'GET':
        return HttpResponse(getRequest(), content_type="application/json")
    elif request.method == 'POST':
        return HttpResponse(postRequest(request), content_type="application/json")

def postRequest(req):
    post_body = json.loads(req.body)
    try:
        temp_db = MainInfo(img=post_body['img'], title=post_body['title'], text=post_body['text'])
        temp_db.save()
        return 'done'
    except Exception as err:
        return err

def getRequest():
    data_from = MainInfo.objects.all()
    send_from = []
    for info in data_from:
        send_from.append({
            'img': info.img,
            'title': info.title,
            'text': info.text})
    return json.dumps(send_from)
