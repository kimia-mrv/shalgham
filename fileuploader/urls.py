from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from .models import photo
admin.site.register(photo)

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='main'),
    path('details/', views.details, name='details'),
    path('result/', views.result, name='result'),
    path('shared/',views.shared, name='shared')
]
if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
