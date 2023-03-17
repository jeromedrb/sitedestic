from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . views import index, foolio, services, test
from .views import solutions, DetailSolution
urlpatterns = [
    path('', views.index, name='index'),
    path('dessolutions/', views.solutions, name='solution'),
    path('solution<int:Solutions_id>/', views.DetailSolution, name='detail_solution'),
    path('contact/', views.contact, name='contact'),
    path('folio/', views.foolio, name='folio'),
    path('services/', views.services, name='services'),
path('test/', views.test, name='test'),

]
