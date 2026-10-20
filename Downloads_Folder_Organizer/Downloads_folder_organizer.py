from pathlib import Path
import shutil

DOWNLOADS = Path.home() / "Downloads"
DRY_RUN = False  # set True to preview without moving anything

CATEGORIES = {
    "Images":    {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".svg"},
    "Documents": {".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md", ".json", ".xml", ".py", ".ipynb"},
    "Videos":    {".mp4", ".mov", ".avi", ".mkv"},
    "Audio":     {".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma", ".opus", ".aiff", ".alac", ".amr", ".mid", ".midi"},
    "Archives":  {".zip", ".rar", ".7z", ".tar", ".gz"},
}

# Build a direct extension -> folder lookup
EXT_TO_FOLDER = {ext: folder for folder, exts in CATEGORIES.items() for ext in exts}


def unique_target(path: Path) -> Path:
    """Return a non-clashing path: file.pdf -> file (1).pdf -> file (2).pdf"""
    counter = 1
    candidate = path
    while candidate.exists():
        candidate = path.with_name(f"{path.stem} ({counter}){path.suffix}")
        counter += 1
    return candidate


def organize(folder: Path = DOWNLOADS, dry_run: bool = DRY_RUN) -> None:
    moved = skipped = failed = 0

    for file in folder.iterdir():
        if not file.is_file() or file.name.startswith("."):
            continue

        category = EXT_TO_FOLDER.get(file.suffix.lower())
        if category is None:
            skipped += 1
            continue

        target_dir = folder / category
        target = unique_target(target_dir / file.name)

        if dry_run:
            print(f"[dry run] {file.name} -> {category}/{target.name}")
            moved += 1
            continue

        try:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(target))
            print(f"Moved {file.name} -> {category}/{target.name}")
            moved += 1
        except (PermissionError, OSError) as e:
            print(f"Could not move {file.name}: {e}")
            failed += 1

    print(f"\nDone. Moved: {moved}, left alone: {skipped}, failed: {failed}")


if __name__ == "__main__":
    organize()