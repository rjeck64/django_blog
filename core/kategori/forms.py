from django import forms
from .models import Category


class CreateKategori(forms.ModelForm):
    # Category_name = forms.CharField(label=False, max_length=255, widget=forms.TextInput(attrs={'class' : "form-control form-control-user" , 'placeholder' : 'Masukan Nama Kategori'}))

    class Meta:
        model = Category
        fields = ['Category_name']
        widgets = {
            'Category_name' : forms.TextInput(attrs={'class' : "form-control form-control-user" , 'placeholder' : 'Masukan Nama Kategori'})
        }
        label = False
        max_length = 255