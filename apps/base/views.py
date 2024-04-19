from django.shortcuts import render
from .utilits import send_mail_code
# Create your views here.

def index(request):
    # send_mail_code('toshniyozovogabek0627@gmail.com', 111222)
    return render(request, "home.html", {})
