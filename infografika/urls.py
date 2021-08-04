from django.urls import path
from .views import InfografikaView, InfografikaCreate, InfografikaDetail, InfografikaUpdate, InfografikaDelete

urlpatterns = [
    path('',InfografikaView.as_view(), name='infografika'),
    path('new-infografika/', InfografikaCreate.as_view(), name='infografika_new'),
    path('<int:pk>/infografika', InfografikaDetail.as_view(), name='infografika_detail'),
    path('update-infografika/<int:pk>', InfografikaUpdate.as_view(), name='infografika_up'),
    path('delete-infografika/<int:pk>', InfografikaDelete.as_view(), name='infografika_del')
]