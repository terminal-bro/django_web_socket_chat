from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat_box(request,chat_box_name):
    return render(request,"chatbox.html",{"chat_box_name":chat_box_name})