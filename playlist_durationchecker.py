"""
YouTube Video & Playlist Duration Fetcher
Supports: regular videos, premieres, live streams, shorts, playlists
Requirements: pip install yt-dlp
Developed by: SAYAN PAL
"""

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


def is_playlist_url(url: str) -> bool:
    """Check if the URL points to a playlist."""
    return "list=" in url and "watch?v=" not in url


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
        "skip_download": True,
        "ignoreerrors": False,
        "extract_flat": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    duration = info.get("duration")
    live_status = info.get("live_status")
    title = info.get("title", "N/A")

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


def get_playlist_duration(url: str) -> dict:
    """
    Fetch all video durations in a YouTube playlist.

    Returns a dict with:
      - title           : playlist title
      - total_seconds   : sum of all available durations
      - total_formatted : HH:MM:SS total
      - video_count     : total videos in playlist
      - skipped_count   : videos with no duration (live/premiere/unavailable)
      - videos          : list of per-video dicts
    """
    try:
        import yt_dlp
    except ImportError:
        raise ImportError("yt-dlp is not installed. Run: pip install yt-dlp")

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "ignoreerrors": True,       # Skip unavailable/private videos
        "extract_flat": False,      # Full metadata for each entry
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if info.get("_type") != "playlist":
        raise ValueError("URL does not appear to be a playlist.")

    playlist_title = info.get("title", "Unknown Playlist")
    entries = info.get("entries", [])

    videos = []
    total_seconds = 0
    skipped = 0

    for i, entry in enumerate(entries, start=1):
        if entry is None:
            skipped += 1
            continue

        duration = entry.get("duration")
        title = entry.get("title", "N/A")
        video_id = entry.get("id", "")
        live_status = entry.get("live_status")

        status_map = {
            "is_upcoming": "Scheduled",
            "is_live":     "Live",
            "was_live":    "VOD",
            "not_live":    "Video",
            None:          "Video",
            "post_live":   "Replay",
        }
        status = status_map.get(live_status, "Video")

        if duration:
            total_seconds += duration
        else:
            skipped += 1

        videos.append({
            "index":              i,
            "title":              title,
            "video_id":           video_id,
            "duration_seconds":   duration,
            "duration_formatted": format_duration(duration),
            "status":             status,
        })

    return {
        "title":           playlist_title,
        "total_seconds":   total_seconds,
        "total_formatted": format_duration(total_seconds),
        "video_count":     len(videos),
        "skipped_count":   skipped,
        "videos":          videos,
    }


def print_video_result(url: str):
    result = get_video_duration(url)
    print(f"Title    : {result['title']}")
    print(f"Status   : {result['status']}")
    if result["duration_seconds"] is not None:
        print(f"Duration : {result['duration_formatted']}  ({result['duration_seconds']} seconds)")
    else:
        print("Duration : Not available yet (scheduled premiere or active livestream)")


def print_playlist_result(url: str):
    print("Fetching playlist... this may take a moment.\n")
    result = get_playlist_duration(url)

    print(f"Playlist : {result['title']}")
    print(f"Videos   : {result['video_count']}  |  Skipped: {result['skipped_count']}")
    print(f"Total    : {result['total_formatted']}  ({result['total_seconds']} seconds)")
    print("-" * 50)

    for v in result["videos"]:
        idx   = f"[{v['index']:>3}]"
        dur   = v["duration_formatted"] if v["duration_seconds"] else "N/A    "
        label = f"({v['status']})" if v["status"] != "Video" else ""
        title = v["title"][:60] + "…" if len(v["title"]) > 60 else v["title"]
        print(f"  {idx}  {dur:<9}  {title}  {label}")

    print("-" * 50)
    print(f"  Total Duration : {result['total_formatted']}")


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter YouTube video or playlist URL: ").strip()

    if not url:
        print("No URL provided.")
        sys.exit(1)

    print(f"\nFetching info for: {url}")
    print("-" * 50)

    try:
        if is_playlist_url(url):
            print_playlist_result(url)
        else:
            print_video_result(url)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()