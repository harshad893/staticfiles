from django.shortcuts import render

# Create your views here.

def bird(request):
    return render(request,'static_files.html')