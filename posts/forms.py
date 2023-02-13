from django import forms

from posts.models import Post


class PostCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите название заметки',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите описание заметки',
    }))
    actuality = forms.CharField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))

    class Meta:
        model = Post
        fields = ('name', 'description', 'actuality')
