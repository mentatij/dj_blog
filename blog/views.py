from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .forms import TagForm
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


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', {'form': bound_form})
