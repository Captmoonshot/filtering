from django.urls import path

from .views import (
    BootstrapFilterView,
)

urlpatterns = [
    path('', BootstrapFilterView, name='bootstrap'),
]