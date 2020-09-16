from django.urls.conf import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('add/', views.BlogCreateView.as_view(), name='add'),
    path('', views.BlogListView.as_view(), name='list'),
    path('edit/<int:pk>/', views.BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
]