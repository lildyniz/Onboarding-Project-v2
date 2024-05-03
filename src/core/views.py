from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView

from .forms import UserDetailForm, BusinessDetailForm, DirectionForm, PlatformForm, FirstPageForm, SecondPageForm
from .models import Direction, Business, Region, City, Page, Question


TEMPLATES = {
    '0': 'index.html',
    '1': 'index.html',
    '2': 'index.html',
    '3': 'index.html',
    '4': 'last_step.html',
    '5': 'last_step.html',
}

FORMS = [
    ('0', UserDetailForm),
    ('1', BusinessDetailForm),
    ('2', DirectionForm),
    ('3', PlatformForm),
    ('4', FirstPageForm),
    ('5', SecondPageForm),
]


# class BusinessWizzardView(SessionWizardView):
#     form_list = [UserDetailForm, BusinessDetailForm, DirectionForm, QuestionForm]
#     template_name = 'index.html'

#     def done(self, form_list, **kwargs):
#         return HttpResponse("Все отправлено!")


def previous_platform(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('is_business_user')


class BusinessWizzardView(SessionWizardView):
    form_list = FORMS
    template_name = 'index.html'
    condition_dict = {"3": previous_platform}

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
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


# Если страница одна
def page_detail(request, slug):
    pass
#     page = Page.objects.get(slug=slug)
#     questions = page.questions.all()
#     form = QuestionForm(questions=questions)
#     return render(request, 'page_detail.html', {'page': page, 'questions': questions, 'form': form})