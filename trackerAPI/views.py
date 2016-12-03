from django.shortcuts import render
from django.http import JsonResponse

def listings(request, filters='', category='', location=''):
    return JsonResponse({
        'filters':filters,
        'category':category,
        'location':location
    })

def categories(request):
    return JsonResponse({'request':'GET', 'categories':['shoes','shirts']})

def locations(request):
    return JsonResponse({'request':'GET', 'locations':['Ottawa','Toronto']})

def landing(request):
    return JsonResponse({'request':'GET', 'results':[]})
