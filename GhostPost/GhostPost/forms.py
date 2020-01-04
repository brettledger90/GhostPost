from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    Boast = 'Boast'
    Roast = 'Roast'

    POST_CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast')
    ]

    post = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))
    type_of_post = forms.ChoiceField(choices=POST_CHOICES)
    class Meta:
        model = Post
        fields = ['post', 'type_of_post']
