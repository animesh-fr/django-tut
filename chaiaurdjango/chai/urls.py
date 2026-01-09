
from django.urls import path
from . import views

# localhost:8000/chai
# localhost:8000/chai/black_tea

urlpatterns = [
    path('', views.all_chai, name='all_chai')
    # path('', views.all_chai, name='orders')
]
