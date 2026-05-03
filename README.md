# 🎥 YouTube Duration Checker Suite

A collection of lightweight and efficient Python tools to quickly fetch the duration and status of YouTube content. Whether it's a single video, a short, a live stream, or an entire playlist, these scripts provide accurate timing data directly in your terminal.

## ✨ Features

- 🕒 **Accurate Duration**: Get exact durations in `HH:MM:SS` format.
- 📂 **Playlist Support**: Calculate the total duration of entire playlists, with per-video breakdowns.
- 📺 **Wide Compatibility**: Works with regular videos, YouTube Shorts, Live Streams, and Premieres.
- 📡 **Live Status Detection**: Identifies if content is "Currently Live", "Scheduled", "Regular", or a "Replay".
- 🚀 **Fast & Simple**: Minimalistic CLI interface with no API keys required.

## 🛠️ Scripts Overview

| Script | Primary Use Case | Supports Playlists? |
| :--- | :--- | :---: |
| `playlist_durationchecker.py` | **Comprehensive tool** for both single videos and full playlists. | ✅ Yes |
| `sayan.py` | **Lightweight tool** optimized for single video checks. | ❌ No |

## ⚙️ Prerequisites & Installation

Ensure you have Python 3.x installed. These tools utilize the powerful `yt-dlp` engine for metadata extraction.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sayanpal514-hue/Youtube-Video-or-Playlist-Duration-Checker.git
   cd "YT VIDEO DURATION CHECKER"
   ```

2. **Install the dependency**:
   ```bash
   pip install yt-dlp
   ```

## 🚀 Usage

### 1. Playlist & Video Checker (`playlist_durationchecker.py`)
This is the recommended script for most users as it handles any YouTube URL.

```bash
# Interactive mode
python playlist_durationchecker.py

# Direct URL argument
python playlist_durationchecker.py "https://youtube.com/playlist?list=..."
```

### 2. Single Video Checker (`sayan.py`)
A simpler version dedicated to checking single video durations.

```bash
python sayan.py "https://www.youtube.com/watch?v=..."
```

## 📊 Example Outputs

### Playlist Result (`playlist_durationchecker.py`)
```text
Playlist : Sunday Suspense | Byomkesh Bakshi
Videos   : 24  |  Skipped: 0
Total    : 46:34:27  (167667 seconds)
--------------------------------------------------
  [  1]  03:52:21   Sunday Suspense | Sajarur Knaata | ব্যোমকেশ বক্সী...
  [  2]  01:26:23   Sunday Suspense Classics | Uposanghar | ব্যোমকেশ...
  ...
--------------------------------------------------
  Total Duration : 46:34:27
```

### Single Video Result Even Ongoing Premieres Video (`sayan.py`)
```text
Title    : Sunday Suspense | Potashgarh er Jongoley
Status   : Regular Video
Duration : 02:56:40  (10600 seconds)
```

## 🔧 Technologies Used

- **Python 3**: The core logic and CLI.
- **yt-dlp**: High-performance metadata extraction.

---
Developed with ❤️ by [SAYAN PAL](https://github.com/sayanpal514-hue)
