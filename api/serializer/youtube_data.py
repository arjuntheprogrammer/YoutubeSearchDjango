from api.models import YoutubeData
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class YoutubeDataSerializer(ModelSerializer):

    class Meta:
        model = YoutubeData
        fields = [
            "id",
            "title",
            "description",
            "published_at",
            "thumbnails",
            "video_id",
        ]
