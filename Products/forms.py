from django import forms

from Products.models import Product, Review


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=200, min_length=2)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=400)
    rate = forms.FloatField()
