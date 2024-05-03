from django import forms 
from .models import User, Business, Direction, Region, City, Question, Page


class UserDetailForm(forms.ModelForm):

    BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
    is_business_user = forms.BooleanField(
        widget=forms.Select(choices=BOOL_CHOICES, attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}),
        label="Вы уже пользуетесь другой платформой для бизнеса?",
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
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )

    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label=None, 
        widget=forms.Select(attrs={'class': 'form-control'})  
    )


class DirectionForm(forms.Form):

    direction = forms.ModelChoiceField(
        queryset=Direction.objects.all(),
        empty_label=None, 
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'})  
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label=None, 
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'})  
    )


class PlatformForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('previous_platform',)
        labels = {
            'previous_platform': 'Укажите какой платформой для бизнеса вы пользовались',
        }
        widgets = {
            'previous_platform': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}),
        }


# Форма, если страница отдельная
# class QuestionForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     # questions = kwargs.pop('questions', None)
    #     questions = Question.objects.all()
    #     super(QuestionForm, self).__init__(*args, **kwargs)
        
    #     if questions:
    #         for question in questions:
    #             self.fields['question_%d' % question.id] = forms.ChoiceField(
    #                 label=question.text,
    #                 choices=[(answer.id, answer.text) for answer in question.answers.all()],
    #                 widget=forms.Select(attrs={'class': 'form-control'}),
    #                 required=True
    #             )


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