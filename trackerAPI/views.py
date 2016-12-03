from django.shortcuts import render
from django.http import JsonResponse
from .getCategories import getCategories

def listings(request, filters=None, category=None, location=None):
    if None in [filters,category,location]:
        return JsonResponse({
            'listings':[
                {
                    'title':'Canadian flag',
                    'link':'http://www.kijiji.ca/',
                    'image':'https://www.google.ca/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                    'price':10,
                    'arunislying':'arunisdefinitelylying',
                },
                {
                    'title':'Canadian flag',
                    'link':'http://www.kijiji.ca/',
                    'image':'https://www.google.ca/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                    'price':10,
                    'arunislying':'arunisdefinitelylying',
                },
                {
                    'title':'Canadian flag',
                    'link':'http://www.kijiji.ca/',
                    'image':'https://www.google.ca/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                    'price':10,
                    'arunislying':'arunisdefinitelylying',
                },
        ]})

    return JsonResponse({
        'filters':filters,
        'category':category,
        'location':location
    })

def categories(request):
    categories = getCategories()
    return JsonResponse({'categories':categories})

def locations(request):
    return JsonResponse({'request':'GET', 'locations':['Ottawa','Toronto']})

def landing(request):
    return JsonResponse({'request':'GET', 'results':[]})
