from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
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


@csrf_exempt
def student_api(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=Studentserializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
