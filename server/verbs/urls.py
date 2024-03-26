from django.urls import path
from . import views

urlpatterns = [
    path('conjugation', views.conj_verbs, name='conjugation'),
    path('past-forms', views.past_forms, name='past_forms'),
    path('rection', views.rection_verbs, name='rection')
]