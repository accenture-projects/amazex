from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/<int:pk>', views.products_view, name="view-product"),
    path('select-config/', views.select_configuration, name='select-configuration'),

    # selected config
    path('view/light-weight', views.light_weight, name='light-weight'),
    path('view/medium', views.medium, name='medium'),

    # laptop detail
    path('view/medium/asus', views.asus, name='asus'),
    path('view/medium/alienware', views.alienware, name='alienware'),

    path('view/medium/asus/invoice', views.as_invoice, name='as-invoice'),
    path('view/medium/alienware/invoice', views.al_invoice, name='al-invoice'),

    path('view/medium/alienware/invoice/success', views.order_placed, name='order-placed'),
]
