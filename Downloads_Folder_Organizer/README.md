# Downloads Organizer

A simple Python script that tidies your Downloads folder by sorting files into subfolders based on their file type.

## What It Does

- Scans your `Downloads` folder (top level only, not subfolders).
- Moves each file into a category folder based on its extension.
- Creates category folders only when they are needed.
- Renames duplicates instead of overwriting or skipping them (e.g. `report.pdf` becomes `report (1).pdf`).
- Leaves hidden files and unrecognised file types where they are.
- Prints each move and a short summary when finished.

## Categories

| Folder      | Extensions                                                        |
|-------------|-------------------------------------------------------------------|
| Images      | .jpg, .jpeg, .png, .webp, .gif, .bmp, .svg                        |
| Documents   | .pdf, .txt, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .csv           |
| Videos      | .mp4, .mov, .avi, .mkv                                            |
| Audio       | .mp3, .wav, .flac, .m4a                                           |
| Archives    | .zip, .rar, .7z, .tar, .gz                                        |

## Requirements

- Python 3.6 or newer
- No extra packages needed (uses only the standard library: `pathlib` and `shutil`)

## Usage

1. Save the script as `organize_downloads.py`.
2. (Recommended) Open the file and set `DRY_RUN = True` to preview what would happen without moving anything.
3. Run it:

   ```
   python organize_downloads.py
   ```

4. Once you are happy with the preview, set `DRY_RUN = False` and run it again.

### Example Output

```
Moved holiday.jpg -> Images/holiday.jpg
Moved invoice.pdf -> Documents/invoice (1).pdf
Moved song.mp3 -> Audio/song.mp3

Done. Moved: 3, left alone: 5, failed: 0
```

## Customising

- **Add or change file types:** edit the `CATEGORIES` dictionary near the top of the script.
- **Add a new category:** add a new entry, for example `"Code": {".py", ".js", ".html"}`.
- **Use a different folder:** change the `DOWNLOADS` path, or call `organize(Path("/path/to/folder"))`.

## Notes

- Files that are locked or in use by another program are skipped, and the script reports them as failed rather than crashing.
- Moving files is not automatically reversible, so use dry-run mode first if you have an important Downloads folder.
- Files inside existing subfolders are not touched.
