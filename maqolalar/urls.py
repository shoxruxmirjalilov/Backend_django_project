from django.urls import path
from .views import ( 
                     MaqolaView, 
                     MaqolaDetail,
                     MaqolalarDetail,
                     MaqolaCreate, 
                     MaqolalarCreate, 
                     MaqolaUpdate, 
                     MaqolaDelete,
                     MaqolalarUpdate,
                     MaqolalarDelete
                    )

urlpatterns = [
    path('',MaqolaView.as_view(), name='maqola'),
    path('maqola/<int:pk>/', MaqolaDetail.as_view(), name='maqoladt'),
    path('<int:pk>/', MaqolalarDetail.as_view(), name='maqolaadt'),
    path('new/', MaqolaCreate.as_view(), name='maqola_new'),
    path('new-article/', MaqolalarCreate.as_view(), name='maqola-img_new'),
    path('update-maqola/<int:pk>', MaqolaUpdate.as_view(), name='maqola_up'),
    path('delete-maqola/<int:pk>', MaqolaDelete.as_view(), name='maqola_del'),
    path('update-maqolalar/<int:pk>', MaqolalarUpdate.as_view(), name='maqolaa_up'),
    path('delete-maqolalar/<int:pk>', MaqolalarDelete.as_view(), name='maqolaa_del'),
]