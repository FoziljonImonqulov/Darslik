from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Foziljon Imonqulov',
        'content': 'First post',
        'title': 'Amazing',
        'posted_data': '2023-08-13'
    },
    {
        'author': 'Qobiljon Imonqulov',
        'content': 'Second post',
        'title': 'Yesterday is history',
        'posted_date': '2023-08-14'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
