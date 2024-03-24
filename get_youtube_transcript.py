import os
import re
import datetime
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import googleapiclient.discovery

load_dotenv()

def get_list_of_videos_from_youtube() -> list[str]:
    # Define the API key and service object
    api_key = os.getenv("YOUTUBE_DATA_API_KEY")
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Define the search term and time period
    search_term = "AI news"
    # Get the date of two days ago
    published_after = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d") + "T00:00:00Z"

    # Perform the search
    search_response = youtube.search().list(
        q=search_term,
        type="video",
        publishedAfter=published_after,
        order="relevance",
        part="id",
        videoCaption="closedCaption",
        maxResults=5
    ).execute()

    # Extract video IDs from the search results
    video_ids = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_ids.append(search_result["id"]["videoId"])
    
    return video_ids
        

def get_caption_from_youtube(id) -> str:
    try:
        srt = YouTubeTranscriptApi.get_transcript(id)
    except:
        return ""

    text = " ".join([dict['text'] for dict in srt])
    paren_removed = re.sub(r'\(.*?\)', '', text)
    pure_transcript = re.sub(r'\n', ' ', paren_removed)

    return pure_transcript


def get_transcripts() -> str:
    vids = get_list_of_videos_from_youtube()
    return "\n\n".join([get_caption_from_youtube(vid) for vid in vids])