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
        'api/persona/lista/',
        views.PersonListAPIView.as_view(),
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista-persona'
    ),
    path(
        'api/persona/search/<str:termino>',
        views.PersonSearchApiView.as_view(),
    )
]