from pathlib import Path
import sys

import argparse
from music_audit.timing import Timer
from datetime import datetime
from music_audit.scanner import scan_audio_files
from music_audit.grouping import group_albums
from music_audit.checks.single_track import check_single_track_album
from music_audit.analysis.modification_clusters import count_single_track_modification_dates
from music_audit.checks.mixed_formats import check_mixed_audio_formats
from music_audit.formatting import format_bytes
from music_audit.metadata import read_metadata

def main() -> int:
    METADATA_PROGRESS_INTERVAL = 500

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        help="Music root directory",
    )
    parser.add_argument(
        "--limit",
        type=int,
    )
    args = parser.parse_args()

    timer = Timer()
    print(
        f"Started scan at "
        f"{datetime.now().isoformat(sep=' ', timespec='seconds')}"
    )

    if args.limit is not None:
        print(f"Processing limit: {args.limit} files")

    root = Path(args.root)
    audio_files = scan_audio_files(
        root,
        limit=args.limit,
    )

    total_size = sum(file.size_bytes for file in audio_files)
    print(f"Scanned {len(audio_files)} audio files")
    print(f"Total size: {format_bytes(total_size)}")

    metadata_timer = Timer()
    print("Reading metadata...")
    metadata_count = 0
    metadata_by_path = {}
    for audio_file in audio_files:
        metadata = read_metadata(audio_file.path)
        metadata_by_path[audio_file.path] = metadata
        metadata_count += 1

        if (
            metadata_count % METADATA_PROGRESS_INTERVAL == 0
            or metadata_count == len(audio_files)
        ):
            print(f"  read {metadata_count} / {len(audio_files)} files")

    print(
        f"Metadata probe read {metadata_count} files "
        f"in {metadata_timer.elapsed:.1f} seconds"
    )

    albums = group_albums(audio_files)
    print(f"Grouped {len(albums)} albums")
    print("Checking albums...")

    findings = []

    for index, album in enumerate(albums, start=1):
        findings.extend(check_single_track_album(album))
        findings.extend(check_mixed_audio_formats(album))

        if index % 50 == 0:
            print(f"  checked {index} / {len(albums)} albums")
    print(f"  checked {len(albums)} / {len(albums)} albums")

    for finding in findings:
        print(f"[{finding.score}] {finding.category}: {finding.album.path}")

        if finding.category == "single_track_album":
            file = finding.album.files[0]
            metadata = metadata_by_path.get(file.path)

            print(f"    file: {file.path.name}")
            print(f"    size: {file.size_mb:.1f} MB")
            print(f"    modified: {file.modified_time}")

            if metadata is not None and metadata.track_number is not None:
                if metadata.track_total is None:
                    print(f"    metadata: track {metadata.track_number}")
                else:
                    print(
                        f"    metadata: track "
                        f"{metadata.track_number} of {metadata.track_total}"
                    )
                if metadata.encoder is not None:
                    print(f"    encoder: {metadata.encoder}")
                print(f"    sample rate: {metadata.sample_rate} Hz")

            if file.extension == ".m4a":
                print("    suspicious: apple-format survivor")

        if finding.category == "mixed_audio_formats":
            mp3_count = sum(
                1
                for file in finding.album.files
                if file.extension == ".mp3"
            )

            non_mp3_files = [
                file
                for file in finding.album.files
                if file.extension != ".mp3"
            ]

            print(f"    {mp3_count} mp3 files")
            print(f"    {len(non_mp3_files)} non-mp3 files")
            print("    non-mp3 files:")

            for file in non_mp3_files:
                metadata = metadata_by_path.get(file.path)
                print(f"        {file.path.name}")
                print(f"            size: {file.size_mb:.1f} MB")
                print(f"            modified: {file.modified_time}")


                if metadata is not None and metadata.track_number is not None:
                    if metadata.track_total is None:
                        print(f"            metadata: track {metadata.track_number}")
                    else:
                        print(
                            f"            metadata: track "
                            f"{metadata.track_number} of {metadata.track_total}"
                        )
                    print(f"            album: {metadata.album}")
                    print(f"            artist: {metadata.artist}")
                    if metadata.encoder is not None:
                        print(f"            encoder: {metadata.encoder}")
                    print(f"            sample rate: {metadata.sample_rate} Hz")

    clusters = count_single_track_modification_dates(albums)
    if clusters:
        print()
        print("Single-track album modification dates")

        for date, count in count_single_track_modification_dates(albums):
            print(f"{date}: {count}")

    print(f"Finished in {timer.elapsed:.1f} seconds")
    print(f"Found {len(audio_files)} audio files")
    print(f"Found {len(albums)} albums")
    print(f"Total size: {format_bytes(total_size)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
