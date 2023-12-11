from django import forms
from post.models import Product


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    about = forms.CharField(widget=forms.Textarea())
    photo = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=1, max_value=10)


class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=100)


class ReviewCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
