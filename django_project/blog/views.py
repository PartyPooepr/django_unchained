from django.shortcuts import render

posts = [
    {
        'author':'Pooepr',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'March 27, 2025'
    },
    {
        'author':'sportole',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 12, 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
