from django.urls import path
from app import views
import django.contrib.flatpages.views as fp_views


urlpatterns = [
    path('', views.home.IndexView.as_view(), name='index'),
    path('catalog/', views.product.ProductListView.as_view(), name='catalog'),
    path('catalog/<str:category>/', views.product.ProductListView.as_view(), name='catalog'),
    path('catalog/<str:category>/<int:pk>', views.product.ProductDetailView.as_view(), name='product'),
    path('about/', fp_views.flatpage, {"url": "/about/"}, name="about"),
    path('payments/', fp_views.flatpage, {"url": "/payments/"}, name="payments"),
    path('delivery/', fp_views.flatpage, {"url": "/delivery/"}, name="delivery"),
    path('returns/', fp_views.flatpage, {"url": "/returns/"}, name="returns"),
]
