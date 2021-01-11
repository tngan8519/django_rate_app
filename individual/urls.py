from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('browse', views.browse_view),
    path('new', views.create_individual_view),
    path('<int:individual_id>/', views.read_individual_view),
    path('<int:individual_id>/edit', views.update_individual_view),
    path('<int:individual_id>/delete', views.delete_individual_view), path('<int:individual_id>/rate/<int:rate_id>/edit', views.update_rate_view),path('<int:individual_id>/rate/<int:rate_id>/delete', views.delete_rate_view),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)