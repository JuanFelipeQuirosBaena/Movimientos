from django.urls import path
from . import views

app_name = 'movimientos'

urlpatterns = [
    path('', views.MovimientoListView.as_view(), name='list'),
    path('crear/', views.MovimientoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MovimientoDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.MovimientoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.MovimientoDeleteView.as_view(), name='delete'),
]
