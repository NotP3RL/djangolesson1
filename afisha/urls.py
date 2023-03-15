from django.urls import path
from .views import show_index

appname='afisha'
urlpatterns = [
    path('', show_index, name='index')
]