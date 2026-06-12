# Live run 004 
## Hidden Casualties Discovered

Date: 2026-06-12
Command:

```bash
.venv/bin/python3 -m music_audit /Volumes/media/Music
```

## Summary

The first full metadata-enabled scan of the archive was completed successfully.

The scan processed:

* 7406 audio files
* 583 albums
* 36.4 GB total archive size

Metadata was successfully read from all files, confirming that track numbers, track totals, sample rates, and some encoder information can be extracted and analysed.

## Major Finding

Prior to metadata analysis, the investigation focused on obvious damage, primarily albums containing only a single surviving track.

The new metadata-based completeness check has revealed a second category of damage:

**Albums that appear partially intact but are missing tracks.**

Examples discovered during the first full run include:

* Joan Baez – *Baez Sings Dylan* (20 expected, 17 found)
* Bim Sherman – *It Must Be A Dream* (11 expected, 7 found)
* Cat Stevens – *Matthew & Son* (22 expected, 16 found)
* John Martyn – *Sweet Little Mysteries: The Island Anthology [Disc 1]* (18 expected, 3 found)
* King Crimson – *In The Court Of The Crimson King* (10 expected, 5 found)
* King Crimson – *In The Court Of The Crimson King [Bonus Tracks]* (10 expected, 5 found)
* Rammstein – *Live aus Berlin* (16 expected, 15 found)

These albums would not have been detected by the original single-track-album check.

## Significance

This confirms that archive damage is not limited to complete album collapse.

The current evidence now supports three distinct categories:

### 1. Healthy Albums

All expected tracks appear to be present.

### 2. Contaminated Albums

Album largely survives, but individual tracks appear to have been replaced or re-encoded.

Current example:

* George Benson – *Give Me The Night*

### 3. Damaged Albums

Albums missing one or more tracks.

This category includes both:

* Complete collapse (single surviving track)
* Partial loss (multiple tracks missing)

## Metadata Evidence

Several surviving files contain useful metadata including:

* Track number
* Track total
* Sample rate
* Encoder information

Examples observed:

* iTunes 8.0.2
* iTunes 8.2
* iTunes v7.7.1
* iTunes v6.0.5
* "by Gnocc@"

The presence of encoder information suggests future opportunities to classify files by origin and acquisition method.

## Conclusions

The metadata phase has already justified itself.

The investigation has moved beyond simply identifying damaged albums and can now detect hidden losses that would not be obvious from directory contents alone.

The discovery of multiple partially damaged albums represents the most significant finding since the original identification of the 2009-09-13 survivor cluster.
