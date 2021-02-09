from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'kclaudine',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#      {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


context = {
    'posts' : Post.objects.all()
}
def home(request):
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})