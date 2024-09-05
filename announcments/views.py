from django.shortcuts import render

def portfolio(request):
    return render(request, 'announcments/index.html')
