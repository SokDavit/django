from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members' : members,
        'firstname': 'sokdavit',
        'greeting' : 1,
    }
    return HttpResponse(template.render(context , request))

def show(request, id):
    detail = Member.objects.get(id=id)
    template = loader.get_template('show.html')
    context = {
        'detail' : detail,
        'members_id' : id,
    }
    return HttpResponse(template.render(context , request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
