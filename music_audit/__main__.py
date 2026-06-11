from pathlib import Path
import sys

from music_audit.timing import Timer
from datetime import datetime
from music_audit.scanner import scan_audio_files
from music_audit.grouping import group_albums
from music_audit.checks.single_track import check_single_track_album
from music_audit.checks.apple_survivor import check_apple_survivor_track


def main() -> int:
    root = Path(sys.argv[1])
    timer = Timer()
    print(
        f"Started scan at "
        f"{datetime.now().isoformat(sep=' ', timespec='seconds')}"
    )

    audio_files = scan_audio_files(root)
    albums = group_albums(audio_files)

    findings = []

    for album in albums:
        findings.extend(check_single_track_album(album))
        findings.extend(check_apple_survivor_track(album))

    for finding in findings:
        print(
            f"[{finding.score}] "
            f"{finding.category}: "
            f"{finding.album.path}"
        )

    print(f"Finished in {timer.elapsed:.1f} seconds")
    print(f"Found {len(audio_files)} audio files")
    print(f"Found {len(albums)} albums")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
