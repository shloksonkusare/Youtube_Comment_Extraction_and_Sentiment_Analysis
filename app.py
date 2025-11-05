from flask import Flask, request, render_template, send_file
from googleapiclient.discovery import build
from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logging
import csv
import os
import re
import sys

app = Flask(__name__)

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")

try:
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    logging.info("YouTube API client initialized successfully.")
except Exception as e:
    logging.error("Failed to initialize YouTube API client.")
    raise CustomException(e, sys)


def extract_video_id(url):
    try:
        logging.info(f"Extracting Video ID from URL: {url}")

        pattern = r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})"
        match = re.search(pattern, url)

        if not match:
            raise ValueError("Invalid YouTube Video URL")

        video_id = match.group(1)
        logging.info(f"Successfully extracted Video ID: {video_id}")
        return video_id

    except Exception as e:
        logging.error("Error occurred while extracting Video ID.")
        raise CustomException(e, sys)


@app.route('/')
def home():
    logging.info("Home page loaded successfully.")
    return render_template('index.html')


@app.route('/extract_comments', methods=['POST'])
def extract_comments():
    try:
        video_url = request.form['youtube_link']
        logging.info(f"Received YouTube link from user: {video_url}")

        video_id = extract_video_id(video_url)
        logging.info(f"Processing comments for video ID: {video_id}")

        comments_list = []
        next_page_token = None

        while True:
            comments = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100,
                textFormat='plainText',
                pageToken=next_page_token
            ).execute()

            for comment in comments['items']:
                text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                comments_list.append([text])

            next_page_token = comments.get('nextPageToken')
            if not next_page_token:
                break

        csv_path = f"comments_{video_id}.csv"

        with open(csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Comment'])
            writer.writerows(comments_list)

        logging.info(f"Successfully saved comments to {csv_path}")
        return send_file(csv_path, as_attachment=True)

    except Exception as e:
        logging.error("Error occurred during comment extraction.")
        raise CustomException(e, sys)


if __name__ == '__main__':
    logging.info("Starting Flask server...")
    app.run(debug=True)
