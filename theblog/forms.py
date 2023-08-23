from django import forms
from .models import Post, Category

# Hardcoded
# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]

# Dynamical
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for items in choices:
    choice_list.append(items)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Enter title of the page..'
            }),
            'title_tag': forms.TextInput(attrs=
            {
                'class': 'form-control'
            }),
            'author': forms.Select(attrs=
            {
                'class': 'form-control'
            }),
            # Hardcoded
            # 'category': forms.Select(choices=choices, attrs=
            # Dynamic
            'category': forms.Select(choices=choice_list, attrs=
            {
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs=
            {
                'class': 'form-control'
            }),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Enter title of the page..'
            }),
            'title_tag': forms.TextInput(attrs=
            {
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs=
            {
                'class': 'form-control'
            }),
        }
