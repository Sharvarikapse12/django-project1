from django.shortcuts import render

def header(request):
    return render(request , 'layout/header.html')