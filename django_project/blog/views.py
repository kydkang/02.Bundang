from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Author, Tag, Category, Post 
from django.contrib import messages
from .forms import FeedbackForm
from django.core.mail import mail_admins
from django_project import helpers

def index(request):
    return HttpResponse("Hello Django")

def post_list(request):
    posts = Post.objects.order_by("-id").all()
    posts = helpers.pg_records(request, posts, 3)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk, post_slug):    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, posts, 3)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)

def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, posts, 3)   
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )

def test_redirect(request):
    return redirect('post_list')


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(
                           f.cleaned_data['subject'],  
                           f.cleaned_data['message'])                                                                     
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})




