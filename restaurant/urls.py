from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'densetsu-home'),
    path('about/', views.about, name = 'densetsu-about'),
    path('menu/', views.menu, name = 'densetsu-menu'),
    path('reservations/', views.reservationsPage, name = 'densetsu-reservations'),
    path('gallery/', views.gallery, name = 'densetsu-gallery'),
    path('contact/', views.contact, name = 'densetsu-contact'),
    path('copyright/', views.copyright, name = 'densetsu-copyright'),
]
