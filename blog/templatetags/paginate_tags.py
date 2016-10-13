from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()


@register.simple_tag(takes_context=True)
def Tag(context):
    request = context['request']
    address = request.session['address']
    return {'address':address}