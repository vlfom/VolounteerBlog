# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Post, User, UserProfile

FIELD_NAME_MAPPING = {
    'title': 'Назва',
    'text': 'Текст',
    'category': 'Категорія',
    'tags': 'Теги',
}

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Назва запису"
        self.fields['text'].label = "Текст запису"
        self.fields['category'].label = "Категорія"
        self.fields['tags'].label = "Теги"

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tags')

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Логін"
        self.fields['username'].help_text = 'Не більше 30 символів. Лише літери, цифри та @ / . / + / - / _ .'
        self.fields['email'].label = "E-mail"
        self.fields['password'].label = "Пароль"

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['website'].label = "Вебсайт"
        self.fields['website'].help_text = 'Не обов\'язкове поле'

    class Meta:
        model = UserProfile
        fields = ['website']