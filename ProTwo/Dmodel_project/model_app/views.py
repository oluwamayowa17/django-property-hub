from django.shortcuts import render
from django.contrib.auth.models import User
# from model_app.models import UserProfile,Category,
from model_app.models import *
# Create your views here.
def myIndex(request):
    mydata = User.objects.all()
    return render(request, 'index.html', {'mycontext':mydata})