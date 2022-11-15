from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'body',
            'tag',
        ]

        labels = {
            'body': '',
            'tag': 'Tag (Please Select A Tag):'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control mb-1'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "body",
        ]

        widgets = {
            'body': forms.Textarea(attrs={'rows':1,'class':'form-control','placeholder':'Leave A Comment!','id':'comment_reply'}),
        }

        labels = {
            "body": "",
        }
