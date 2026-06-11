# Live Run 001

Date: 2026-06-11
Command:

```bash
.venv/bin/python3 -m music_audit /Volumes/media/Music
```

## Summary

First live run of Music Archive Auditor against the real NAS-mounted music collection.

The tool successfully completed a full scan and produced the first list of albums requiring attention.

## Runtime

Started scan at: 2026-06-11 18:27:28
Finished in: 71.4 seconds

## Collection Size

Audio files found: 7,406
Albums found: 583

## Findings

Total findings: 38

All findings in this first run were:

```text
single_track_album
```

No `apple_survivor_track` findings were reported in this run.

## Initial Observations

The tool is already useful: it reduced the vague concern “some albums may be damaged” to a concrete investigation list of 38 album folders.

The known suspicious album was detected:

```text
/Volumes/media/Music/AC_DC/Highway To Hell
```

This confirms that the first vertical slice can detect at least one real-world damaged album candidate.

## Albums Flagged

```text
AC_DC / Highway To Hell
Bobby Brown / Dance!...Ya Know It!
Chesney Hawkes / Buddy's Song
Compilations / Brahms' Lullaby and Other Classical Music for Children
Compilations / Couldn't Get It Right...plus {detailed info!}
Compilations / För minnenas skull [Disc 2]
Compilations / Goodbye Yellow Brick Road
Compilations / Living In The Past
Compilations / Pirates of Penzance
Compilations / Sweet Little Mysteries_ The Island Anthology [Disc 2]
Compilations / The Best Of James Bond 30th Anniversary Collection
Compilations / The Best Of Thomas Dolby_ Retrospectacle
Coolio / Gangsta's Paradise
Earth Wind & Fire / All 'n All
Elvis Costello & The Attractions / Best Of
Eric Gadd / Do You Believe In Gadd
Extreme / Pornograffitti
Fine Young Cannibals / The Raw And The Cooked
France Gall / Babacar
Indigo Girls & Joan Baez / Unknown Album
Joan Baez / Ring Them Bells
Louise Hoffsten / Rhythm & Blonde
Lucio Battisti / Le avventure di Lucio Battisti e Mogol
Lucio Battisti / Le avventure di Lucio Battisti e Mogol cd 1
Mylène Farmer / Ainsi Soit Je .._
Nathalie Remy / Behöver Dig
Rotary Connection / I Am The Black Gold Of The Sun - Remastered
Santana / Abraxas [Original Master Recording]
The Cardigans / Gran Turismo
The Clash / London Calling
The Kloons / The Kloons
The Noveltones / Left Bank Two
The xx / Sunset (Jamie xx Edit) - Single
Tobias Hayes / Mum's Funeral
UNI Singers / Giovanni Pierluigi da Palestrina
Various Artists / Working in the Coal Mine
Vaughan Williams / Cantaton Homework
dB soundworks / Canabalt Soundtrack + Ringtones Pack (w_ bonus Fathom Megamix!)
```

## Notes for Next Development Step

The next useful improvement is to include the filename and extension for each single-track album.

This will help distinguish between:

* genuinely suspicious single surviving tracks
* intentional singles
* soundtrack/ringtone packs
* personal recordings
* compilation edge cases
* known one-track albums

It will also explain why `Highway To Hell` did not trigger `apple_survivor_track`: likely due to case, filename mismatch, extension mismatch, or folder/title normalization.
