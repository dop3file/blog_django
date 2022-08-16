from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('all_articles/', views.get_all_articles),
    path('article/<int:id>/', views.get_article),
    path('search/', views.search_article),
    path('category/', views.get_all_categorys),
    path('category/<slug:name>', views.get_category),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
