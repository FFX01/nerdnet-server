from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^images/$', views.ImageList.as_view(), name='image-list'),
    url(r'images/create/$', views.ImageCreate.as_view(), name='image-create'),
    url(r'^images/(?P<pk>\d+)/$', views.ImageDetail.as_view(), name='image-detail')
]
