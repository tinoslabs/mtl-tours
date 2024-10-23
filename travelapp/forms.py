from django import forms
from django.forms.models import inlineformset_factory
from .models import Package,Category,Contactus


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'