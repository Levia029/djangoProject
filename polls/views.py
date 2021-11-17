from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('这里是liujiangblog的投票站点')

# Create your views here.
