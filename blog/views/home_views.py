from django.shortcuts import render

def renderHOme(request):
 return render(request, 'home/index.html')