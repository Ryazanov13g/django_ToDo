from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from posts.forms import PostCreateForm
from posts.models import Post


class IndexView(TitleMixin, TemplateView):
    template_name = 'posts/index.html'
    title = 'ToDo'


class PostsListView(TitleMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'
    title = 'ToDo - Напоминания'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostCreateView(TitleMixin, CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    title = 'ToDo - Создание заметки'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts:posts_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(TitleMixin, UpdateView):
    model = Post
    template_name = 'posts/post_create.html'
    title = 'ToDo - Изменение заметки'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts:posts_list')

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


def not_actuality(request):
    Post.post_not_actuality(user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
