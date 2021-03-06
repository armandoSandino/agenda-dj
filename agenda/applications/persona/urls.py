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
        name='person-detail'
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
    ),
    # Para vista que no implementa un modelo en su serializador
    path(
        'api/personas/',
        views.PersonaAPILista.as_view(),
    ),
    #####
    # ListAPIView
    path(
        'api/reuniones/',
        views.ReunionListAPIView.as_view()
    ),
    path(
        'api/reuniones/link/',
        views.ReunionListAPIViewLink.as_view()
    ),
    path(
        'api/persona/pagination/',
        views.PersonPaginationListAPIView.as_view(),
    ),
    path(
        'api/reunion/job/',
        views.ReunionByPersonJobs.as_view()
    )
]