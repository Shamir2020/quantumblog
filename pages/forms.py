from .models import *
from django.forms import ModelForm

class CreateBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'