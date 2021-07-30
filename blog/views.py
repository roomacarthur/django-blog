from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# when creating new views we need to do three things:
# 1. Create the view code.
# 2. Create a template to render the view.
# 3. Connect up our URLs in the urls.py file.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # paginate = limiting the list to 6 on homepage, if more than 6
    # Django will auto add navigation. 
    paginate_by = 6
