from django.shortcuts import render
import numpy
from Det.templates import*


def CalcDet(request):
    if request.method=='GET':
       return render(request, 'forDet.html',)
    if request.method=='POST':
      num1=int(request.POST.get("num1")) 
      num2=int(request.POST.get("num2"))
      
      return render(request, 'firstpage.html',{"num1":num1,"num2":num2,"result":result})
# Create your views here.
