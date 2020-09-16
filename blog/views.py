from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'

    success_url = reverse_lazy('blog:list')


class BlogListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author_id=self.request.user.pk).order_by('-updated_at')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = '__all__'

    success_url = reverse_lazy('blog:list')


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog

    success_url = reverse_lazy('blog:list')


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

