from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard , name="dashboard"),
]

# dashboard user kategori blog
# relasi user -> blog
# relasi kategori -> blog

# tambahan = upload gambar