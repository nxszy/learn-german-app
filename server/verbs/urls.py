from django.urls import path
from . import views

urlpatterns = [
    path('conjugation', views.conj_verbs, name='default_learning_set'),
    path('past-forms', views.past_forms, name='past_forms')
]