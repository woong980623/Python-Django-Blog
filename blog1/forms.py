from django import forms
from .models import Post, Profile, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image', 'video']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
