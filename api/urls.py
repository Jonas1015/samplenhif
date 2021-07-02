from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('facilities/', FacilitiesList.as_view()),
    # path('create-Facility/', FacilityCreate.as_view()),
    # path('update-Facility/<int:pk>/', FacilityRetrieveUpdateDestroy.as_view()),
    # path('Facility/<int:pk>/complete', FacilityComplete.as_view()),
    path('facility/<int:pk>/', FacilityDetailView, name = 'facility'),
    path('create-facility/', FacilityCreateView, name = 'create-facility'),
    path('update-facility/<int:pk>/', FacilityUpdateView, name = 'update-facility'),
    path('delete-facility/<int:pk>/', FacilityDeleteView, name = 'delete-facility'),

    # Authentication
    path('register/', registration_view, name = 'register'),
    path('login/', obtain_auth_token, name = "login"),
]
