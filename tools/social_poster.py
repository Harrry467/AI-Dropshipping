from langchain.tools import tool
import os

@tool
def upload_to_social(video_path: str, caption: str, platforms: list = ["youtube"]) -> dict:
    """
    Uploads the video to YouTube Shorts (and optionally IG/TikTok).
    Returns a dict of platform -> post URL.
    """
    results = {}
    # TODO: Implement YouTube Data API upload (see Google's sample)
    # For Instagram/TikTok, note that official posting APIs are limited or non-existent.
    # Use a service like Buffer API or a risky reverse-engineered library.
    if "youtube" in platforms:
        # youtube_upload(video_path, title=caption, category=22, privacy="public")
        results["youtube"] = "https://youtube.com/shorts/placeholder"
    # Instagram / TikTok stubs – normally blocked
    warnings.warn("Instagram & TikTok upload may violate ToS. Use at own risk.")
    return results
