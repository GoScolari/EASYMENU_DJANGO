from django.urls import path
from .views import BlogListView, BlogCreateView,BlogDetailView, BlogUpdateView,BlogDeleteView	

app_name = 'menu'

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/Delete', BlogDeleteView.as_view(), name="delete"),
]