from django.urls import path
from .views import Index, IndexCreate, IndexUpdate, IndexDelete, IndexDetail

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('new-index/', IndexCreate.as_view(), name='index_new'),
    path('<int:pk>/index', IndexDetail.as_view(), name='index_detail'),
    path('update-index/<int:pk>', IndexUpdate.as_view(), name='index_up'),
    path('delete-index/<int:pk>', IndexDelete.as_view(), name='index_del'),

]