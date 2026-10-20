# YouTube Downloader

A simple command-line Python script that downloads a YouTube video, or just its audio, using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Downloads video as MP4 at your chosen maximum quality (default 1080p).
- Audio-only mode that saves as MP3.
- Shows live download progress.
- Handles errors (invalid links, private videos, network issues) without crashing.
- Downloads a single video even if the link is part of a playlist.
- Saves to `Downloads/YouTube` by default.

## Requirements

- Python 3.8 or newer
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (merges video and audio, and converts to MP3)

## Installation

1. Install yt-dlp:

   ```
   pip install yt-dlp
   ```

2. Install ffmpeg:

   | System  | Command                    |
   |---------|----------------------------|
   | Windows | `winget install ffmpeg`    |
   | macOS   | `brew install ffmpeg`      |
   | Linux   | `sudo apt install ffmpeg`  |

## Usage

```
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

If you run the script without a URL, it will ask you to paste one.

### Options

| Option             | Description                                    | Default              |
|--------------------|------------------------------------------------|----------------------|
| `-a`, `--audio`    | Download audio only and convert to MP3         | off (video)          |
| `-q`, `--quality`  | Maximum video height, e.g. 480, 720, 1080      | 1080                 |
| `-o`, `--output`   | Folder to save the file in                     | `~/Downloads/YouTube`|

### Examples

```
python youtube_downloader.py URL --quality 720
python youtube_downloader.py URL --audio
python youtube_downloader.py URL --output ~/Videos
```

## Troubleshooting

- **"yt-dlp is not installed":** run `pip install yt-dlp`.
- **Errors about ffmpeg:** make sure ffmpeg is installed and available in your system PATH.
- **Download suddenly stops working:** YouTube changes often, so update yt-dlp with `pip install -U yt-dlp`.

## Legal Note

Only download videos that you own, that are freely licensed, or that you have permission to save. YouTube's Terms of Service restrict downloading other content.
