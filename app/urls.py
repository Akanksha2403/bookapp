from django.urls import path
from . import views

urlpatterns = [
    path("buy/", views.buy, name="buy"),
    path('books/<int:myid>', views.bookview, name="bookView"),
    path("search/", views.search, name ="Search"),
    path("checkout/", views.checkout, name ="checkout"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name='about'),
]
