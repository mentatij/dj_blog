from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from transliterate import translit


def get_slug(title):
    title = translit(title, reversed=True)
    new_slug = slugify(title)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_pub']

    def get_absolute_url(self):
        return reverse('post_detail_url', args=(self.slug,))

    def get_update_url(self):
        return reverse('post_update_url', args=(self.slug,))

    def get_delete_url(self):
        return reverse('post_delete_url', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', args=(self.slug,))

    def get_update_url(self):
        return reverse('tag_update_url', args=(self.slug,))

    def get_delete_url(self):
        return reverse('tag_delete_url', args=(self.slug,))
