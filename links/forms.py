from django import forms
from .models import Link

# Create your views here

class LinkForm(forms.ModelForm):
  class Meta:
    model = Link
    fields = ['name', 'url', 'slug']