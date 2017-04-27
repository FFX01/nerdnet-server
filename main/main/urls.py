"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

from rest_framework.routers import DefaultRouter

from users.api.resources import UserViewSet
from articles.api.resources import ArticleViewSet
from media.api.resources import ImageViewSet
from feeds.api.resources import ActionViewSet


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)
router.register('images', ImageViewSet)
router.register('actions', ActionViewSet)


urlpatterns = [
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls)
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
