# YOUTUBE SEARCH

- Application to fetch Youtube Videos Data related to specific search query(Cricket in our case).
- Storing the data in PostgreSQL DB
- API for searching and retrieving Youtube Data.

## BASIC REQUIREMENTS

- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimized.

## ADDITIONAL REQUIREMENTS

- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Make a dashboard to view the stored videos with filters and sorting options (optional)
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
  - Ex 1: A video with title _`How to make tea?`_ should match for the search query `tea how`

## TECH STACK

- Django(Python 3.9)
- PostgreSQL DB
- Celery
- Redis

## INSTALLATION COMMAND

`$ docker-compose up -d`

## API ENDPOINT

- To GET Paginated Videos Data: `http://localhost:8000/api/get_videos/`
  ![image](https://user-images.githubusercontent.com/15984084/134779831-29274948-de44-4b29-bae2-f9abbfe5884c.png)

- To GET Paginated Search Query Data Videos: `http://localhost:8000/api/search_video/?query=Kohli`
  ![image](https://user-images.githubusercontent.com/15984084/134779837-78466663-f619-452f-9e7c-a3a3af2897e4.png)

## POSTMAN COLLECTION

[YoutubeSearch.postman_collection.json.zip](https://github.com/arjuntheprogrammer/YoutubeSearchDjango/files/7230077/YoutubeSearch.postman_collection.json.zip)

## REFERENCE

- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
  - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
  - Without publishedAfter, it will give you cached results which will be too old
