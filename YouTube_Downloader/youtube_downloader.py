"""Download a YouTube video (or just its audio) using yt-dlp.

Usage:
    python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
    python youtube_downloader.py URL --audio
    python youtube_downloader.py URL --quality 720 --output ~/Videos

Requirements:
    pip install yt-dlp
    ffmpeg (needed to merge video + audio and to convert to MP3)
"""

import argparse
import sys
from pathlib import Path

try:
    import yt_dlp
    from yt_dlp.utils import DownloadError
except ImportError:
    sys.exit("yt-dlp is not installed. Run: pip install yt-dlp")

DEFAULT_OUTPUT = Path.home() / "Downloads" / "YouTube"


def progress_hook(d: dict) -> None:
    """Print a simple one-line progress indicator."""
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        eta = d.get("_eta_str", "").strip()
        print(f"\rDownloading: {percent} at {speed}, ETA {eta}   ", end="", flush=True)
    elif d["status"] == "finished":
        print("\nDownload finished, processing file...")


def build_options(output_dir: Path, audio_only: bool, max_height: int) -> dict:
    """Create the yt-dlp options for video or audio-only downloads."""
    options = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "progress_hooks": [progress_hook],
        "noplaylist": True,  # download only the single video, not the whole playlist
        "quiet": True,
        "no_warnings": True,
    }

    if audio_only:
        options["format"] = "bestaudio/best"
        options["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    else:
        options["format"] = (
            f"bestvideo[height<={max_height}]+bestaudio/best[height<={max_height}]"
        )
        options["merge_output_format"] = "mp4"

    return options


def download(url: str, output_dir: Path, audio_only: bool, max_height: int) -> bool:
    """Download the given URL. Returns True on success, False on failure."""
    output_dir.mkdir(parents=True, exist_ok=True)
    options = build_options(output_dir, audio_only, max_height)

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Saved: {info.get('title', 'video')}")
            print(f"Location: {output_dir}")
        return True
    except DownloadError as e:
        print(f"\nDownload failed: {e}")
    except KeyboardInterrupt:
        print("\nCancelled by user.")
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download a YouTube video or its audio.")
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "-o", "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"folder to save into (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "-a", "--audio", action="store_true",
        help="download audio only and convert it to MP3",
    )
    parser.add_argument(
        "-q", "--quality", type=int, default=1080,
        help="maximum video height, e.g. 480, 720, 1080 (default: 1080)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    url = args.url or input("Paste the YouTube URL: ").strip()

    if not url:
        sys.exit("No URL provided.")

    success = download(url, args.output.expanduser(), args.audio, args.quality)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
