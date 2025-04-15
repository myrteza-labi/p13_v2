from django.contrib import admin
from django.urls import path, include
from lettings.views import test_error
from lettings.views import test_sentry
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path('test500/', test_error, name='test_error'),
    path('sentry-test/', test_sentry, name='sentry-test'),
]
