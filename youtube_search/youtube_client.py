from django.conf import settings
from django.utils import timezone

import googleapiclient.discovery
from youtube_search.constants import YOUTUBE_API_KEY, YOUTUBE_DATE_FORMAT


class YoutubeApiClient:
    api_service_name = 'youtube'
    api_version = 'v3'

    def __init__(self):
        self.youtube_service = googleapiclient.discovery.build(
            self.api_service_name,
            self.api_version,
            developerKey=YOUTUBE_API_KEY)

    @staticmethod
    def serialize_data(data):
        modified_data = []
        for video in data:
            snippet = video['snippet']
            modified_data.append({
                'title': snippet['title'],
                'published_at': snippet['publishedAt'],
                'description': snippet['description'],
                'thumbnails': snippet['thumbnails'],
                'video_id': video['id']['videoId']
            })
        return modified_data

    def fetch_videos(self, query, start_date='', end_date=timezone.now()):
        video_data = []
        if not start_date:
            raise Exception('start date missing')

        if (end_date - start_date).days > 30:
            raise Exception('interval too big')

        kwargs = {
            'part': 'snippet',
            'maxResults': 50,
            'q': query,
            'order': 'date',
            'publishedAfter': start_date.strftime(YOUTUBE_DATE_FORMAT),
            'publishedBefore': end_date.strftime(YOUTUBE_DATE_FORMAT),
            'type': 'video'
        }

        while True:
            request = self.youtube_service.search().list(**kwargs)
            response = request.execute()
            video_data.extend(response['items'])
            if len(response['items']) < 50:
                break
            kwargs['pageToken'] = response['nextPageToken']
        return self.serialize_data(video_data)
