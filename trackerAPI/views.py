from django.shortcuts import render
from django.http import JsonResponse

def listings(request):
    # if this is a POST request we need to process the request
    if request.method == 'POST':
        return JsonResponse({'request':'POST'})

    # if a GET (or any other method) we'll return the default values
    return JsonResponse({'request':'GET', 'link':'http://www.rona.ca/images/7402004_L.jpg', 'price':10, 'title':'Canadian flag'})

def categories(request):
    return JsonResponse({'request':'GET', 'categories':['shoes','shirts']})

def locations(request):
    return JsonResponse({'request':'GET', 'locations':['Ottawa','Toronto']})

def landing(request):
    return JsonResponse({'request':'GET', 'results':[]})
