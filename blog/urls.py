from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^tag/(?P<tag_id>[\w-]+)/$', views.TagView.as_view(), name="tag"),
    url(r'^category/(?P<category_id>[\w-]+)/$', views.CategoryView.as_view(), name="category"),
)