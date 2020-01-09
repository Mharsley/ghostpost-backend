from django import forms
# from ghostpost.models import Author, Post
from ghostpost.models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'boast']

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=30)