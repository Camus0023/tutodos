from django.urls import path
from .views import homePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView, CartView, CartRemoveAllView, ImageViewFactory
from .utils import ImageLocalStorage

urlpatterns = [
    path("", homePageView, name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/created/', ProductCreatedView.as_view(), name='product_created'),
    path('cart/',            CartView.as_view(),          name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(),   name='cart_add'),
    path('cart/removeAll',   CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/',      ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
]

