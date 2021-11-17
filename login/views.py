from django.shortcuts import render
from login import models
# Create your views here.
#user_list = []

#定义一个主页请求
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user=username, pwd=password)
        #print(username, password)
        #tmp = {'user':username, 'pwd':password}
    user_list = models.UserInfo.objects.all()
    # return HttpResponse("Hello World!")
    return render(request, 'index.html', {'data': user_list})
