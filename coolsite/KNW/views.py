from django.http.request import HttpRequest
from django.shortcuts import render_to_response,render

from KNW.templates import*
def Open(request):
    if request.method=='GET':
      return render(request, 'Page.html')
