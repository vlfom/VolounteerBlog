from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogengine import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial_blog_ng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blogengine.urls', namespace='blogengine')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
    url(r'^register/$', views.register, name='register'),
    url(r'', include('blogengine.urls')),
)