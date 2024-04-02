
from django.contrib import admin
from django.urls import path
from movie import views as movieViews 
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('about/', movieViews.about, name='about'),
    path('signup/', movieViews.signup, name='signup'),
    path('news/', include('news.urls')),
    path('movie/', include('movie.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)