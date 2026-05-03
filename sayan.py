"""
YouTube Video Duration Fetcher
Supports: regular videos, premieres, live streams, shorts
Requirements: pip install yt-dlp
"""

import re
import sys

def format_duration(seconds):
    """Convert seconds to HH:MM:SS or MM:SS format."""
    if seconds is None:
        return "Unknown"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def get_video_duration(url: str) -> dict:
    """
    Fetch YouTube video duration using yt-dlp.
    Works for: regular videos, premieres, scheduled/upcoming livestreams, shorts.
    
    Returns a dict with keys: title, duration_seconds, duration_formatted, status
    """
    try:
        import yt_dlp
    except ImportError:
        raise ImportError("yt-dlp is not installed. Run: pip install yt-dlp")

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,         # Don't download, just fetch metadata
        "ignoreerrors": False,
        "extract_flat": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    duration = info.get("duration")          # None for scheduled premieres
    live_status = info.get("live_status")    # e.g. "is_upcoming", "is_live", "not_live"
    title = info.get("title", "N/A")

    # Determine human-readable status
    status_map = {
        "is_upcoming": "Scheduled Premiere / Upcoming",
        "is_live":     "Currently Live",
        "was_live":    "Was Live (VOD)",
        "not_live":    "Regular Video",
        None:          "Regular Video",
        "post_live":   "Post-Live / Replay",
    }
    status = status_map.get(live_status, live_status or "Unknown")

    return {
        "title":              title,
        "duration_seconds":   duration,
        "duration_formatted": format_duration(duration),
        "status":             status,
        "live_status_raw":    live_status,
    }


def main():
    # Accept URL from command line or prompt
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter YouTube video URL: ").strip()

    if not url:
        print("No URL provided.")
        sys.exit(1)

    print(f"\nFetching info for: {url}")
    print("-" * 50)

    try:
        result = get_video_duration(url)

        print(f"Title    : {result['title']}")
        print(f"Status   : {result['status']}")

        if result["duration_seconds"] is not None:
            print(f"Duration : {result['duration_formatted']}  ({result['duration_seconds']} seconds)")
        else:
            print("Duration : Not available yet (video may be a scheduled premiere or active livestream)")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()