from django.urls import path
from .views import strona1, strona2

urlpatterns = [
    path('strona1/', strona1, name='strona1'),
    path('strona2/', strona2, name='strona2'),
]