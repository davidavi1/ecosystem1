from django.urls import path
from .views import ProductListView,CategoryView,ProductDetailView,BuyProduct

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('product/<int:pk>',ProductDetailView.as_view(),name='detail'),
    path('category/<int:pk>',CategoryView,name='category'),
    path('buy/<int:pk>',BuyProduct,name='buy')
]
