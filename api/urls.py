from django.conf.urls import url

from api.views import infraciones
from api.views import geocode


urlpatterns = [
    url(r'^infracciones', infraciones.as_view(), name='api_infraciones'),
    url(r'^geography', geocode.as_view(), name='api_geocode'),
]
