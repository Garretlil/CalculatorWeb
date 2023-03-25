from django.http.request import HttpRequest
from django.shortcuts import render_to_response,render

from Calc.templates import*



def index (request):
    if request.method=='GET':
      name="empty for a while"
      return render(request, 'testpage.html',{"namefrompython":name})
    if request.method=='POST':
      name=request.POST.get("name")+"frompython"
      return render(request, 'testpage.html',{"namefrompython":name})

def Calculate (request):
     if request.method=='GET':
        return render(request, 'firstpage.html',)
     if request.method=='POST':
      num1=int(request.POST.get("num1")) 
      num2=int(request.POST.get("num2"))
      znak=request.POST.get("btnfld")
      result=0
      if znak=="+":
         result=num1+num2
      elif znak=="-":
          result=num1-num2
      elif znak=="*":
          result=num1*num2
      elif znak=="/":
          result=num1/num2
      return render(request, 'firstpage.html',{"num1":num1,"num2":num2,"result":result})
# Create your views here.
