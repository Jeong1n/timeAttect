from django.shortcuts import render
from .models import UserModel



def base_response(request):
    return render(request,"index.html")


from django.shortcuts import render
import hashlib
# Create your views here.

class user:
    def __init__(self,password,email,):
        self.email = email
        self.name = password


def signup(request):
    if request.method == 'GET':
        return render(request, 'timeattcet')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        new_user = UserModel()
        new_user.password = password
        new_user.bio = email
        new_user.save()
