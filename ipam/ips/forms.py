from django import forms
from .models import IPAddressModel

# Создаём форму для изменения статуса и добавления комментария
class IPAddressUpdateForm(forms.ModelForm):
    class Meta:
        model = IPAddressModel
        fields = ['status', 'comment']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
