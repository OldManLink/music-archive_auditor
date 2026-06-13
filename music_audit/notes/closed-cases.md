Case #001
=========
Album:
King Crimson – In The Court Of The Crimson King

Finding:
incomplete_album_by_metadata

Root Cause:
Album intentionally split into
main album + bonus tracks

Repair:
Updated track numbering and
total track counts

Audio Changes:
None

Status:
Closed (2026-06-13)

# Case #002

Album:
George Benson – Give Me The Night

Finding:
mixed_audio_formats

Evidence:
Album contained 10 MP3 files and 1 M4A file.

```
The MP3 files were all encoded by iTunes 10.1.2 at
160 kbps and shared a common timestamp from
2011-02-11.

The M4A file:

    06 Dinorah, Dinorah.m4a

was encoded as AAC at approximately 128 kbps,
had an older timestamp from 2009-09-13, and
lacked the iTunes 10.1.2 encoder metadata.
```

Investigation:
The M4A file was determined to be an obsolete
survivor from an earlier state of the archive.

```
The album appears to have been re-ripped in its
entirety in 2011, producing a complete set of
10 MP3 files.

The older AAC file remained in the directory and
was not removed during the repair.
```

Root Cause:
Legacy survivor from a previous archive state.

Repair:
Removed obsolete file:

```
    06 Dinorah, Dinorah.m4a
```

Status:
Closed (2026-06-13)

Notes:
This case provides evidence that at least some
archive damage may have been discovered and
repaired manually many years before the MAA
investigation began.
