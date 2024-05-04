from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView

from .forms import UserDetailForm, BusinessDetailForm, DirectionForm, FirstPageForm, SecondPageForm, SurveyForm
from .models import Direction, Business, Region, City, User, Question, Answer, QuestionForSurvey

TEMPLATES = {
    '0': 'index.html',
    '1': 'index.html',
    '2': 'index.html',
    '3': 'last_step.html',
    '4': 'last_step.html',
    '5': 'last_step.html',
}

FORMS = [
    ('0', UserDetailForm),
    ('1', BusinessDetailForm),
    ('2', DirectionForm),
    ('3', FirstPageForm),
    ('4', SecondPageForm),
    ('5', SurveyForm),
]


class BusinessWizzardView(SessionWizardView):
    form_list = FORMS
    template_name = 'index.html'

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]] 

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)
        if step == '2':
            cleaned_data = self.get_cleaned_data_for_step('1') or {}
            business_type = cleaned_data.get('business_type')
            region = cleaned_data.get('region')
            if business_type:
                business = get_object_or_404(Business, business_type=business_type)
                form.fields['direction'].queryset = Direction.objects.filter(business=business)
            if region:
                regions = get_object_or_404(Region, region=region)
                form.fields['city'].queryset = City.objects.filter(region=regions)
        return form

    def done(self, form_list, **kwargs):
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        
        questions_with_answers = []
        for key, value in data.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                question = Question.objects.get(pk=question_id)
                answer_id = int(value)
                answer = Answer.objects.get(pk=answer_id).text
                questions_with_answers.append(f"{question.text} {answer}")
            if key.startswith('survey-question_'):
                question_id = int(key.split('_')[1])
                question = QuestionForSurvey.objects.get(pk=question_id)
                answer = "Да" if value == 'True' else 'Нет'
                questions_with_answers.append(f"{question.text} {answer}")


        user= User.objects.create(email=data['email'],
                                  name = data['name'],
                                  previous_platform = "Есть" if data['is_business_user'] == 'True' else "Нет",
                                  business = Business.objects.get(business_type=data['business_type']),
                                  business_direction = Direction.objects.get(direction=data['direction']),
                                  region = Region.objects.get(region=data['region']),
                                  city = City.objects.get(city=data['city']),
                                  answers_to_questions = "\n".join(questions_with_answers)
                                )
        user.save()


        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })