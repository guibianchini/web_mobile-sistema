from django.contrib import admin
from django.urls import path
from sistema.views import Login

urlpatterns = [
    path('', Login.as_view(), name = 'index'),
    path('admin/', admin.site.urls),
]
