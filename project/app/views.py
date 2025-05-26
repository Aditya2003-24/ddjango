from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse,JsonResponse

# Create your views here.

def student_list(request):
    stu=Student.objects.all()
    serializer=Studentserializers(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def student_detail(request,pk):
    user=Student.objects.get(pk=pk)
    serializer=Studentserializers(user)
    return JsonResponse(serializer.data,safe=False)