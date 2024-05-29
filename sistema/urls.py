from django.contrib import admin
from django.urls import path, include
from sistema.views import Index, Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'index'),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
    path('anuncio/', include('anuncio.urls'), name='anuncio')
]
