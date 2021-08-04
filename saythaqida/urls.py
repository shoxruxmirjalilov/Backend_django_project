from django.urls import path
from .views import SaytHaqidaView, SaytHaqidaCreate, SaytHaqidaDetail, HaqidaUpdate, HaqidaDelete

urlpatterns = [
    path('',SaytHaqidaView.as_view(), name='haqida'),
    path('new-article/', SaytHaqidaCreate.as_view(), name='haqida_new'),
    path('<int:pk>/haqida', SaytHaqidaDetail.as_view(), name='sayt_haqida_detail'),
    path('update-sayt-haqida/<int:pk>', HaqidaUpdate.as_view(), name='haqida_up'),
    path('delete-sayt-haqida/<int:pk>', HaqidaDelete.as_view(), name='haqida_del')
]