from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('shoes/', views.ShoesList.as_view(), name="shoes_list"),
    path('shoes/<int:pk>', views.ShoesDetail.as_view(), name="shoes_detail"),
    path("brand/", views.BrandList.as_view(), name="brand_list"),
    path("brand/<int:pk>", views.BrandDetail.as_view(), name="brand_detail")
]