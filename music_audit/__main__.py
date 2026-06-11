from pathlib import Path
import sys

from music_audit.timing import Timer
from datetime import datetime
from music_audit.scanner import scan_audio_files
from music_audit.grouping import group_albums
from music_audit.checks.single_track import check_single_track_album
from music_audit.checks.apple_format_single_track import check_apple_format_single_track_album
from music_audit.analysis.modification_clusters import count_single_track_modification_dates
from music_audit.checks.mixed_formats import check_mixed_audio_formats

def main() -> int:
    root = Path(sys.argv[1])
    timer = Timer()
    print(
        f"Started scan at "
        f"{datetime.now().isoformat(sep=' ', timespec='seconds')}"
    )

    audio_files = scan_audio_files(root)
    albums = group_albums(audio_files)

    print(f"Scanned {len(audio_files)} audio files")
    print(f"Grouped {len(albums)} albums")
    print("Checking albums...")

    findings = []

    for index, album in enumerate(albums, start=1):
        findings.extend(check_single_track_album(album))
        findings.extend(check_apple_format_single_track_album(album))
        findings.extend(check_mixed_audio_formats(album))

        if index % 50 == 0:
            print(f"  checked {index} / {len(albums)} albums")
    print(f"  checked {len(albums)} / {len(albums)} albums")

    for finding in findings:
        print(f"[{finding.score}] {finding.category}: {finding.album.path}")

        if finding.category == "single_track_album":
            file = finding.album.files[0]

            print(f"    file: {file.path.name}")
            print(f"    size: {file.size_mb:.1f} MB")
            print(f"    modified: {file.modified_time}")

        if finding.category == "mixed_audio_formats":
            print(
                f"    formats: "
                f"{finding.message.removeprefix('Album contains multiple audio formats: ')}"
            )

            non_mp3_files = [
                file
                for file in finding.album.files
                if file.extension != ".mp3"
            ]

            print("    non-mp3 files:")

            for file in non_mp3_files:
                print(f"        {file.path.name}")
                print(f"            size: {file.size_mb:.1f} MB")
                print(f"            modified: {file.modified_time}")
    print()
    print("Single-track album modification dates")

    for date, count in count_single_track_modification_dates(albums):
        print(f"{date}: {count}")

    print(f"Finished in {timer.elapsed:.1f} seconds")
    print(f"Found {len(audio_files)} audio files")
    print(f"Found {len(albums)} albums")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
