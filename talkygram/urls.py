
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name = 'home'),
    
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls', namespace = 'profiles')),
    path('posts/', include('posts.urls', namespace = 'posts')),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
