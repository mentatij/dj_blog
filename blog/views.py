from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm, TagForm
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostsListView(ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(ObjectDetailMixin, View):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template_name = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template_name = 'blog/post_update_form.html'
    raise_exception = True


class PostDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template_name = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class TagsListView(ListView):
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TagDetailView(ObjectDetailMixin, View):
    model = Tag
    template_name = 'blog/tag_detail.html'


class TagCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template_name = 'blog/tag_create_form.html'
    raise_exception = True


class TagUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template_name = 'blog/tag_update_form.html'
    raise_exception = True


class TagDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template_name = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
