from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)
    slug = models.SlugField(max_length=200, unique=True,null = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Tags"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag": self.name})


class Category(models.Model):
    name = models.CharField(max_length=200, null = True)
    slug = models.SlugField(max_length=200, unique=True,null = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Clasifications"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category": self.name})



class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True,null = True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    categorys = models.ForeignKey('Category', blank=True, null = True)
    tags = models.ForeignKey('Tag', blank=True, null = True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

