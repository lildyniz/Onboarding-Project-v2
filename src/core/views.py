from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView

from .forms import UserDetailForm, BusinessDetailForm, DirectionForm
from .models import Direction, Business  # new



class BusinessWizzardView(SessionWizardView):
    form_list = [UserDetailForm, BusinessDetailForm, DirectionForm]
    template_name = 'index.html'

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)
        if step == '2':  # Это порядковый номер шага для DirectionForm
            cleaned_data = self.get_cleaned_data_for_step('1') or {}  # Получаем данные с предыдущего шага
            business_type = cleaned_data.get('business_type')  # Извлекаем тип бизнеса
            if business_type:
                # Получаем объект Business по его типу
                business = get_object_or_404(Business, business_type=business_type)
                # Фильтруем направления по выбранному типу бизнеса
                form.fields['name'].queryset = Direction.objects.filter(business=business)
        return form

    def done(self, form_list, **kwargs):
        return HttpResponse("Все отправлено!")