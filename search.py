"""from flask import Flask, request, Response
from flask_ngrok import run_with_ngrok
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


app = Flask(__name__)

def build_youtube_search(developer_key):
  DEVELOPER_KEY = developer_key
  YOUTUBE_API_SERVICE_NAME="youtube"
  YOUTUBE_API_VERSION="v3"
  return build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def get_search_response(youtube, query):
  search_response = youtube.search().list(
    q = query,
    order = "relevance",
    part = "snippet",
    maxResults = 10
    ).execute()
  return search_response

def get_video_info(search_response):
  result_json = {}
  idx =0
  for item in search_response['items']:
    if item['id']['kind'] == 'youtube#video':
      result_json[idx] = info_to_dict(item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['thumbnails']['medium']['url'])
      idx += 1
  return result_json

def info_to_dict(videoId, title, description, url):
  result = {
      "videoId": videoId,
      "title": title,
      "description": description,
      "url": url
  }
  return result

@app.route('/')
def just_started():
  return "just started"

@app.route('/video_list', methods=['GET', 'POST'])
def get_video_list():
  developer_key =  request.args['key']
  query = request.args['query']
  youtube = build_youtube_search(developer_key)
  search_response = get_search_response(youtube, query)
  res = json.dumps(get_video_info(search_response), ensure_ascii=False)
  return Response(res, content_type='application/json; charset=utf-8')

run_with_ngrok(app)
app.run()"""