from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



# Create your views here.

def index(request):

    return render(request, 'home.html')


def count(request):
    # if request.Get['option_count']:
    if "option_count" in request.GET:
        print(request.GET)
        data = request.GET['ourtext']
        list_data = data.split()
        length = len(list_data)
        context = {
            'text_lenght':length,
            'option':request.GET["option_count"]
        }
        return render(request, 'count.html',context)
    else:
        return HttpResponse('<h1>BOX NOT CHECKED</h1>')