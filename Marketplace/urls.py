from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlantListView.as_view(), name="home"),
    path('marktplatz/inserat/erstellen', views.ProductCreateView.as_view(), name="upload"),
    path('marktplatz/inserat/bearbeiten/<slug>', views.ProductUpdateView.as_view(), name='edit'),
    path('marktplatz/inserat/<slug>', views.detail, name='detail'),
    path('impressum', views.impressum, name='impressum'),
    path('faq', views.faq, name='faq'),
    ]