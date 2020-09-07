from django.urls import path, re_path, include

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersona.as_view(),
        name='personas'
    ),
    # ListAPIView
    path(
        'api/persona/lista/',
        views.PersonListAPIView.as_view(),
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista-persona'
    ),
    # ListAPIView
    path(
        'api/persona/search/<str:termino>',
        views.PersonSearchApiView.as_view(),
    ),
    # CreateAPIView
    path(
        'api/person/create/',
        views.PersonCreateAPIView.as_view()
    ),
    # RetrieveAPIView or DetailView
    path(
        'api/persona/<pk>/',
        views.PersonRetrieveAPIView.as_view(),
    ),
    # DestroyAPIView
    path(
        'api/persona/delete/<pk>/',
        views.DestroyAPIView.as_view()
    ),
    # UpdateAPIView es equivalente al UpdateView en Django
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateView.as_view(),
    ),
    # PersonRetrieveUpdateView
    path(
        'api/persona/modificar/<pk>/',
        views.PersonRetrieveUpdateView.as_view(),
    )
]