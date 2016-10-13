from django.db.models.aggregates import Count
from .models import Category, Entry, Tag


def sidebar(request):
    tag_list_temp = [ ]
    category_list_temp = [ ]

    queryset = Entry.objects.published()
    for object in queryset:
        tag_list_temp.append(object.tags.name)
        category_list_temp.append(object.categorys)

    tag_list = { x : tag_list_temp.count(x) for x in tag_list_temp }
    tag_list = tag_list.items()

    category_list = { x : category_list_temp.count(x) for x in category_list_temp }
    category_list = category_list.items()

    return {
        'tag_list': tag_list,
        'category_list': category_list
    }