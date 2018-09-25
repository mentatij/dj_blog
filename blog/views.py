from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View

from .forms import PostForm, TagForm
from .models import Post, Tag
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostsListView(ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(ObjectCreateMixin, View):
    model_form = PostForm
    template_name = 'blog/post_create_form.html'


class PostUpdateView(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template_name = 'blog/post_update_form.html'


class PostDeleteView(ObjectDeleteMixin, View):
    model = Post
    template_name = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'


class TagsListView(ListView):
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TagDetailView(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'


class TagCreateView(ObjectCreateMixin, View):
    model_form = TagForm
    template_name = 'blog/tag_create_form.html'


class TagUpdateView(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template_name = 'blog/tag_update_form.html'


class TagDeleteView(ObjectDeleteMixin, View):
    model = Tag
    template_name = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
