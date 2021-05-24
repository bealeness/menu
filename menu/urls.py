from django.urls import path
from django.views.generic import TemplateView

app_name = 'menu'

urlpatterns = [
    path('', TemplateView.as_view(template_name='menu/index.html')),
]