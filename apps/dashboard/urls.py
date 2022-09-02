from django.urls import URLPattern, path, include
from .views import *

urlpatterns = [
    path('', getDashboard , name="principalDashboard"),
    path('modulos/', include("apps.dashboard.controllers.modulos.urls")),
    path('usuarios/', include("apps.dashboard.controllers.usuarios.urls")),
    path('roles/', include("apps.dashboard.controllers.roles.urls")), 
]

