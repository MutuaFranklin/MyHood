from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views  import UpdateProfileView, NewProfileUpdateView




urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index,name='index'),
    path('home', views.home,name='home'),
    path('search/', views.search, name='search_business'),
    path('<username>/', views.userProfile, name='userProfile'),
    path('update-new-profile/<int:pk>', NewProfileUpdateView.as_view(), name='new-profile'),
    path('update/<int:pk>', UpdateProfileView.as_view(), name='update-profile'),
    path('health-facility', views.registerHealthFacility,name='health_facility'),




]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


