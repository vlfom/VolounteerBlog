from django.conf.urls import patterns, url
from blogengine.views import *
from . import views
from django.views.generic import DetailView
from django.contrib.sitemaps.views import sitemap
from blogengine.sitemap import PostSitemap, FlatpageSitemap

# Define sitemaps
sitemaps = {
    'posts': PostSitemap,
    'pages': FlatpageSitemap
}

urlpatterns = patterns('',
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'),
    url(r'^(?P<pub_date__year>\d{4})/'
        r'(?P<pub_date__month>\d{1,2})/'
        r'(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        ),
        name='post'),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$',
        CategoryListView.as_view(
            paginate_by=5,
            model=Category,
        ),
        name='category'),
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$',
        TagListView.as_view(
            paginate_by=5,
            model=Tag,
        ),
        name='tag'),
    url(r'^search', 'blogengine.views.getSearchResults', name='search'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)