from carexpo import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'carexpo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('cars/<int:car_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)