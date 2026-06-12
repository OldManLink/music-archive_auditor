# Live Run 003

Date: 2026-06-12
Command:

```bash
.venv/bin/python3 -m music_audit /Volumes/media/Music
```

## Purpose

Investigate mixed-format albums to determine whether Apple-format files appear inside otherwise MP3-based albums.

This check was motivated by the hypothesis that the 2009-09-13 event may have affected albums that were not reduced to a single surviving track.

---

## New Check

Category:

```text
mixed_audio_formats
```

Criteria:

```text
Album contains more than one audio format.
```

Example:

```text
.mp3 + .m4a
```

Severity:

```text
WARNING
```

Score:

```text
40
```

---

## Results

Only two mixed-format albums were detected in the entire collection.

### Arcadia — Arcadia Sings

```text
Formats:
  .m4a=2
  .mp3=2

Files:
  Arcadia.m4a
      modified: 2010-11-10

  Favourite Things.m4a
      modified: 2010-11-10
```

Observation:

This does not appear related to the 2009 cluster.

The modification dates are later and the album contains a roughly even split of formats.

Current assessment:

```text
Interesting
but not obviously suspicious.
```

---

### George Benson — Give Me The Night

```text
Formats:
  .mp3=10
  .m4a=1

M4A file:
  06 Dinorah, Dinorah.m4a
      modified: 2009-09-13 22:39:19
```

Observation:

The modification timestamp falls directly inside the previously identified 2009 cluster.

---

## Key Discovery

This is the first confirmed example of:

```text
An album affected by the 2009 event
without being reduced to a single track.
```

Prior to this run, all evidence pointed toward:

```text
album
    ->
single surviving track
```

The George Benson album demonstrates that the event can also produce:

```text
album
    ->
mostly intact
    +
isolated M4A replacement
```

This significantly expands the scope of the investigation.

---

## Revised Understanding

Old model:

```text
Damage manifests as
single-track albums.
```

New model:

```text
Damage may manifest as:

1. Single surviving track
2. Partial album replacement
3. Isolated M4A contamination
```

The single-track detector therefore identifies only a subset of potentially affected albums.

---

## Implications

The 2009-09-13 event appears to have modified albums in more than one way.

The current evidence supports:

```text
Single-track casualties
+
Partial survivors
```

This increases confidence that the event was a bulk automated process rather than random file loss.

---

## Future Investigation

Potential future checks:

### M4A files inside MP3 albums

Detect:

```text
Album contains mostly MP3 files
plus a small number of M4A files.
```

Especially where:

```text
M4A modification date
==
2009-09-13
```

### Archive-wide date analysis

Determine whether:

```text
2009-09-13
```

was:

```text
A collection-wide migration date
```

or

```text
A damage-specific event.
```

### Metadata analysis

Read:

```text
track number
track total
encoder
comments
```

to identify incomplete albums and possible source fingerprints.

---

## Conclusion

The mixed-format check produced only two findings, but one of them is highly significant.

The George Benson album demonstrates that the 2009-09-13 event affected at least one album that was not reduced to a single track.

This is the strongest evidence so far that the current list of 38 damaged albums may not represent the full extent of the impact.
