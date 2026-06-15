from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = [
    ("q9F_xCiTXfU", "rob-walling.txt"),
    ("ar9JCsiq6hs", "dan-martell.txt"),
    ("qsXxckCbci0", "alex-hormozi.txt"),
    ("GnX4PsQZfAs", "nathan-latka.txt"),
    ("ra0-ZvVApGk", "saastr.txt"),
    ("HQZMyxBvz_0", "tk-kader.txt"),
    ("NPpky92ZfjA", "starter-story.txt"),
    ("yyXCQHX55N4", "y-combinator.txt"),
    ("IFLY6L3YPGo", "greg-isenberg.txt"),
    ("JMSmodtv-iY", "sabrina-ramonov.txt"),
]

output_dir = os.path.join(os.path.dirname(__file__), "research", "youtube-transcripts")
os.makedirs(output_dir, exist_ok=True)

api = YouTubeTranscriptApi()

for video_id, filename in videos:
    output_path = os.path.join(output_dir, filename)
    try:
        transcript = api.fetch(video_id)
        text = "\n".join(entry.text for entry in transcript)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[OK] {filename} ({len(transcript)} segments)")
    except Exception as e:
        print(f"[FAIL] {filename}: {e}")
