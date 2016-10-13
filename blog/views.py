from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from . import models
from .models import Entry, Category, Tag
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.db.models import Q


class BlogIndex(generic.ListView):

    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return models.Entry.objects.filter(
                                                Q(title__icontains=query)|
                                                Q(body__icontains=query)|
                                                Q(categorys__name__icontains=query) |
                                                Q(tags__name__icontains=query)
                                                )
        else:
            return models.Entry.objects.published()


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"


def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')


class CategoryView(generic.ListView):
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        return models.Entry.objects.filter(categorys__name=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        return context


class TagView(generic.ListView):
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        return models.Entry.objects.filter(tags__name=self.kwargs['tag_id'])

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        return context
