from django.urls import path
from . import views

urlpatterns= [
    path('' ,views.index , name='index' ),
    path('yes' , views.yes , name = 'yes'),
    path('no' , views.no , name = 'no')
]