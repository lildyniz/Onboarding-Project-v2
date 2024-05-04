from django import forms 
from .models import User, Business, Direction, Region, City, Page, QuestionForSurvey


class UserDetailForm(forms.ModelForm):

    BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
    is_business_user = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        label="Вы уже пользуетесь другой платформой для бизнеса?",
        required=True
    )


    class Meta:
        model = User
        fields = ('name', 'email')
        labels = {
            'name': 'Введите ваше имя',
            'email': 'Ведите ваш email'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}),
        }


class BusinessDetailForm(forms.Form):

    business_type = forms.ModelChoiceField(
        queryset=Business.objects.all(),
        label="Укажите тип вашего бизнеса",
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )

    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        label="Укажите регион работы бизнеса",
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})  
    )


class DirectionForm(forms.Form):

    direction = forms.ModelChoiceField(
        queryset=Direction.objects.all(),
        label="Укажите направление вашего бизнеса",
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'})  
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="Укажите город работы бизнеса",
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'})  
    )


class FirstPageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        first_page = Page.objects.get(title='First_page')
        questions = first_page.questions.all()
        super(FirstPageForm, self).__init__(*args, **kwargs)
        
        if questions:
            for question in questions:
                self.fields['question_%d' % question.id] = forms.ChoiceField(
                    label=question.text,
                    choices=[(answer.id, answer.text) for answer in question.answers.all()],
                    widget=forms.Select(attrs={'class': 'form-control'}),
                    required=True
                )


class SecondPageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        second_page = Page.objects.get(title='Second_page')
        questions = second_page.questions.all()
        super(SecondPageForm, self).__init__(*args, **kwargs)
        
        if questions:
            for question in questions:
                self.fields['question_%d' % question.id] = forms.ChoiceField(
                    label=question.text,
                    choices=[(answer.id, answer.text) for answer in question.answers.all()],
                    widget=forms.Select(attrs={'class': 'form-control'}),
                    required=True
                )


class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = QuestionForSurvey.objects.all()
        super(SurveyForm, self).__init__(*args, **kwargs)
        
        if questions:
            for question in questions:
                self.fields['survey-question_%d' % question.id] = forms.ChoiceField(
                    label=question.text,
                    choices=[(True, 'Да'), (False, 'Нет')],
                    widget=forms.CheckboxInput,
                    required=False
                )