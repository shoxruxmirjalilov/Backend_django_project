from django.urls import path

from .views import VideoView, VideoCreate, VideoDetail, VideoUpdate, VideoDelete

urlpatterns = [
    path('',VideoView.as_view(), name='video'),
    path('new-article/', VideoCreate.as_view(), name='video_new'),
    path('<int:pk>/', VideoDetail.as_view(), name='vid_detail'),
    path('update-video/<int:pk>', VideoUpdate.as_view(), name='video_up'),
    path('delete-video/<int:pk>', VideoDelete.as_view(), name='video_del'),
]