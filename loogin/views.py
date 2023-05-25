from django.shortcuts import render, redirect
from django.http import HttpResponse
from loogin.models import Followers
from django.contrib.auth.models import User
# Create your views here.
def register_html(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(full_name)
        print(email)
        if password1 != password2:
            return HttpResponse("password xato")

        Followers.objects.create(
            full_name=full_name,
            email=email,
            password=password2
        )

        return redirect("/loogin")
    return render(request, "register.html")

def loogin_html(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        if Followers.objects.filter(full_name=username,password=password).exists():
            return HttpResponse("Saytimizga Xush Kelibsz : 🤗 ")
        else:
            return HttpResponse("username yoki password xato kiritilgan: ")

    return render(request, "login.html")







