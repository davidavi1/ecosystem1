from django import forms
from .models import Zakaz,Product


class ZakazForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all().order_by('title'),label='Продукт')
    class Meta:
        model = Zakaz
        fields = ('product','name', 'phone', 'email', 'comment')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
