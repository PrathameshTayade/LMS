from django.shortcuts import render ,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import books
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        fname = request.POST["fname"]

        lname = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        passwd = request.POST["passwd"]

    user = User.objects.create_user(username=username, email=email, password=passwd, first_name=fname, last_name=lname)
    user.save()
    print("saved")
    return render("home.html")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:

        username = request.POST["username"]
        passwd = request.POST["password"]
        print(username)
        print(passwd)
        user = auth.authenticate(username=username,  password=passwd)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return render(request ,"home.html")
        else:
            messages.info(request,"Wrong Credentials")
            print("login failde")
            return render(request, "signin.html")



def showallbooks(request):
    b = books.objects.all()
    dict = {'books' : b}
    return render(request,"showallbooks.html", dict)

def insertbook(request):
    if request.method == "POST":
        bname = request.POST['bookname']
        aname = request.POST['authorname']
        edition = request.POST['edition']
        b = books(book_name = bname, author_name = aname, edition = edition)
        b.save()
        return render(request,"home.html")

    else:
        return render(request,"insertbook.html")


def home(request):
    return render(request,"home.html")
