from django.shortcuts import render
# from django.http import HttpResponse
import datetime

def view_home(request, *args, **kwargs):
    print("Logged as:", request.user, "!")
    return render(request, "home.html", {'date': datetime.date})

