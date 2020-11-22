from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Blog, Topic, Post
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count

@login_required

def home(request):
    blogs = Blog.objects.all()
    topics = Topic.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, 'topics': topics})
