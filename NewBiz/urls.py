from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('portfolios/<int:pk>/',PortfoliosSingle,name='portfolio-single'),
    path('form/',Form,name='form-contact'),
    path('footerform/',FooterForm,name='footer=form')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
