from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json

# Create your views here.

class home(APIView):
    def get(self,request, *args, **kwargs):
        body = request.data
        print(body)
        body = json.loads(body)
        data={}
        #data['headers']= request.headers
        data['content']=request.content_type 
        data['header'] =dict(request.headers)   
        return JsonResponse(data)