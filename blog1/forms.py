from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

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
