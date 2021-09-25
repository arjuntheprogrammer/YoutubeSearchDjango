from django.urls import path

from api.views import GetVideosAPIView, SearchVideoAPIView

urlpatterns = [

    path(r'get_videos/', GetVideosAPIView.as_view(),
         name='get_videos_data'),
    path(r'search_video/', SearchVideoAPIView.as_view(),
         name='search_video'),
]
