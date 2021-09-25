from api.models import YoutubeData
from api.serializer.youtube_data import YoutubeDataSerializer
from common.core import BaseAPIView

from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from django.contrib.postgres.search import SearchRank, SearchVector, SearchQuery


class GetVideosAPIView(BaseAPIView):
    queryset = YoutubeData.objects.all()
    serializer_class = YoutubeDataSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']


class SearchVideoAPIView(BaseAPIView):
    serializer_class = YoutubeDataSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if(query):
            vector = SearchVector('title', weight='A') + \
                SearchVector('description', weight='B')

            return YoutubeData.objects.annotate(
                rank=SearchRank(
                    vector,
                    SearchQuery(query),
                    cover_density=True)
            ).order_by('-rank').filter(rank__gt=0)
        else:
            YoutubeData.objects.all()
