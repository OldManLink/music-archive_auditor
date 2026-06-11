# Live Run 002

Date: 2026-06-11

## Purpose

Enhance the initial single-track album report with additional forensic information:

* surviving filename
* file extension
* file size
* modification timestamp

Add modification date clustering analysis to identify potential historical damage events.

---

## Collection Summary

Audio files found: 7,406

Albums found: 583

Single-track albums detected: 38

Scan duration: 57.2 seconds

---

## Key Discovery

A very large proportion of suspicious albums share the same modification date:

```text
2009-09-13: 26 albums
```

This represents:

```text
26 / 38 = 68.4%
```

of all currently detected single-track albums.

All remaining modification dates occur only once.

---

## Modification Date Distribution

```text
2009-09-13: 26
2008-12-02: 1
2008-12-16: 1
2009-01-14: 1
2009-07-20: 1
2009-08-03: 1
2010-11-01: 1
2010-12-16: 1
2011-02-18: 1
2012-11-28: 1
2013-01-22: 1
2013-09-09: 1
2025-07-12: 1
```

---

## Interpretation

The concentration around 2009-09-13 is unlikely to be explained by normal manual activity.

Observations:

* Affected albums span many artists and genres.
* Many survivors are M4A files.
* Most clustered files were modified within a very short time window.
* The affected albums appear to have lost most or all of their original contents.
* The surviving tracks are often well-known tracks from the affected albums.

Examples include:

```text
AC/DC - Highway To Hell
Coolio - Gangsta's Paradise
Extreme - Pornograffitti
The Clash - London Calling
Earth Wind & Fire - All 'n All
Fine Young Cannibals - The Raw And The Cooked
```

This strongly suggests that an automated process acted on many albums at approximately the same time.

---

## Apple Survivor Hypothesis

The original APPLE_SURVIVOR_TRACK heuristic assumed:

```text
single track
M4A
title matches album title
```

Live data has shown that this definition is too narrow.

Examples:

```text
Highway To Hell
  surviving track:
  Walk All Over You.m4a

Pornograffitti
  surviving track:
  More Than Words.m4a

All 'n All
  surviving track:
  Fantasy.m4a
```

The broader pattern appears to be:

```text
single-track album
surviving M4A file
modification timestamp clustered around 2009-09-13
```

This may be a more useful future detection rule.

---

## Historical Context

The date 2009-09-13 is particularly interesting.

This falls very close to the transition period between Leopard and Snow Leopard.

While no conclusion can yet be drawn regarding root cause, the clustering is consistent with some form of migration, import, synchronization, consolidation, or library-repair operation occurring around that time.

The data currently supports:

> "A significant automated event affected many albums on 2009-09-13."

The data does not yet identify the exact mechanism.

---

## Conclusions

Music Archive Auditor has already achieved its primary objective:

```text
From:
"I have no idea how much damage exists."

To:
"There are currently 38 albums requiring investigation."
```

In addition, the tool has uncovered a statistically significant modification-date cluster that was previously unknown.

This cluster is now the leading forensic lead in the investigation.

---

## Suggested Next Step

Analyse the relationship between:

* modification date
* file format
* survivor count

Specifically:

```text
2009-09-13
  M4A: ?
  MP3: ?
```

to determine whether the cluster is primarily associated with Apple-managed formats.
