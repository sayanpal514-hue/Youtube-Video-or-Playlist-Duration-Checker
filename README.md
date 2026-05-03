# 🎥 YouTube Video Duration Checker

A lightweight and efficient Python tool to quickly fetch the duration and status of any YouTube video, including regular videos, shorts, live streams, and premieres.

## ✨ Features

- 🕒 **Accurate Duration**: Get the exact duration in `HH:MM:SS` format.
- 📺 **Wide Support**: Works with regular videos, YouTube Shorts, Live Streams, and Premieres.
- 📡 **Live Status Detection**: Identifies if a video is "Currently Live", "Scheduled", "Regular", or a "Replay".
- 🚀 **Fast & Simple**: Minimalistic CLI interface for quick checks.

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed on your system. This tool relies on the powerful `yt-dlp` library.

## 📥 Installation

1. **Clone the repository** (or just download `sayan.py`):
   ```bash
   git clone https://github.com/yourusername/yt-video-duration-checker.git
   cd "YT VIDEO DURATION CHECKER"
   ```

2. **Install the required dependency**:
   ```bash
   pip install yt-dlp
   ```

## 🚀 Usage

You can run the script in two ways:

### 1. Interactive Mode
Simply run the script and paste the URL when prompted:
```bash
python sayan.py
```

### 2. Command Line Argument
Pass the URL directly as an argument:
```bash
python sayan.py "https://www.youtube.com/watch?v=example"
```

## 📊 Example Output

```text
Enter YouTube video URL: https://www.youtube.com/watch?v=eptQr18DJCE

Fetching info for: https://www.youtube.com/watch?v=eptQr18DJCE
--------------------------------------------------
Title    : Sunday Suspense | Potashgarh er Jongoley
Status   : Regular Video
Duration : 02:56:40  (10600 seconds)
```

## 🔧 Technologies Used

- **Python 3**: The core logic.
- **yt-dlp**: The engine used for metadata extraction.

---
Developed with ❤️ by [Sayan Pal]
