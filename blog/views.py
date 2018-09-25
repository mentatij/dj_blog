from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Tag


class PostsListView(ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class TagsListView(ListView):
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TagDetailView(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'


# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/posts_list.html', {'posts': posts})
#
#
# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
#
# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blog/tags_list.html', {'tags': tags})
#
#
# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', {'tag': tag})
