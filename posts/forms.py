from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Post
        fields = ('content', 'image')

