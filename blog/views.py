from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            },
        )
