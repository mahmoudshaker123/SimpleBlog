from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request , 'blog/post_list.html' , {'posts':posts} )