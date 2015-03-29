# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from blogengine.models import Category, Tag
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from forms import *
from django.contrib.sites.models import get_current_site
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage

class CategoryListView(ListView):
    template_name = 'blogengine/category_post_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['category'] = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            context['category'] = None
        return context

class TagListView(ListView):
    template_name = 'blogengine/tag_post_list.html'
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_subscribe(request, pub_date__year, pub_date__month, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        post.subscribers.add( request.user )
    except:
        pass
    post.save()
    return redirect('/' + pub_date__year.__str__() + "/" + pub_date__month.__str__() + "/" + slug.__str__())

@login_required
def getSearchResults(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    if query:
        results = Post.objects.filter(Q(tags__name__icontains=query))
    else:
        results = []
    pages = Paginator(results, 5)
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    return render_to_response('blogengine/search_post_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.site_id = get_current_site(request).id
            post.save()
            return redirect(post.get_absolute_url(), pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogengine/post_edit.html', {'form': form })

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'blogengine/user_register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Your account is blocked.', content_type='charset=utf-8')
        else:
            return HttpResponse("Wrong login or password.", content_type='charset=utf-8')
    else:
        return render_to_response('blogengine/user_login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')