from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
#def index(request):
#    return HttpResponse("hello world says by ale and tango <a href='/rango/about'>:About</a>")

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict ={'categories':category_list}
    # context_dict = {'boldmessage': "I am bold fonrt from the context"}
    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render_to_response('rango/index.html', context_dict, context)

#def about(request):
#    return HttpResponse("hi, this is about page, still not finished <a href='/rango/'>Index</a>")

def about(request):
    return render_to_response('rango/about.html')


def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_',' ')
    context_dict = {'category_name': category_name}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category']= category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict , context)
