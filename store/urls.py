from django.urls import path
from . import views

app_name='store'


urlpatterns = [
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),

]