from django import forms
from .models import BlogPostModel

# model bound form
class NewPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ['title', 'text']
