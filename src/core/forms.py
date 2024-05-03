from django import forms 
from .models import User, Business, Direction, Region, City


class UserDetailForm(forms.ModelForm):

    BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
    is_business_user = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False
    )

    class Meta:
        model = User
        fields = ('name', 'email')


class BusinessDetailForm(forms.Form):

    business_type = forms.ModelChoiceField(
        queryset=Business.objects.all(),
        empty_label=None,  # убирает пустой элемент из выпадающего списка
        widget=forms.Select(attrs={'class': 'form-control'})  # добавляем класс для стилизации
    )

    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label=None,  # убирает пустой элемент из выпадающего списка
        widget=forms.Select(attrs={'class': 'form-control'})  # добавляем класс для стилизации
    )


class DirectionForm(forms.Form):

    direction = forms.ModelChoiceField(
        queryset=Direction.objects.all(),
        empty_label=None,  # убирает пустой элемент из выпадающего списка
        widget=forms.Select(attrs={'class': 'form-control'})  # добавляем класс для стилизации
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label=None,  # убирает пустой элемент из выпадающего списка
        widget=forms.Select(attrs={'class': 'form-control'})  # добавляем класс для стилизации
    )