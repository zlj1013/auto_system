from django.shortcuts import render
from .models import Program
# Create your views here.

def getProgram(request):
    all_messages=Program.objects.all()
    #part_messages=Program.objects.filter(pro_name="保险系统")
    for message in all_messages:
        print(message.pro_name)
    #return render(request,'message.html')