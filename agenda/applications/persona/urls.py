from django.urls import path, re_path, include

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersona.as_view(),
        name='personas'
    ),
    path(
        'api/persona/list/',
        views.PersonListAPIView.as_view(),
    )
]