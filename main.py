import streamlit as st
import datetime
import os
from pathlib import Path

from summary import ChatModel
from openai_tts import TextToSpeech
from get_youtube_transcript import get_transcripts

def _get_documents() -> list[str]:
    docs = []
    
    # Add additional news sources by appending them to the list.
    docs.append(get_transcripts())
    return docs

def get_mp3():
    docs = _get_documents()
    chat_model = ChatModel(docs)
    news = chat_model.get_response()
    
    speech_model = TextToSpeech()
    speech_model.tts(news)


if __name__ == "__main__":
    # Set the page title
    st.set_page_config(page_title="Daily AI News")

    # Add a title to the app
    st.title("Daily AI News")

    # Generate the MP3 file
    filename = os.path.join("./audios/", datetime.date.today().strftime('%Y-%m-%d') + ".mp3")
    todays_news = Path(filename)
    if not todays_news.is_file():
        get_mp3()
    
    # Display audio player
    st.audio(filename, format='audio/mp3')