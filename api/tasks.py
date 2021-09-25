from django.utils import timezone
from youtube_search import celery_app

from youtube_search.constants import YOUTUBE_SEARCH_QUERY
from api.models import YoutubeData
from youtube_search.youtube_client import YoutubeApiClient


@celery_app.task()
def fetch_latest_videos():
    existing_video_ids = YoutubeData.objects.filter().values_list("video_id", flat=True)

    latest_video = YoutubeData.objects.order_by('-published_at').first()
    if not latest_video:
        start_date = timezone.now() - timezone.timedelta(days=10)
    else:
        start_date = latest_video.published_at
    end_date = timezone.now()

    bulk_youtube_videos_objs = []

    video_data = YoutubeApiClient().fetch_videos(
        YOUTUBE_SEARCH_QUERY, start_date=start_date, end_date=end_date)
    print(f"existing_video_ids = {existing_video_ids}")
    for video in video_data:

        # check for duplicates, move this to model clean method
        if video['video_id'] not in existing_video_ids:
            bulk_youtube_videos_objs.append(
                YoutubeData(**video)
            )
        else:
            print(f"video['video_id'] = {video['video_id']}")

    YoutubeData.objects.bulk_create(
        bulk_youtube_videos_objs, ignore_conflicts=True)
