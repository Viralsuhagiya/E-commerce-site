from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about, name='AboutUs'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("contact/", views.contact, name="contact"),
    path("checkout/", views.checkout, name="checkout"),
    path("tracker/", views.tracker, name="tracker"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]