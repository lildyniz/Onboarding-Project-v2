from django import forms 
from .models import User, Business, Direction

class UserDetailForm(forms.ModelForm):

    BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
    is_business_user = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False
    )


    class Meta:
        model = User
        fields = ('name', 'email')

class BusinessDetailForm(forms.ModelForm):


    class Meta:
        model = Business
        fields = ('business_type',)

class DirectionForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=Direction.objects.all(),
        empty_label=None,  # убирает пустой элемент из выпадающего списка
        widget=forms.Select(attrs={'class': 'form-control'})  # добавляем класс для стилизации
    )