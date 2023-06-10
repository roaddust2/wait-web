from django.urls import path
from app import views
import django.contrib.flatpages.views as fp_views


urlpatterns = [
    path('', views.home.IndexView.as_view(), name='index'),
    path('catalog/', views.product.ProductListView.as_view(), name='catalog'),
    path('catalog/<slug:category_slug>/', views.product.ProductCategorizedListView.as_view(), name='category'),
    path('catalog/<slug:category_slug>/<slug:product_slug>', views.product.ProductDetailView.as_view(), name='product'),
    path('about/', views.about.About.as_view(), name="about"),
    path('delivery/', fp_views.flatpage, {"url": "/delivery/"}, name="delivery"),
    path('returns/', fp_views.flatpage, {"url": "/returns/"}, name="returns"),
    path('cooperation/', fp_views.flatpage, {"url": "/cooperation/"}, name="cooperation"),
]
