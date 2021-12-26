from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.inform_func, name='home'),

    path('accounts', include('django.contrib.auth.urls')),
    path('admin', admin.site.urls),

    path('unit', views.unit_func, name='unit'),
    path('unit/add_unit', views.add_unit_func, name='add_unit'),

    path('place', views.place_func, name='place'),
    path('place/add_unit', views.add_place_func, name='add_place'),
    # path('place/update_place/<pk>', views.PlaceUpdatelView.as_view(), name='update_place'),
    path('place/delete_place/<path>', views.delete_place_func, name='delete_place'),

    path('providers', views.providers_func, name='providers'),
    path('providers/add_new_provider', views.add_provider_func, name='add_provider'),
    path('providers/update_provider/<int:pk>', views.ProvidersUpdatelView.as_view(), name='update_provider'),
    path('providers/delete_provider/<id>', views.delete_provider_func, name='delete_provider'),

    path('clients', views.clients_func, name='clients'),
    path('clients/add_new_client', views.add_client_func, name='add_client'),
    path('clients/update_client/<int:pk>', views.ClientsUpdatelView.as_view(), name='update_client'),
    path('clients/delete_client/<id>', views.delete_client_func, name='delete_client'),

    path('products', views.products_func, name='products'),
    path('products/add_new_product', views.add_product_func, name='add_product'),
    path('products/update_product/<int:pk>', views.ProductsUpdatelView.as_view(), name='update_product'),
    path('products/delete_product/<id>', views.delete_product_func, name='delete_product'),

    path('documents', views.docShow_func, name='documents'),
    path('documents/form_act_sale', views.form_act, name='act_sale'),
    path('documents/open_act', views.open_act, name='open_act'),

    path('documents/form_opis', views.form_opis, name='opis'),
    path('documents/open_opis', views.open_opis, name='open_opis'),

    path('blanks', views.my_view, name='my-view'),
    path('blanks/<id>', views.my_view_status, name='my-view-status'),
    path('<path>', views.download_docx, name='download'),

]