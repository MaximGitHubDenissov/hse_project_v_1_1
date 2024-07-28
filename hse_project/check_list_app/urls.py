from django.urls import path
from .views import index, select, regular
from django.views.generic import RedirectView

urlpatterns = [
    path('', index, name='index'),
    path('select/', select, name='select'),
    path('select/regular/', regular, name='regular')

    
]

urlpatterns += [
    path('', RedirectView.as_view(url='/ru/')),  # Перенаправление на русский по умолчанию
]

