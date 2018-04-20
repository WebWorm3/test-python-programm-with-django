from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    new_data = database(System=body['system'])
    new_data.save()

    success_data = 'Added new system!';
    return JsonResponse(success_data, safe=False)
