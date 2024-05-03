from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusinessWizzardView.as_view(), name='business_wizard'),
    path('pages/<slug:slug>/', views.page_detail, name='page-detail'),
]
