from django import forms
from .models import Blog
from kategori.models import Category

class Content(forms.ModelForm):
    Category_name = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        empty_label=None,
        to_field_name='Category_name',
        widget=forms.Select(attrs={'class': 'form-control form-control-user m-2'})
    )

    class Meta: 
      model = Blog
      fields = ['title' , 'deskripsi', 'Category_name', 'author']
      widgets = {
         'title' : forms.TextInput(attrs={'class' : 'form-control form-control-user m-2' , 'placeholder' : 'Title...'}),
         'deskripsi' : forms.Textarea(attrs={'class' : "form-control form-control-user m-2"}),
        #  'Category_name' : forms.Select(attrs={'class' : 'form-control form-control-user m-2'}),
         'author' : forms.TextInput(attrs={'class' : 'form-control form-control-user m-2' , 'placeholder' : 'Author...'})
      }  

    def __init__(self, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True
      