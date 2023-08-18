import json
import requests


def insta_downloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "93e8dd3ccfmsh15be576e4fd52d3p13968ajsn4660ae894f77",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'


# print(insta_downloader("https://www.instagram.com/reel/Cv7yMFyuLA9/?utm_source=ig_web_copy_link"))


def yout_tube_downloader(videoId):
    b = videoId.index('=')
    id = videoId[b + 1:]
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    querystring = {"videoId": id}

    headers = {
        "X-RapidAPI-Key": "93e8dd3ccfmsh15be576e4fd52d3p13968ajsn4660ae894f77",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    data = {}
    data['url'] = rest['videos']['items'][0]['url']
    return data

# print(yout_tube_downloader("https://www.youtube.com/watch?v=IMRYSkd1xzA"))
