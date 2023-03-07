from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . views import api_listeUsers
urlpatterns = [
    path('Listeuser', views.api_listeUsers),

]
