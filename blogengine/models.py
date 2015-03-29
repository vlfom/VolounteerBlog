from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template import defaultfilters
from unidecode import unidecode

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = defaultfilters.slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = defaultfilters.slugify(unidecode(self.name))
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

    def __unicode__(self):
        return self.name

class Delivery(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    delivery_date = models.DateTimeField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    site = models.ForeignKey(Site)
    author = models.ForeignKey(User, related_name='delivery_author')
    recipients = models.ManyToManyField(User, blank=True, null=True, related_name='delivery_recipients')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = original = defaultfilters.slugify(unidecode(self.title))
            number = 0
            print original
            while True:
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                number += 1
                self.slug = '%s-%d' % (original, number)
        super(Delivery, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-delivery_date"]

class Post(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    site = models.ForeignKey(Site)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    author = models.ForeignKey(User, related_name='post_author')
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='post_subscribers')

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = original = defaultfilters.slugify(unidecode(self.title))
            number = 0
            print original
            while True:
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                number += 1
                self.slug = '%s-%d' % (original, number)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username